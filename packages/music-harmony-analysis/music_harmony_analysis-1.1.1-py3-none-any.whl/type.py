from typing import List, Tuple
from fractions import Fraction

def powerset(lst: List) -> List[List]:
    if not lst:
        return [[]]
    ps = powerset(lst[1:])
    return ps + [x + [lst[0]] for x in ps]

PC = int
all_PCs: List[PC] = list(range(12))

PCSet = List[PC]

Key = Tuple[PC, str]
all_keys: List[Key] = [(n, mode) for n in range(12) for mode in ['dur', 'moll']]

HarmonicState = List[Key]
#all_harmonic_states: List[HarmonicState] = [hs for hs in powerset(all_keys) if len(hs) < 15] # This takes waaaaay to long

HarmonicEvent = Tuple[PCSet, Fraction]
Music = List[HarmonicEvent]
HarmonicAnalysis = List[Tuple[HarmonicEvent, HarmonicState]]

dur = [0, 2, 4, 5, 7, 9, 11]
moll = [0, 2, 3, 5, 7, 8, 11]

def show_key(key: Key) -> str:
    """
    Input:
    - key: tupel with two fields: pitchclass: int from 0-11 and mode: 'dur' or 'moll'

    Output:
    The Key as a string in the format 'C' for dur and 'Am' for moll. Fis and Es are used for sharp and flat keys.
    Bb is used for pitchclass 10, B for pitchclass 11.
    
    Example:
    (0, 'dur') -> 'C'
    (1, 'dur') -> 'Cis'
    (1, 'moll') -> 'Cism'
    (11, 'moll') -> 'Bm'
    (10, 'dur') -> 'Bb'
    """
    n, mode = key
    notes = ['C', 'Cis', 'D', 'Es', 'E', 'F', 'Fis', 'G', 'As', 'A', 'Bb', 'B']
    return notes[n] + ('' if mode == 'dur' else 'm')

def show_harmonic_state(keys: HarmonicState) -> str:
    if not keys:
        return "[]"
    if set(keys) == set(all_keys):
        return '[All]'
    return "[" + ", ".join([show_key(key) for key in keys]) + "]"

def show_harmonic_states(states: List[HarmonicState]) -> str:
    return "".join([show_harmonic_state(state) for state in states])

def parse_key(key_str: str) -> tuple:
    """
    Parses a string representation of a Key into a tuple (pitchclass, mode).

    Input:
    - key_str: A string in the format 'C', 'Cis', 'Am', 'Bm', 'Bb', etc.

    Output:
    - A tuple (pitchclass, mode), where:
      - pitchclass: int (0-11) representing the pitch class
      - mode: str, either 'dur' for major or 'moll' for minor

    Example:
    - 'C' -> (0, 'dur')
    - 'Cis' -> (1, 'dur')
    - 'Cism' -> (1, 'moll')
    - 'Bb' -> (10, 'dur')
    - 'Bm' -> (11, 'moll')
    """
    notes = ['C', 'Cis', 'D', 'Es', 'E', 'F', 'Fis', 'G', 'As', 'A', 'Bb', 'B']
    if key_str.endswith('m'):  # Minor key
        note_str = key_str[:-1]
        mode = 'moll'
    else:  # Major key
        note_str = key_str
        mode = 'dur'
    
    pitchclass = notes.index(note_str)
    return (pitchclass, mode)

def parse_harmonic_state(state_str: str) -> list:
    """
    Parses a string representation of a HarmonicState into a list of Keys.

    Input:
    - state_str: A string in one of the following formats:
      - '[]' for an empty state
      - '[All]' for a state containing all keys
      - '[C, Cis, Am, Bb]' for specific keys

    Output:
    - A list of Keys (tuples), where each Key is (pitchclass, mode).

    Example:
    - '[]' -> []
    - '[All]' -> all_keys
    - '[C, Am, Bb]' -> [(0, 'dur'), (9, 'moll'), (10, 'dur')]
    """
    if state_str == '[]':
        return []
    if state_str == '[All]':
        return list(all_keys)
    
    # Remove brackets and split the string into individual keys
    key_strings = state_str[1:-1].split(', ')
    return [parse_key(key_str) for key_str in key_strings]

def key_to_pcset(key: Key) -> PCSet:
    n, mode = key
    return transpose(n, dur) if mode == 'dur' else transpose(n, moll)

def show_harmonic_analysis(analysis: HarmonicAnalysis) -> str:
    return "\n".join([f"{pcset} {duration} {keys}" for (pcset, duration), keys in analysis])


def transpose(n: int, pcset: PCSet) -> PCSet:
    return [(pc + n) % 12 for pc in pcset]
