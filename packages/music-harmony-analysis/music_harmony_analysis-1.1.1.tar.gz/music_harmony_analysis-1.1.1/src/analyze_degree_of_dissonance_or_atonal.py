from type import key_to_pcset, all_keys 

def analyze_degree_of_dissonance_or_atonal(analysis):
    """
    Input:
    - analysis: List of tuples: ((pcset, duration), new_harmonic_state, sauterian_formula), where (pcset, duration) are the musical events from music and new_harmonic_state is the new harmonic state (a list of keys) after this event.
    sauterian_formula is a tuple of two lists: (tonal_result, atonal_pitches). tonal_result is a list of 9 booleans in the order: T1, T3, T5, D1, D3, D5, S1, S3, S5. This roughly corresponds to whether the scale degree for each field is used in the event, with exceptions: The scale degree 1 could be seen as T1 or as S5, the scale degree 5 could be seen as T5 or as D1. The sauterian_formula is defined in a way that the result is the most consonant interpretation (See degree_of_dissonances for more information). Example: The Chord CEG in C-Dur could be seen as T1,T3,T5,D1,S5, but removing D1 and S5 results in a less dissonant interpretation: T1,T3,T5, while still all pitches are used. For CEGA however, the sauterian_formula would be T1,T3,T5,S3,S5 because removing the S5 would not result in a more consonant interpretation. atonal_pitches is a list of pitches that are not in the key of the harmonic state.
    atonal_pitches is a list of pitches that are not in the key of the harmonic state.
    If a harmonic state of an event has multiple keys, the sauterian formula for this event is not defined and has the value 'ind.' ('indifference') instead.
    If the event has no pitches (a rest), sauterian_formula is '/'.

    Output:
    - analysis: List of tuples: ((pcset, duration), new_harmonic_state, sauterian_formula, degree_of_dissonance_or_atonal).

    Adds the degree of dissonance for each harmony to the analysis.

    degree_of_dissonance is either:
    Either "con", "fcon", "low", "mid", "high", "A1", "A2", "A3", "A4" or "A5". Or "ind." or "/". 
    "con": consonance
    "fcon": false consonance
    "low": low dissonance
    "med": medium dissonance
    "high": high dissonance
    "A<n>": atonal with n atonal pitches
    "ind.": indifferent: not atonal, but dissonance grade can't be determined because there are multiple keys in the harmonic state.
    "/": no pitches in this event.

    order of calculation:
    1. atonality
    2. pcset with exactly one pitch -> consonant
    3. indifferent or rest
    4. dissonance_degree.
    -> If the pcset is atonal and the harmonic state is indifferent, it will still be marked as atonal.
    -> a pcset with exactly one pitch is consonant, even in an indifferent harmonic state. (Because it will surely be consonant in every key.)
    """
    for i in range(len(analysis)):
        analysis[i] = (analysis[i][0], analysis[i][1], analysis[i][2], degree_of_dissonance_or_atonal(analysis[i]))
    return analysis


def degree_of_dissonance_or_atonal(event_analysis):
    """
    Input:
    - event_analysis: ((pcset, duration), harmonic_state, sauterian_formula), (but duration and harmonic_state are not needed here), each pitch in pcset is a int in range 0-11. harmonic_state is a list of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.
    sauterian_formula is a tuple of two lists: (tonal_result, atonal_pitches). tonal_result is a list of 9 booleans in the order: T1, T3, T5, D1, D3, D5, S1, S3, S5. This roughly corresponds to whether the scale degree for each field is used in the event, with exceptions: The scale degree 1 could be seen as T1 or as S5, the scale degree 5 could be seen as T5 or as D1. The sauterian_formula is defined in a way that the result is the most consonant interpretation (See degree_of_dissonances for more information). Example: The Chord CEG in C-Dur could be seen as T1,T3,T5,D1,S5, but removing D1 and S5 results in a less dissonant interpretation: T1,T3,T5, while still all pitches are used. For CEGA however, the sauterian_formula would be T1,T3,T5,S3,S5 because removing the S5 would not result in a more consonant interpretation. atonal_pitches is a list of pitches that are not in the key of the harmonic state.
    atonal_pitches is a list of pitches that are not in the key of the harmonic state.
    If a harmonic state of an event has multiple keys, the sauterian formula for this event is not defined and has the value 'ind.' ('indifference') instead.
    If the event has no pitches (a rest), sauterian_formula is '/'.

    Output: String. The degree of dissonance for this event.
    Either "con", "fcon", "low", "mid", "high", "A1", "A2", "A3", "A4" or "A5". Or "ind." or "/". 
    "con": consonance
    "fcon": false consonance
    "low": low dissonance
    "med": medium dissonance
    "high": high dissonance
    "A<n>": atonal with n atonal pitches
    "ind.": indifferent: not atonal, but dissonance grade can't be determined because there are multiple keys in the harmonic state.
    "/": no pitches in this event.

    order of calculation:
    1. atonality
    2. pcset with exactly one pitch -> consonant
    3. indifferent or rest
    4. dissonance_degree.
    -> If the pcset is atonal and the harmonic state is indifferent, it will still be marked as atonal.
    -> a pcset with exactly one pitch is consonant, even in an indifferent harmonic state. (Because it will surely be consonant in every key.)
    """
    pcset = event_analysis[0][0]

    atonality_degree = calc_atonality_degree(pcset)
    if atonality_degree != 0:
        return "A" + str(atonality_degree)

    sauterian_formula = event_analysis[2]
    
    return calc_degree_of_dissonance(sauterian_formula, pcset)


def calc_atonality_degree(pcset):
    """
    Input:
    - pcset: List of ints in range 0-11. The pitchclasses of one event.
    
    Output: Int from 0 to 5. The atonality degree of this pcset.

    0: tonal pcset: the pcset is subset of a key. 
    1: you have to remove at least one pitch to get a tonal pcset.
    2: you have to remove at least two pitches to get a tonal pcset.
    ...
    5: The atonal pcset of all pitches 0-11 simultaneously. This is the most atonal pcset in this model and sounds approbiately terrible.
    """
    pcsets = [pcset]
    n = 0

    if all(x in pcset for x in [0,1,2,3,4,5,6,7,8,9,10,11]): # If the pcset consists of all possible pitches, it is the most atonal pcset and has the most atonal degree 5. There is only this one possibility for an atonal set of 5th degree.
        return 5                                             

    while True:

        for pcset in pcsets:
            for key in list(map(key_to_pcset, all_keys)):
                if all(x in key for x in pcset):
                    return n

        # Build all sublists of each pcset, where exactly one element from pcset was removed.
        # [[0,1,2]] -> [[1,2], [0,2], [0,1]]
        # [[0,1,2], [3,4,5]] -> [[1,2], [0,2], [0,1], [4,5], [3,5], [3,4]]
        pcsets = [[pitch for pitch in pcset if pitch != pitch_to_remove] for pcset in pcsets for pitch_to_remove in pcset]

        n += 1
        if n > 5: # Should be impossible if used like intended.
            raise Exception('Atonal chord with more than 5 atonal tones')


def calc_degree_of_dissonance(sauterian_formula, pcset):
    """
    Input:
    - sauterian_formula: Tuple of two lists: (tonal_result, atonal_pitches).
    tonal_result is a list of 9 booleans in the order: T1, T3, T5, D1, D3, D5, S1, S3, S5. This roughly corresponds to whether the scale degree for each field is used in the event, with exceptions: The scale degree 1 could be seen as T1 or as S5, the scale degree 5 could be seen as T5 or as D1. The sauterian_formula is defined in a way that the result is the most consonant interpretation (See degree_of_dissonances for more information). Example: The Chord CEG in C-Dur could be seen as T1,T3,T5,D1,S5, but removing D1 and S5 results in a less dissonant interpretation: T1,T3,T5, while still all pitches are used. For CEGA however, the sauterian_formula would be T1,T3,T5,S3,S5 because removing the S5 would not result in a more consonant interpretation.
    atonal_pitches is a list of pitches that are not in the key of the harmonic state.
    If a harmonic state of an event has multiple keys, the sauterian formula for this event is not defined and has the value 'ind.' ('indifference') instead.
    If a event has no pitches (a rest), sauterian_formula is '/'.
    - pcset: List of ints in range 0-11. The pitchclasses of one event.
    
    Output: String. The degree of dissonance for this event. Either "con", "fcon", "low", "mid", "high". Or "ind." or "/".

    Calculates the degree of dissonance from the given sauterian formula:
    If the pcset has exactly on element, it is always consonant, even if the harmonic state is indifferent.
    If sauterian_formula is defined. If sauterian_formula is 'ind.' or '/', this value is returned as is.
    Should only be used for tonal events without atonal pitches, because for atonal chords, the degree of dissonance is defined otherwise (see degree_of_dissonance_or_atonal) but it is not forbidden to analyze the tonal part of an atonal chord with this function.
    """
    if len(pcset) == 1:
        return 'con'

    if sauterian_formula == 'ind.' or sauterian_formula == '/':
        return sauterian_formula

    tonal_result = sauterian_formula[0]

    T = tonal_result[0] or tonal_result[1] or tonal_result[2]
    D = tonal_result[3] or tonal_result[4] or tonal_result[5]
    S = tonal_result[6] or tonal_result[7] or tonal_result[8]

    if T + S + D == 1: # T or S or D
        return 'con'
    elif is_consonant(pcset):
        return 'fcon'
    elif T+S+D == 3: # T+S+D
        return 'high'
    elif T: # T+S or T+D
        return 'low'
    else: # S+D
        return 'med'
    

def is_consonant(pcset):
    """
    Input:
    - pcset: List of ints in range 0-11. The pitchclasses of one event.
    
    Output: Boolean. True if the pcset is consonant, False otherwise.

    Calculates if the pcset is consonant:
    For pcsets with three pitchclasses: Only a major or minor chord is consonant.
    For intervals: (Prime, Octave, should not occur in a pcset), Quinte, Quarte, major and minor third, major and minor sixth are consonant, all other intervals are dissonant.
    Single notes are always consonant.
    """
    if len(pcset) == 0:
        return False
    if len(pcset) == 1:
        return True
    if len(pcset) == 2:
        return (pcset[0]-pcset[1]) % 12 in [0, 3, 4, 5, 7, 8, 9] # 0->Prime, 3->k3, 4->g3, 5->r4, 7->r5, 8->k6, 9->g6
    if len(pcset) == 3:
        return (pcset[0]-pcset[1]) % 12 in [0, 3, 4, 5, 7, 8, 9] and (pcset[0]-pcset[2]) % 12 in [0, 3, 4, 5, 7, 8, 9] and (pcset[1]-pcset[2]) % 12 in [0, 3, 4, 5, 7, 8, 9] # Only major or minor chords have this property.
    elif len(pcset) >= 4:
        return False