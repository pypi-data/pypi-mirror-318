from duration import voice_duration
from type import show_key, all_keys
from representation import pacset_equal


def analysis_to_abc_strings(analysis, harmony_lines, mode='pac', custom_pitch_to_abc_method=None):
    """
    Input:
    - analysis: List of tuples: (event, harmonic_state, sauterian_formula, degree_of_dissonance_or_atonal).
    event is a tuple of a pcset and a duration. pcset is a list of ints from 0-11.
    harmonic_state is a list of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.
    sauterian_formula is a string ('ind.' if there is not exactly one key, '/' if the event is a rest) or a tuple of two lists: (tonal_result, atonal_pitches).
    tonal_result is a list of 9 booleans in the order: T1, T3, T5, D1, D3, D5, S1, S3, S5. This roughly corresponds to whether the scale degree for each field is used in the event, with exceptions: The scale degree 1 could be seen as T1 or as S5, the scale degree 5 could be seen as T5 or as D1. The sauterian_formula is defined in a way that the result is the most consonant interpretation (See degree_of_dissonances for more information). Example: The Chord CEG in C-Dur could be seen as T1,T3,T5,D1,S5, but removing D1 and S5 results in a less dissonant interpretation: T1,T3,T5, while still all pitches are used. For CEGA however, the sauterian_formula would be T1,T3,T5,S3,S5 because removing the S5 would not result in a more consonant interpretation.
    atonal_pitches is a list of pitches that are not in the key of the harmonic state.
    degree_of_dissonance_or_atonal is a string: 'con', 'fcon', 'low', 'mid', 'high', 'A1', 'A2', 'A3', 'A4', 'A5', 'indiff.' or '/'.

    - harmony_lines: List of lines/voices (exactly one voice per line), where each voice is a list of events. Each event has a 'pitches' and a 'duration' field.
    The events in analysis have to be the same as the events in harmony_lines, only with a different representation. The events in analysis are replaced by the events in harmony_lines in to_abc_strings_preprocess. 
    - mode: 'pc', 'pac' or 'custom'. See event_to_abc_string for more information.
    - custom_pitch_to_abc_method: function. Maps a pitch representation to a string. Needed if mode is 'custom'.

    Output:
    - analysis_abc_strings: Dictionary with the following fields:
    - header: String. The header of the abc analysis: '\nL:1\n'.
    - events: List of strings. Format: '[V: Analysis] [CE^^G]1/4 [C_EGB]1/4\n'. ('[V: Analysis name=Analysis snm=A.]' for the first line) Each string represents the harmonies of one line of music.
    - harmonic_states: List of strings. Format: 'w: [C,Cis,Dm] [C,Cis,Dm]\n'. Each string corresponds to the events of one line.
    - sauterian_formula: List of strings. Format: 'w: T15D15S3 D35S1A3,11\n'. Each string corresponds to the events of one line.
    - degree_of_dissonance_or_atonal: List of strings. Format: 'w: / low\n'. Each string corresponds to the events of one line. 

    Example:
    analysis = [
        (
            ([0, 2, 4], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            'T15D15S3',
            'high'
        ),
        (
            ([0, 2, 4], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')]
            '/',
            '/'
        ),
        (
            ([0, 2, 4], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')]
            'ind.',
            'ind.'
        ),
        (
            ([0, 2, 4], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')]
            'T15S3A0,11,4',
            'A3'
        )
    ]
    harmony_lines = [
        [
            {'pitches': [0, 2, 4], 'duration': Fraction(1, 4)},
            {'pitches': [0, 2, 4], 'duration': Fraction(1, 4)},
        ],
        [
            {'pitches': [0, 2, 4], 'duration': Fraction(1, 4)},
            {'pitches': [0, 2, 4], 'duration': Fraction(1, 4)},
        ]
    ]
    ->
    {
        "header": "\nL:1\n",
        "events": [
            "[V: Analysis name=Analysis snm=A.] [CEG]1/4 [CEG]1/4\n",
            "[V: Analysis] [CEG]1/4 [CEG]1/4\n"
        ],
        "harmonic_states": [
            "w: [C,Cis,Dm]~ *\n",
            "w: [C,Cis,Dm]~ *\n"
        ],
        "sauterian_formula": [
            "w: T15D15S3~ /\n",
            "w: ind.~ T15S3A0,11,4\n"
        ],
        "degree_of_dissonance_or_atonal": [
            "w: high~ /\n",
            "w: ind.~ A3\n"
        ]
    }
    """
    analysis_lines = to_abc_strings_preprocess(analysis, harmony_lines)

    analysis_abc_strings = {
    	"header": "\nL:1\nK:none\n",
    	"events": [],
    	"harmonic_states": [],
    	"sauterian_formula": [],
    	"degree_of_dissonance_or_atonal": []
    }
    
    first_line = True

    for line in analysis_lines:
    
        if first_line:
            first_line = False
            event_string = '[V: Analysis name=Analysis snm=A.] '
        else:
            event_string = '[V: Analysis] '
        harmonic_states_string = 'w: '
        sauterian_formula_string = 'w: '
        degree_of_dissonance_or_atonal_string = 'w: '
        
        old_harmonic_state = []
        old_pcset = [-1]
        is_new_pcset = True

        for x in line: # x = (event, harmonic_state, sauterian_formula, degree_of_dissonance_or_atonal)
            is_new_pcset = not pacset_equal(x[0]['pitches'], old_pcset)

            event_string += event_to_abc_string(x[0], mode, custom_pitch_to_abc_method) + ' '
            harmonic_states_string += harmonic_state_to_abc_string(x[1], old_harmonic_state)
            old_harmonic_state = x[1]

            sauterian_formula_string += sauterian_formula_to_abc_string(x[2]) + '~ ' if is_new_pcset else '_'
            degree_of_dissonance_or_atonal_string += x[3] + '~ ' if is_new_pcset else '_'
            old_pcset = x[0]['pitches']
        
        event_string = event_string[0:-1] + '\n'
        harmonic_states_string = harmonic_states_string[0:-2] + '\n' if harmonic_states_string[-2] == '~' else harmonic_states_string + '\n'
        sauterian_formula_string = sauterian_formula_string[0:-2] + '\n' if sauterian_formula_string[-2] == '~' else sauterian_formula_string + '\n'
        degree_of_dissonance_or_atonal_string = degree_of_dissonance_or_atonal_string[0:-2] + '\n' if degree_of_dissonance_or_atonal_string[-2] == '~' else degree_of_dissonance_or_atonal_string + '\n'
    
        analysis_abc_strings["events"].append(event_string)
        analysis_abc_strings["harmonic_states"].append(harmonic_states_string)
        analysis_abc_strings["sauterian_formula"].append(sauterian_formula_string)
        analysis_abc_strings["degree_of_dissonance_or_atonal"].append(degree_of_dissonance_or_atonal_string)
    
    return analysis_abc_strings


def to_abc_strings_preprocess(analysis, harmony_lines):
    """
    Input:
    - analysis: List of tuples: (event, harmonic_state, sauterian_formula, degree_of_dissonance_or_atonal).
    event is a tuple of a pcset and a duration. pcset is a list of ints from 0-11.
    - harmony_lines: List of lines/voices (exactly one voice per line), where each voice is a list of events. Each event has a 'pitches' and a 'duration' field.

    Output:
    - analysis_lines: List of lines/voices (exactly one voice per line), where each voice is a list of tuples (event, keys, sauterian_formula, degree_of_dissonance_or_atonal). See Input.

    Splits the analysis into lines by comparing the durations of the analysis with the duration of each line, those durations are calculated from the harmony_lines.
    Also the events in analysis are replaced by the events in harmony_lines.
    """
    line_durations = list(map(voice_duration, harmony_lines))

    analysis_lines = []
    current_line = []
    current_line_duration = 0
    current_line_index = 0

    current_harmony_lines_index = 0

    i = 0
    while True:

        if current_line_index < len(line_durations) and current_line_duration == line_durations[current_line_index]:
            analysis_lines.append(current_line)
            current_line = []
            current_line_duration = 0
            current_line_index += 1
            current_harmony_lines_index = 0
            continue

        if i == len(analysis):
            break

        event, harmonic_state, sauterian_formula, degree_of_dissonance_or_atonal = analysis[i]
        current_line.append((harmony_lines[current_line_index][current_harmony_lines_index], harmonic_state, sauterian_formula, degree_of_dissonance_or_atonal))
        current_line_duration += event[1]
        current_harmony_lines_index += 1
        
        if current_line_duration > line_durations[current_line_index]:
            raise Exception("Analysis event lengths don't match line lengths.")
        
        i += 1

    if not len(line_durations) == len(analysis_lines) or current_line != []:
        raise Exception("Analysis event lengths don't match line lengths.")
    
    return analysis_lines


def event_to_abc_string(event, mode='pac', custom_pitch_to_abc_method=None):
    """
    - event has a 'pitches' and a 'duration' field.
    a pitch in pitches can have different representations, depending on the
    - mode:
    'pc': int from 0-11
    'pac': dict with two fields: pitch (int from 0-6) and acc (string)
    custom: any representation you want. Just define a function that maps your representation to a string:
    - custom_pitch_to_abc_method: function. Maps a pitch representation to a string.

    Output:
    - abc_string: String. The event in abc notation.

    Example:
    {'pitches': [0, 2, 4], 'duration': Fraction(1, 4)} -> [CEG]1/4
    {'pitches': [{'pitch': 0, 'acc': 'none'}, {'pitch': 2, 'acc': 'flat'}, {'pitch': 4, 'acc': 'dblsharp'}], 'duration': Fraction(1, 4)} -> [C_E^^G]1/4
    """
    string = '['
    for pitch in event['pitches']:
        if mode == 'pc':
            string += pc_to_abc(pitch)
        elif mode == 'pac':
            string += pac_to_abc(pitch)
        else:
            string += custom_pitch_to_abc_method(pitch)
    string += ']'
    string += duration_to_abc(event['duration'])
    return string

def pc_to_abc(pitch):
    if pitch == 0: return 'C'
    elif pitch == 1: return '^C'
    elif pitch == 2: return 'D'
    elif pitch == 3: return '_E'
    elif pitch == 4: return 'E'
    elif pitch == 5: return 'F'
    elif pitch == 6: return '^F'
    elif pitch == 7: return 'G'
    elif pitch == 8: return '^G'
    elif pitch == 9: return 'A'
    elif pitch == 10: return '_B'
    elif pitch == 11: return 'B'
    else: raise Exception("Unexpected pitch value: " + pitch)
	
def pac_to_abc(pitch):
    """
    Input:
    - pitch: Int. A pitch in pac notation. It has a 'pitch' (int from 0-6) and an 'acc' field (string).

    Output:
    - abc_string: String. The pitch in abc notation.

    Example:
    {pitch: 2, acc: 'none'} -> E
    {pitch: 0, acc: 'flat'} -> _C
    {pitch: 0, acc: 'dblflat'} -> __C
    {pitch: 3, acc: 'dblsharp'} -> ^^F
    {pitch: 5, acc: 'sharp'} -> ^A
    {pitch: 6, acc: 'natural'} -> =B
    """
    string = ''

    if pitch['acc'] == 'none': string += ''
    elif pitch['acc'] == 'sharp': string += '^'
    elif pitch['acc'] == 'dblsharp': string += '^^'
    elif pitch['acc'] == 'flat': string += '_'
    elif pitch['acc'] == 'dblflat': string += '__'
    elif pitch['acc'] == 'natural': string += '='
    else:
        raise Exception("Unexpected accidental value: " + pitch['acc'])
    
    if pitch['pitch'] == 0: string += 'C'
    elif pitch['pitch'] == 1: string += 'D'
    elif pitch['pitch'] == 2: string += 'E'
    elif pitch['pitch'] == 3: string += 'F'
    elif pitch['pitch'] == 4: string += 'G'
    elif pitch['pitch'] == 5: string += 'A'
    elif pitch['pitch'] == 6: string += 'B'
    else:
        raise Exception("Unexpected pitch value: " + pitch['pitch'])
    
    return string

def duration_to_abc(duration):
    """
    Input:
    - duration: Fraction. The duration of a note.

    Output:
    The duration as a string in the format 'num/den'. abcjs handles this very good: It shows all 'normal' durations (1/1,1/2,1/4,1/8 etc. and possibly up to eigth points, no ntoles) in the expected way, and all other lengths like ntoles or very small values that can occur are shown approximated by the nearest normal note length, but internally the given length will be used, so that the alignment of the notes will be still right. For the use case of the program this is more than enough.
    """
    return str(duration.numerator) + '/' + str(duration.denominator)


def harmonic_state_to_abc_string(harmonic_state, old_harmonic_state):
    """
    Input:
    - harmonic_state: List of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.
    - old_harmonic_state: List of keys: (pitchclass, mode).
    
    Output:
    '_', if the harmonic state is the same as the old harmonic state.
    '[All]' if the harmonic state is the state containing all 24 keys.
    Else:
    The harmonic_state as a string in the format '[key1,key2,key3,...]~ '.
    
    Example:
    [(0, 'dur'), (1, 'dur'), (2, 'moll')], [] -> '[C,Cis,Dm]~ '
    [(11, 'dur'), (10, 'moll')], [] -> '[B,Bbm]~ '
    [(0, 'dur'), (1, 'dur'), (2, 'moll')], [(1, 'dur'), (0, 'dur'), (2, 'moll')] -> '_'
    """
    if set(harmonic_state) == set(old_harmonic_state):
        return '_'
    
    string = '['
    for key in harmonic_state:
        string += show_key(key) + ','
    string = string[0:-1]
    string += ']~ '
    return string


def sauterian_formula_to_abc_string(sauterian_formula):
    """
    Input:
    - sauterian_formula: String or (Tuple of two lists: (tonal_result, atonal_pitches)).
    tonal_result is a list of 9 booleans in the order: T1, T3, T5, D1, D3, D5, S1, S3, S5. This roughly corresponds to whether the scale degree for each field is used in the event, with exceptions: The scale degree 1 could be seen as T1 or as S5, the scale degree 5 could be seen as T5 or as D1. The sauterian_formula is defined in a way that the result is the most consonant interpretation (See degree_of_dissonances for more information). Example: The Chord CEG in C-Dur could be seen as T1,T3,T5,D1,S5, but removing D1 and S5 results in a less dissonant interpretation: T1,T3,T5, while still all pitches are used. For CEGA however, the sauterian_formula would be T1,T3,T5,S3,S5 because removing the S5 would not result in a more consonant interpretation.
    atonal_pitches is a list of pitches that are not in the key of the harmonic state.

    Output:
    The sauterian_formula as a string in the format T135D135S135A<pcs of the atonal notes> or ind. or /.
    If the sauterian formula is 'ind.' or '/' for this event, this string is returned.

    Example:
    ([True, False, True, True, False, True, False, True, False], []) -> 'T15D15S3'
    ([True, False, True, False, False, False, False, False, False], [0, 2, 4]) -> 'T15A0,2,4'
    """
    if type(sauterian_formula) == str:
        return sauterian_formula
    else:
        tonal_result, atonal_pitches = sauterian_formula
        string = ''
        if tonal_result[0] or tonal_result[1] or tonal_result[2]: string += 'T'
        if tonal_result[0]: string += '1'
        if tonal_result[1]: string += '3'
        if tonal_result[2]: string += '5'
        if tonal_result[3] or tonal_result[4] or tonal_result[5]: string += 'D'
        if tonal_result[3]: string += '1'
        if tonal_result[4]: string += '3'
        if tonal_result[5]: string += '5'
        if tonal_result[6] or tonal_result[7] or tonal_result[8]: string += 'S'
        if tonal_result[6]: string += '1'
        if tonal_result[7]: string += '3'
        if tonal_result[8]: string += '5'
        if atonal_pitches: string += 'A' + ','.join(map(str, atonal_pitches))
        return string


def show_analysis_abc_strings(analysis_abc_strings):
    """
    Input:
    - analysis_abc_strings: Dictionary with the following fields:
    - header: String. The header of the abc analysis: '\nL:1\n'.
    - events: List of strings. Format: '[V: Analysis] [CE^^G]1/4 [C_EGB]1/4\n'. Each string represents the harmonies of one line of music.
    - harmonic_states: List of strings. Format: 'w: [C,Cis,Dm] [C,Cis,Dm]\n'. Each string corresponds to the events of one line.
    - sauterian_formula: List of strings. Format: 'w: T15D15S3 D35S1A3,11\n'. Each string corresponds to the events of one line.
    - degree_of_dissonance_or_atonal: List of strings. Format: 'w: / low\n'. Each string corresponds to the events of one line. 

    Output:
    - analysis_abc_string_representation: String. A formatted string of the analysis_abc_strings dictionary for better readability
    """
    analysis_abc_string_representation = '{\n'
    analysis_abc_string_representation += '    "header": "' + analysis_abc_strings['header'] + '",\n'
    analysis_abc_string_representation += '    "events": [\n'
    for event in analysis_abc_strings['events']:
        analysis_abc_string_representation += '        "' + event + '",\n'
    analysis_abc_string_representation = analysis_abc_string_representation[0:-2] + '\n'
    analysis_abc_string_representation += '    ],\n'
    analysis_abc_string_representation += '    "harmonic_states": [\n'
    for harmonic_state in analysis_abc_strings['harmonic_states']:
        analysis_abc_string_representation += '        "' + harmonic_state + '",\n'
    analysis_abc_string_representation = analysis_abc_string_representation[0:-2] + '\n'
    analysis_abc_string_representation += '    ],\n'
    analysis_abc_string_representation += '    "sauterian_formula": [\n'
    for sauterian_formula in analysis_abc_strings['sauterian_formula']:
        analysis_abc_string_representation += '        "' + sauterian_formula + '",\n'
    analysis_abc_string_representation = analysis_abc_string_representation[0:-2] + '\n'
    analysis_abc_string_representation += '    ],\n'
    analysis_abc_string_representation += '    "degree_of_dissonance_or_atonal": [\n'
    for degree_of_dissonance_or_atonal in analysis_abc_strings['degree_of_dissonance_or_atonal']:
        analysis_abc_string_representation += '        "' + degree_of_dissonance_or_atonal + '",\n'
    analysis_abc_string_representation = analysis_abc_string_representation[0:-2] + '\n'
    analysis_abc_string_representation += '    ]\n'
    analysis_abc_string_representation += '}'
    return analysis_abc_string_representation
