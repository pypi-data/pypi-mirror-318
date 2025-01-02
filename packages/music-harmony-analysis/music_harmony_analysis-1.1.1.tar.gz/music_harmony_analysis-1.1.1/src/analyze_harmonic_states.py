from typing import List, Tuple

from type import Key, HarmonicState, HarmonicAnalysis, Music, PCSet, all_keys, key_to_pcset


# Function to analyze music and return HarmonicAnalysis
def analyze_harmonic_states(m: Music, start_harmonic_state = all_keys) -> HarmonicAnalysis:
    """
    Input:
    - m: Music, a list of tuples (pcset, duration), where pcset is a List of pitchclasses, where pitchclass is a int in range 0-11 and duration is a Fraction object. duration is not used in this function, but is part the return value.

    Output:
    - harmonic_analysis: List of tuples: ((pcset, duration), new_harmonic_state), where (pcset, duration) are the musical events from music and new_harmonic_state is the new harmonic state (a list of keys) after this event.

    Calculates the harmonic analysis of the given music. A harmonic state is the set of all keys that a listener of the music can consider as the current key, based on a theory of musical harmony perception https://www.tonalemusik.de/lexikon/modulation.htm#Modulation.
    For most of the time in tonal music, this harmonic state is a single key, but there are times where there are multiple possible keys simultaneously ('tonale Indifferenz').

    Example:
    music = [
        ([2, 5, 7, 11], Fraction(1, 4)), # G7
        ([0, 4, 7], Fraction(1, 4)), # C
        ([2, 6, 9], Fraction(1, 4)), # D
        ([2, 7, 11], Fraction(1, 4)) # G
    ]
    analyze_harmonic_states(music) -> [
        (([2, 5, 7, 11], Fraction(1, 4)), [(0, 'dur'), (0, 'moll')]),
        (([0, 4, 7], Fraction(1, 4)), [(0, 'dur')]),
        (([2, 6, 9], Fraction(1, 4)), [(7, 'dur')]),
        (([2, 7, 11], Fraction(1, 4)), [(7, 'dur')])
    ]
    """
    return _analyze_harmonic_states(m, start_harmonic_state)


def _analyze_harmonic_states(m: Music, old_harmonic_state: HarmonicState) -> HarmonicAnalysis:
    """
    Input:
    - m: Music, a list of tuples (pcset, duration), where pcset is a List of pitchclasses, where pitchclass is a int in range 0-11 and duration is a Fraction object. duration is not used in this function, but is part the return value.
    - old_harmonic_state: List of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'. Represents the old harmonic state before the next musical event in music.

    Output:
    - harmonic_analysis: List of tuples: ((pcset, duration), new_harmonic_state), where (pcset, duration) are the musical events from music and new_harmonic_state is the new harmonic state (a list of keys) after this event.
    
    Calculates the harmonic analysis of the given music.
    """
    if not m:
        return []
    else:
        pcset, duration = m[0]
        possible_keys = calc_possible_keys(pcset)
        new_harmonic_state = calc_new_harmonic_state(old_harmonic_state, possible_keys)
        t = ((pcset, duration), new_harmonic_state)
        return [t] + _analyze_harmonic_states(m[1:], new_harmonic_state)


# Function to calculate possible keys based on PCSet
def calc_possible_keys(pcset: PCSet) -> List[Key]:
    """
    Input:
    - pcset: PCSet, a List of pitchclasses, where pitchclass is a int in range 0-11.

    Output:
    - List of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.

    Calculates all possible keys for the given pcset and returns them as a list of keys. (1. in the algorithm from the paper)
    Possible keys are all keys, where a maximum of the pitchclasses of the pcset are in the key.
    (For tonal pcsets exists always a key, where all pitchclasses are in the key, for atonal pcsets there are no such keys.)
    
    Keep in mind that for minor keys the harmonic minor scale with the raised 7th degree is used.

    Example:
    calc_possible_keys([0, 2, 4]) -> [ #The Pitchclasses for C, D and E
        (0, 'dur'),
        (5, 'dur'),
        (7, 'dur'),
        (9, 'moll')
    ]
    calc_possible_keys([0, 1, 2]) -> [ #The Pitchclasses for C, Cis and D, which is an atonal pcset. Because of that the return value will be all keys that have not three (there do not exist such keys), but one less: two pitchclasses of the pcset in it, because there exist such keys.
        (0, 'dur'),
        (0, 'moll'),
        (1, 'dur'),
        (1, 'moll'),
        (2, 'dur'),
        (2, 'moll'),
        (3, 'dur'),
        (5, 'dur'),
        (5, 'moll'),
        (6, 'moll'),
        (7, 'dur'),
        (7, 'moll'),
        (8, 'dur'),
        (9, 'dur'),
        (9, 'moll'),
        (10, 'dur'),
        (10, 'moll'),
        (11, 'moll')
    ]
    """
    keys_with_value = compare(all_keys, pcset)
    return [key for key, _ in get_max_tupel(keys_with_value)]


def calc_new_harmonic_state(old_harmonic_state: HarmonicState, possible_keys: List[Key]) -> HarmonicState:
    """
    Input:
    - old_harmonic_state: List of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'. Represents the old harmonic State before the current pcset in _analyze, for which the possible_keys argument was calculated.
    - possible_keys: List of keys: (pitchclass, mode). The possible keys of a pcset.

    Output:
    - new_harmonic_state: List of keys: (pitchclass, mode). The new harmonic state after the current pcset in _analyze.
    
    Calculates the new harmonic state based on the old harmonic state and the possible keys of a new pcset. (2. in the algorithm from the paper)
    For each key in possible_keys the highest number of equal pitchclasses with a key in old_harmonic_state is calculated.
    Then the keys with the highest number of equal pitchclasses are returned as a list.

    Keep in mind that for minor keys the harmonic minor scale with the raised 7th degree is used.

    Example:
    calc_new_harmonic_state(
        [(0, 'dur')],
        [(0, 'dur'), (1, 'dur'), (2, 'dur'), (3, 'moll')]
    ) -> [(0, 'dur')] #The key C major has the highest number of equal pitchclasses (7) with the key C major from old_harmonic_state.

    calc_new_harmonic_state(
        [(0, 'dur')],
        [(7, 'dur'), (1, 'dur'), (2, 'dur'), (3, 'moll')]
    ) -> [(7, 'dur')] #The key G major has the highest number of equal pitchclasses (6) with the key C major from old_harmonic_state.

    calc_new_harmonic_state(
        [(0, 'dur')],
        [(7, 'dur'), (5, 'dur'), (9, 'moll)]
    ) -> [(7, 'dur'), (5, 'dur'), (9, 'moll')] #The keys G major, F major and A minor have the highest number of equal pitchclasses (6) with the key C major.

    calc_new_harmonic_state(
        [(0, 'dur'),
        (1, 'dur')], [(0, 'dur'), (1, 'dur), (8, 'moll')]
    ) -> [(0, 'dur'), (1, 'dur')] #The keys C major and Cis major have the highest number of equal pitchclasses (7) with one of the keys C major and Cis major from old_harmonic_state. 
    """
    new_harmonic_state = [key for key, _ in get_max_tupel(
            [
                (key, max(
                        map(lambda x: x[1], compare(old_harmonic_state, key_to_pcset(key))) # For each key in possible_keys: Get the highest number of equal pitchclasses with any key in old_harmonic_state.
                    )) for key in possible_keys                                             
            ])
    ]

    return new_harmonic_state


# Function to compare keys with PCSet and return list of tuples of Key and int
def compare(keys: HarmonicState, pcset: PCSet) -> List[Tuple[Key, int]]:
    """
    Input:
    - keys: List of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.
    - pcset: List of pitchclasses, where pitchclass is a int in range 0-11.

    Output:
    - List of tuples (key, int), where int is the number of equal pitch classes between the key and the given pcset (see calc_how_many_equal_pcs).

    Calculates for each key in the given list of keys the number of equal pitch classes with the given pcset.
    Then returns a list of tuples (key, int), where int is the number of equal pitch classes between the key and the given pcset.
    Keep in mind that for minor keys the harmonic minor scale with the raised 7th degree is used.

    Example:
    compare(
        [(0, 'dur'), (1, 'dur'), (2, 'dur'), (3, 'moll')], #C major, Cis major, D major, Dis major
        [0, 2, 4] #The Pitchclasses for C, D and E
    ) -> [
        ((0, 'dur'), 3),
        ((1, 'dur'), 1), # The pitch class 0 is in the key Cis major, but 2 and 4 are not.
        ((2, 'dur'), 2), # D major has D and E, but not C.
        ((3, 'moll'), 1) # Dis minor (or Es minor) has Pitchclass 2 (Cisis (or D)), but not C or E.
        ]
    """
    return [(key, calc_how_many_equal_pcs(key, pcset)) for key in keys]

# Function to calculate how many equal pitch classes a Key has with a PCSet
def calc_how_many_equal_pcs(key: Key, pcset: PCSet) -> int:
    """
    Input:
    - key: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.
    - pcset: List of pitchclasses, where pitchclass is a int in range 0-11.

    Output:
    - int. The number of equal pitch classes between key and pcset.

    Returns the number of equal pitch classes between the pitchclasses of a key and the given pcset.

    Example:
    calc_how_many_equal_pcs((0, 'dur'), [0, 2, 4]) -> 3 #Pitchclasses 0 (C), 2 (D) and 4 (E) are in the key C major.
    calc_how_many_equal_pcs((0, 'dur'), [1, 3, 5]) -> 1 #Pitchclass 5 (F) is in the key C major, but 1 (C#) and 3 (D#) are not.
    """
    return len(set(key_to_pcset(key)).intersection(pcset))


def get_max_tupel(tupel_list: List[Tuple[Key, int]]) -> List[Tuple[Key, int]]:
    """
    Input:
    - tupel_list: List of tuples (key, quantity), where quantity is an int.
    
    Output:
    - List of tuples (key, quantity) of all the given tuples, of which quantity has the maximum value. If there are multiple tuples with the same maximum value, all of them are returned.

    Returns the maximum tuples from a list of tuples of Key and int. 'Maximum' is based on the int value of the tuple.

    Example:
    get_max_tupel([((0, 'dur'), 1), ((1, 'dur'), 2), ((2, 'dur'), 2), ((3, 'dur'), 1)]) -> [((1, 'dur'), 2), ((2, 'dur'), 2)]
    """
    max_quantity = max(map(lambda x: x[1], tupel_list))
    return [(key, quantity) for key, quantity in tupel_list if quantity == max_quantity]
