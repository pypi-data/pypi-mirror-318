from fractions import Fraction

from preprocess import get_line_end_time


def calc_harmonies(voices, note_equal_function = lambda x, y: x == y):
    """
    Input:
    - voices: a list of voices, where each voice is a list of Events, where each Event has a list of pitches and a duration. (All the voices of one line of music)
    
    The representation of a pitch is not specified here. It can be a pc_note, a pac_note, or any other representation of a pitch. ('pc' means pitch class, 'pac' means pitch and accidentals. )
    But for custom representations of pitches you have to provide a note_equal_function:
    - note_equal_function: a function, which takes two pitches and returns True if they are equal, False otherwise.
    The default value for note_equal_function is lambda x, y: x == y, which works for pc_notes and pac_notes.

    pc: Pitches are represented as: Int in range 0-11
    pac: Pitches are represented as: Object (python dictionary) with two fields: 'pitch': Int in range 0-6 (for c,d,e,f,g,a,b), 'acc': String in ['none', 'sharp', 'flat', 'natural', 'dblsharp', 'dblflat'] (the accidental of the pitch)
    The PAC-Representation is useful if the resulting harmonies should be displayed as classical notes (like in abcjs), where enharmonic notes are displayed as different notes.

    Output: Depending on Input-Event-Representation:
    voice of Events: One voice: a list of Events with the same representation as the input events.

    This function gets multiple voices and calculates the resulting harmonies, and the duration of these harmonies.
    Each time a note or rest in one voice starts, a new harmony is created.

    Example:
    Informal notation:
    Voice1: [A,C]2, [G,C]2, [A,C]1
    Voice2: [C]4, [F]2, [E]4, [F]1
    Outputvoice: [A,C]4, [A,C,F]4, [G,C,F]4, [G,C,E]4, [A,C,F]1

    Input in pc-mode: #############################################################################
    - voices: [
        [
            {
                pitches: [9, 0],
                duration: Fraction(1, 2)
            },
            {
                pitches: [7, 0],
                duration: Fraction(1, 2)
            },
            {
                pitches: [9, 0],
                duration: Fraction(1, 1)
            }
        ],
        [
            {
                pitches: [0],
                duration: Fraction(1, 4)
            },
            {
                pitches: [5],
                duration: Fraction(1, 2)
            },
            {
                pitches: [4],
                duration: Fraction(1, 4)
            },
            {
                pitches: [5],
                duration: Fraction(1, 1)
            },
        ]
    ]
    #########################################################
    Output:
    - [
        {
            pitches: [9, 0],
            duration: Fraction(1, 4)
        },
        {
            pitches: [9, 0, 5],
            duration: Fraction(1, 4)
        },
        {
            pitches: [7, 0, 5],
            duration: Fraction(1, 4)
        },
        {
            pitches: [7, 0, 4],
            duration: Fraction(1, 4)
        },
        {
            pitches: [9, 0, 5],
            duration: Fraction(1, 1)
        },
    ]


    Input in pac-mode: #############################################################################
    - voices: [
        [
            {
                pitches: [
                    {
                        pitch: 5,
                        acc: 'none'
                    },
                    {
                        pitch: 0,
                        acc: 'none'
                    }
                ],
                duration: Fraction(1, 2)
            },
            {
                pitches: [
                    {
                        pitch: 4,
                        acc: 'none'
                    },
                    {
                        pitch: 0,
                        acc: 'none'
                    }
                ],
                duration: Fraction(1, 2)
            },
            {
                pitches: [
                    {
                        pitch: 5,
                        acc: 'none'
                    },
                    {
                        pitch: 0,
                        acc: 'none'
                    }
                ],
                duration: Fraction(1, 1)
            }
        ],
        [
            {
                pitches: [
                    {
                        pitch: 0,
                        acc: 'none'
                    }
                ],
                duration: Fraction(1, 4)
            },
            {
                pitches: [
                    {
                        pitch: 3,
                        acc: 'none'
                    }
                ],
                duration: Fraction(1, 2)
            },
            {
                pitches: [
                    {
                        pitch: 2,
                        acc: 'none'
                    }
                ],
                duration: Fraction(1, 4)
            },
            {
                pitches: [
                    {
                        pitch: 3,
                        acc: 'none'
                    }
                ],
                duration: Fraction(1, 1)
            },
        ]
    ]
    #########################################################
    Output:
    - [
        {
            pitches: [
                {
                    pitch: 5,
                    acc: 'none'
                },
                {
                    pitch: 0,
                    acc: 'none'
                }
            ],
            duration: Fraction(1, 4)
        },
        {
            pitches: [
                {
                    pitch: 5,
                    acc: 'none'
                },
                {
                    pitch: 0,
                    acc: 'none'
                },
                {
                    pitch: 3,
                    acc: 'none'
                }
            ],
            duration: Fraction(1, 4)
        },
        {
            pitches: [
                {
                    pitch: 4,
                    acc: 'none'
                },
                {
                    pitch: 0,
                    acc: 'none'
                },
                {
                    pitch: 3,
                    acc: 'none'
                }
            ],
            duration: Fraction(1, 4)
        },
        {
            pitches: [
                {
                    pitch: 4,
                    acc: 'none'
                },
                {
                    pitch: 0,
                    acc: 'none'
                },
                {
                    pitch: 2,
                    acc: 'none'
                }
            ],
            duration: Fraction(1, 4)
        },
        {
            pitches: [
                {
                    pitch: 5,
                    acc: 'none'
                },
                {
                    pitch: 0,
                    acc: 'none'
                },
                {
                    pitch: 3,
                    acc: 'none'
                }
            ],
            duration: Fraction(1, 1)
        },
    ]
    """

    if all(map(lambda voice: len(voice) == 0, voices)):
        return [] 

    current_time = Fraction(0, 1)
    # a voice is a list of Events here, turn it to an dictionary, so we can add more fields to it.
    voices = list(map(lambda voice: {'events': voice}, voices))

    for voice in voices:
        if voice['events']:
            voice['current_event_index'] = 0
            voice['time_of_next_event'] = voice['events'][voice['current_event_index']]['duration']
	
    harmonies = [] # list of harmonies which are resulting by the simutaneous notes of all voices.
	
    end_time = get_line_end_time([voice['events'] for voice in voices]) # This also checks for end_time consistency for each voice in the line. If not all end_times are equal, it throws an exception. 
	
    while True:
		
        time_of_next_event = min(map(lambda voice: voice['time_of_next_event'], voices))
		
        all_pitches_of_all_current_events = [note for voice in voices for note in voice['events'][voice['current_event_index']]['pitches']]
		
        harmonies.append(
            {
                'pitches': remove_duplicates(all_pitches_of_all_current_events, note_equal_function),
                'duration': time_of_next_event - current_time
            }
        )
		
        current_time = time_of_next_event
        if current_time == end_time:
            break
		    
        for voice in voices:
            if voice['time_of_next_event'] == current_time:
                voice['current_event_index'] += 1
                voice['time_of_next_event'] += voice['events'][voice['current_event_index']]['duration']

        
    return harmonies


def remove_duplicates(lst, eq_function):
    """
    Input:
    - lst: a list of elements
    - eq_function: a function, which takes two elements of lst and returns True if they are equal, False otherwise.

    Output: a list of elements, where all duplicates are removed, so that only the first occurence of each element remains.
    """
    return [v1 for i, v1 in enumerate(lst) if not any(eq_function(v1, v2) for v2 in lst[:i])]
