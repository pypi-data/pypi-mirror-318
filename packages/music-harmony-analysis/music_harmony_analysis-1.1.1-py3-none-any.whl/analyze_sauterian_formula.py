from type import key_to_pcset

def analyze_sauterian_formula(analysis):
    """
    Input:
    - analysis: List of tuples: ((pcset, duration), new_harmonic_state), where (pcset, duration) are the musical events from music and new_harmonic_state is the new harmonic state (a list of keys) after this event.

    Output:
    - analysis: List of tuples: ((pcset, duration), new_harmonic_state, sauterian_formula), sauterian_formula is the sauterian formula for this event.

    Adds the sauterian formula for each harmony to the analysis.
    """
    for i in range(len(analysis)):
        analysis[i] = (analysis[i][0], analysis[i][1], sauterian_formula(analysis[i]))
    return analysis


def sauterian_formula(event_analysis):
    """
    Input:
    - event_analysis: ((pcset, duration), harmonic_state), (but duration is not needed here), each pitch in pcset is a int in range 0-11. harmonic_state is a list of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.
    
    Output:
    - sauterian_formula: Tuple of two lists: (tonal_result, atonal_pitches).
    tonal_result is a list of 9 booleans in the order: T1, T3, T5, D1, D3, D5, S1, S3, S5. This roughly corresponds to whether the scale degree for each field is used in the event, with exceptions: The scale degree 1 could be seen as T1 or as S5, the scale degree 5 could be seen as T5 or as D1. The sauterian_formula is defined in a way that the result is the most consonant interpretation (See degree_of_dissonances for more information). Example: The Chord CEG in C-Dur could be seen as T1,T3,T5,D1,S5, but removing D1 and S5 results in a less dissonant interpretation: T1,T3,T5, while still all pitches are used. For CEGA however, the sauterian_formula would be T1,T3,T5,S3,S5 because removing the S5 would not result in a more consonant interpretation.
    atonal_pitches is a list of pitches that are not in the key of the harmonic state.
    If the sauterian formula is not defined for this event, 'ind.' or '/' is returned.
    'ind.' is returned if the harmonic state has multiple keys.
    '/' is returned if the event has no pitches (a rest).

    Calculates the sauterian formula for the given event and harmonic state.
    """
    pitches = event_analysis[0][0]
    harmonic_state = event_analysis[1]

    if len(pitches) == 0: # a rest has no sauterian formula
        return "/"

    if len(harmonic_state) != 1: # sauterian formula is only defined for harmonic_states with a single key.
        return "ind."
    
    
    key_pitches = key_to_pcset(harmonic_state[0])

    used_scale_degrees = list(map(lambda x: x in pitches, key_pitches))
    
    #Return type: List of 9 booleans in the order:
    #T1, T3, T5, D1, D3, D5, S1, S3, S5
    tonal_result = [False for x in range(9)]

    
    tonal_result[1] = used_scale_degrees[2] #T3
    
    tonal_result[4] = used_scale_degrees[6] #D3
    tonal_result[5] = used_scale_degrees[1] #D5
    
    tonal_result[6] = used_scale_degrees[3] #S1
    tonal_result[7] = used_scale_degrees[5] #S3

    T = tonal_result[1]
    D = tonal_result[4] or tonal_result[5]
    S = tonal_result[6] or tonal_result[7]
    
    #If !S and !D or T:
    #   T1,T5
    #Elif S and D:
    #Elif !D: #S, aber nicht D
    #   T5
    #   Wenn T5:
    #     T1
    #Else: #D, aber nicht S
    #   T1
    #   Wenn T1:
    #      T5
    #
    #If D:
    #   D1
    #If S:
    #   S5

    if not S and not D or T:
        tonal_result[0] = used_scale_degrees[0]
        tonal_result[2] = used_scale_degrees[4]
    elif S and D:
        pass
    elif not D: #S, aber nicht D
        tonal_result[2] = used_scale_degrees[4]
        if tonal_result[2]:
            tonal_result[0] = used_scale_degrees[0]
    else: #D, aber nicht S
        tonal_result[0] = used_scale_degrees[0]
        if tonal_result[0]:
            tonal_result[2] = used_scale_degrees[4]
    
    if D:
        tonal_result[3] = used_scale_degrees[4]
    if S:
        tonal_result[8] = used_scale_degrees[0]

    

    atonal_pitches = [pitch for pitch in pitches if pitch not in key_pitches]

    return (tonal_result, atonal_pitches)