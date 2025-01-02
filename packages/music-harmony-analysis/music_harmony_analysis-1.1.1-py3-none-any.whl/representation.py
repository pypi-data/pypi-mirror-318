
"""
A musical "Event" is defined here as an object with pitches and a musical duration. This can model a note (one object in the pitches list), a chord (multiple pitches) and a rest (empty pitches list), each with a specified length.
It is implemented as a dict with the following keys:
    - pitches: a list of representations of a pitch. pac_notes or pc_notes for example (see below). 
    - duration: Fraction
	
There are different ways to represent a pitch:
    pc_pitch: Pitches are represented as: Int in range 0-11. This is a simple pitch class representation, where enharmonic notes are represented by the same number.
    pac_pitch: Pitches are represented as: Object (python dictionary) with two fields: 'pitch': Int in range 0-6 (for c,d,e,f,g,a,b), 'acc': String in ['none', 'sharp', 'flat', 'natural', 'dblsharp', 'dblflat'] (the accidental of the pitch)
    The PAC-Representation is useful if the resulting harmonies should be displayed as classical notes (like in abcjs), where enharmonic notes are displayed as different notes.


PAC-Repräsentation eines Events:
{
	pitches: [
		{
			pitch: [0-6],
			acc: ['none', 'sharp', 'flat', 'natural', 'dblsharp', 'dblflat']
		}
	],
	duration: Fraction
}

PC-Repräsentation eines Events:
{
   pitches: [0-11],
   duration: Fraction
}
"""
#################

def abcjs_to_pac_events(voice):
    return list(filter(lambda y: y == None, map(lambda x: abcjs_to_pac_event(x), voice)))

def abcjs_to_pac_event(x):
        if x['el_type'] == 'note':
            return {
                'pitches': abcjs_to_pac_pitches(x['pitches']),
                'duration': x['duration']
            }
        else:
             return None

def abcjs_to_pac_pitches(pitches):
	for p in pitches:
		# p is an object with the fields 'accidental', 'name', 'pitch', ...
		p = {
			'pitch': abcjs_name_to_pac_pitch(p['name']),
			'acc': p['accidental'] if 'accidental' in p else 'none' 
		}

def abcjs_name_to_pac_pitch(name):
    """
    - name: String. This String is the name attribute of a note in the abcjs representation. It is a string like "c", "D", "E,,", "f''", "^c,"
    So: octavespecifiers, lowercase and Uppercase, accidentals...

    Output: Int. The equivalent pac_note_pitch value to the note name, accidentals are ignored.
    cC -> 0
    dD -> 1
    eE -> 2
    fF -> 3
    gG -> 4
    aA -> 5
    bB -> 6
    """
    if 'c' in name or 'C' in name: return 0
    elif 'd' in name or 'D' in name: return 1
    elif 'e' in name or 'E' in name: return 2
    elif 'f' in name or 'F' in name: return 3
    elif 'g' in name or 'G' in name: return 4
    elif 'a' in name or 'A' in name: return 5
    elif 'b' in name or 'B' in name: return 6
    else: raise Exception("Unexpected note name: " + name)


def pcset_equal(pcset1, pcset2):
    """Returns True if pcset1 and pcset2 are equal, False otherwise.
    pcset1 and pcset2 are lists of pitch classes, e.g. [0, 4, 7]"""
    return sorted(pcset1) == sorted(pcset2)


def pacset_equal(pacset1, pacset2):
    """Returns True if pacset1 and pacset2 have the same elements, False otherwise.
    pacset1 and pacset2 are lists of pac pitches, e.g. [{'pitch': 4,'acc': 'none'},{'pitch': 0,'acc': 'none'},{'pitch': 3,'acc': 'none'}]"""
    if len(pacset1) != len(pacset2):
        return False
    for pac_note in pacset1:
        if pac_note not in pacset2:
            return False
    return True


def pac_to_pc(pac):
    """
    Input: Event in PAC-Representation
    Output: The equivalent Event in PC-Representation

    Calculates the actual PCs in the event from the information of the PAC-Event, which has 7 pitch values for CDEFGAB and maybe accidentals.

    PAC-Event: {
    	pitches: [
    		{
    			pitch: [int],
    			acc: ['none', 'sharp', 'flat', 'natural', 'dblsharp', 'dblflat']
    		}
    	],
    	duration: Fractal
    }

    PC-Event: {
        pitches: [0-11],
        duration: Fraction
    }

    """
    return {
        'pitches': list(set(map(pac_note_to_pc, pac['pitches']))),
        'duration': pac['duration']
    }

def pac_note_to_pc(pac_note) -> int:
    """
    Input:
    - pac_note. a single note in pac-representation
    Output:	Int. (In range 0-11) The equivalent PC value to the pac_note_pitch + accidental value.

    Examples:
    {pitch: 4, acc: ['none']} -> 7
    {pitch: 0, acc: ['flat']} -> 11
    {pitch: 0, acc: ['dblflat']} -> 10
    {pitch: 6, acc: ['dblsharp']} -> 1
    {pitch: 5, acc: ['sharp']} -> 10
    """
	
    pac_note_pitch = pac_note['pitch'] % 7 
	
    if pac_note_pitch == 0: pc = 0
    elif pac_note_pitch == 1: pc = 2
    elif pac_note_pitch == 2: pc = 4
    elif pac_note_pitch == 3: pc = 5
    elif pac_note_pitch == 4: pc = 7
    elif pac_note_pitch == 5: pc = 9
    elif pac_note_pitch == 6: pc = 11
    else: raise Exception("Unexpected pac_note pitch value: " + pac_note_pitch)

    acc_value = get_acc_value(pac_note['acc'])
	
    return (pc + acc_value) % 12
	
def get_acc_value(acc_string) -> int:
    """
    Input:
    - acc_string: String. Either 'none', 'sharp', 'flat', 'natural', 'dblsharp' or 'dblflat'
    Output: Int. The change in pitchclass made by this accidental:
    'none': 0
    'sharp': 1
    'flat': -1
    'dblsharp': 2
    'dblflat': -2
    """
    if acc_string == 'none': return 0
    elif acc_string == 'sharp': return 1
    elif acc_string == 'flat': return -1
    elif acc_string == 'natural': return 0
    elif acc_string == 'dblsharp': return 2
    elif acc_string == 'dblflat': return -2
    else: raise Exception("Unexpected accidental string: " + acc_string)


def preprocessed_lines_to_string(lines):
    """
    Input: List of lines. A line is a list of voices. A voice is a list of events. An event is a dict with the keys 'pitches' and 'duration'.
    Output: String. The string representation of the lines.
    """
    return '[\n' + '\n'.join(map(lambda line: preprocessed_line_to_string(line), lines)) + '\n]'


def preprocessed_line_to_string(line):
    """
    Input: List of voices. A voice is a list of events. An event is a dict with the keys 'pitches' and 'duration'.
    Output: String. The string representation of the line.
    """
    return '\t[\n' + '\n'.join(map(lambda voice: preprocessed_voice_to_string(voice), line)) + '\n\t]'


def preprocessed_voice_to_string(voice):
    """
    Input: List of events. An event is a dict with the keys 'pitches' and 'duration'.
    Output: String. The string representation of the voice.
    """
    return '\t\t[\n' + ',\n'.join(map(lambda event: preprocessed_event_to_string(event), voice)) + '\n\t\t]'


def preprocessed_event_to_string(event):
    """
    Input: Event. An event is a dict with the keys 'pitches' and 'duration'.
    Output: String. The string representation of the event.
    """
    return '\t\t\t' + str(event)


def to_analyze_representation(music, event_to_pc_function = pac_to_pc):
    """
    Input:
    - music: A voice. A voice is a list of events. An event is a dict with the keys 'pitches' and 'duration'.
    - event_to_pc_function: A function that takes an event and returns the pc representation of the event. Default is pac_to_pc.

    Output:
    - A voice in the representation that the analyze module expects: A list of tuples (pcset, duration). pcset is a list of ints, duration is a Fraction.
    """
    pc_list = list(map(event_to_pc_function, music))

    return list(map(lambda pc_event: (pc_event['pitches'], pc_event['duration']), pc_list))