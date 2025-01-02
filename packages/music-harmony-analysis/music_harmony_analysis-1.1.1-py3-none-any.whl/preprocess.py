import itertools
from fractions import Fraction
import copy

from representation import abcjs_name_to_pac_pitch
from duration import durations_to_fractions, meter_to_fraction


def preprocess(lines):
	"""
	Input:
	- lines: [
		{
			staff: [Notenzeile]
		}
	]. Dieses Objekt ist Rückgabewert von der renderABC()-Methode aus der abcjs-Bibliothek, welches noch von einer Javascript-Funktion reduziert wurde. 
	
	Output: [[[PAC-Event]]]. Eine Liste von lines. Mit je einer Liste von voices. Eine voice besteht aus einer Liste von PAC-Events (see representation.py). Die Besonderheit bei PAC-Events ist, dass sie nicht enharmonisch verwechseln, da sie Note und Vorzeichen speichern.
    
	Nimmt das (von abcjs zurückgegebene) lines-Objekt und
	1. weist alle Vorzeichen und Versetzungszeichen jeder betroffenen Note zu. Wenn zu Anfang (erste line) im ersten staff in der ersten voice innerhalb der Länge eines Taktes (durch M: Attribut in abc optional definiert) ein Taktstrich vorkommt, gelten Versetzungszeichen immer für einen ganzen Takt, d.h. bis zum nächsten Taktstrich. Wenn nicht, gelten Versetzungszeichen immer nur für eine Note.
	2. weist jeder Note ihre Duration (zeitliche Länge) zu, welche von Float in ein Fraction-Objekt umgewandelt wird. Auch bei ntolen wird die tatsächliche zeitliche Länge berechnet.
	3. wandelt Pausen in Notenevents (mit leerer pitches list) um.
	"""

	informations = [] # TODO: give information about acc mode in warnings.
	
	acc_mode = determine_mode(lines) # either 'single' or 'bar"
	informations.append('The accidental_mode is "bar". Accidentals of a note in a bar now apply for all notes with the same octave_pitch after the note in the bar. The given key accidentals are applied, if there is no accidental in the bar for this pitch.') if acc_mode == 'bar' else informations.append('The accidental_mode is "single". Accidentals of a note apply only for a single note.')
	
	meter = None
	is_compound = None
	
	for i, line in enumerate(lines): # ab hier das Äquivalent zur handle_line-Methode
		
		new_meter, new_is_compound = get_meter(line)
		if new_meter != None:
			meter = new_meter
			is_compound = new_is_compound
			
		staff_list = line['staff']
		for j, staff in enumerate(staff_list): # ab hier das Äquivalent zur handle_staff-Methode

			voices = staff['voices']
			accidentals = get_accidentals(staff)

			voices, barlines_with_time = voices_to_poac_and_bar_lines(voices, is_compound)

			if acc_mode == 'single':
				for voice in voices:
					voice = add_key_accidentals(voice, accidentals)
			elif acc_mode == 'bar':
				barlines_with_time = remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter)
				voices = accidental_resolution(voices, accidentals, barlines_with_time)
	
			staff_list[j] = voices
		lines[i] = list(itertools.chain(*staff_list))

	return lines, informations


def add_key_accidentals(voice, accidentals):
	"""
	Input:
	- voice: List of poac-events: {'pitches': [{'pitch': 0-6, 'octave_pitch': int, 'acc': ''}, ...], 'duration': Fraction}
	- accidentals: List of objects, each with a 'pitch' field (0-6) and a 'acc' field (sharp, flat, natural, none, ...)
	
	Output:
	- pac-voice: List of pac-events. pac-events have a 'pitches' and a 'duration' field. A pitch consists of a 'pitch' and an 'acc' field. The acc field can be sharp, flat, natural, dblsharp, dblflat or none.
	
	Weist jeder Note in jedem event in voice Vorzeichen aus accidentals zu, wenn der pitch der Note gleich einem pitch aus accidentals ist und 'acc' bei dem pitch in der Note bisher 'none' ist. 
	"""	
	for event in voice:
		for pitch in event['pitches']:
			del pitch['octave_pitch'] # octave_pitch wird nur für den 'bar'-mode (with accidental_resolution()) gebraucht, hier im 'single'-mode nicht.
			for acc in accidentals:
				if pitch['pitch'] == acc['pitch'] and pitch['acc'] == 'none':
					pitch['acc'] = acc['acc']
	return voice


def accidental_resolution(voices, accidentals, barlines_with_time):
	"""
	Input:
	- voices: List of voices, where each voice is a list of poac-events: {'pitches': [{'pitch': 0-6, 'octave_pitch': int, 'acc': ''}, ...], 'duration': Fraction}
	- accidentals: List of objects, each with a 'pitch' field (0-6) and a 'acc' field (sharp, flat, natural, none, ...)
	- barlines_with_time: List of objects representing barlines, each with a 'type' field and a 'time' field.
	
	Output:
	- pac-voices. List of voices, each voice is a list of pac-events. pac-events have a 'pitches' and a 'duration' field. A pitch consists of a 'pitch' and an 'acc' field. The acc field can be sharp, flat, natural, dblsharp, dblflat or none.
	
	Returns the given list of voices, but accidentals of a note in a bar now apply for all notes with the same octave_pitch after the note in the bar. The given key accidentals are applied, if there is no accidental in the bar for this pitch. 
	"""

	if all(map(lambda voice: len(voice) == 0, voices)):
		return voices

	current_time = Fraction(0, 1)
    # a voice is a list of poac-Events here, turn it to an dictionary, so we can add more fields to it.
	voices = list(map(lambda voice: {'events': voice}, voices))

	for voice in voices:
		voice['current_event_index'] = 0
		voice['current_time'] = Fraction(0, 1)
		voice['time_of_next_event'] = voice['events'][voice['current_event_index']]['duration']
	
	end_time = get_line_end_time([voice['events'] for voice in voices]) # This also checks for end_time consistency for each voice in the line. If not all end_times are equal, it throws an exception. 
	
	bar_accidentals = [] # List of objects, each with a 'octave_pitch' and a 'acc' field (sharp, flat, natural, none, ...)

	while True:
		
		time_of_next_event = min(map(lambda voice: voice['time_of_next_event'], voices))

		# Wenn ein neuer Takt beginnt, werden die accidentals aus dem vorherigen Takt gelöscht.
		if barlines_with_time and barlines_with_time[0]['time'] == current_time:
			bar_accidentals = []
			barlines_with_time = barlines_with_time[1:]

		for voice in voices:
			#bei allen gleichzeitig beginnenden neuen events werden die accidentals geupdatet:
			#
			#Für jede Note dieses Events:
			#  Wenn note kein Versetzungszeichen hat:
			#    Wenn Versetzungszeichen in diesem Takt für diesen octave pitch gilt: Füge dieses accidental der Note hinzu
			#    Sonst Wenn Vorzeichen für diesen pitch gilt: Füge dieses accidental der Note hinzu 
			#  Wenn pitch Versetzungszeichen hat:
			#    Lösche eventuell vorhandenes accidental für diesen octave_pitch in diesem Takt
			#    Füge dieses accidental mit dem octave_pitch der Note den für diesen Takt geltenden accidentals hinzu
			if voice['current_time'] == current_time:
				for pitch in voice['events'][voice['current_event_index']]['pitches']:

					if pitch['acc'] == 'none':
						if pitch['octave_pitch'] in map(lambda x: x['octave_pitch'], bar_accidentals):
							pitch['acc'] = list(filter(lambda x: x['octave_pitch'] == pitch['octave_pitch'], bar_accidentals))[0]['acc']
						elif pitch['pitch'] in map(lambda x: x['pitch'], accidentals):
							pitch['acc'] = list(filter(lambda x: x['pitch'] == pitch['pitch'], accidentals))[0]['acc']
					else:
						#if pitch['octave_pitch'] in map(lambda x: x['octave_pitch'], bar_accidentals):
						bar_accidentals = list(filter(lambda x: x['octave_pitch'] != pitch['octave_pitch'], bar_accidentals))
						bar_accidentals.append({'octave_pitch': pitch['octave_pitch'], 'acc': pitch['acc']})
					del pitch['octave_pitch']
				voice['current_time'] += voice['events'][voice['current_event_index']]['duration']
				voice['current_event_index'] += 1
				


		current_time = time_of_next_event
		if current_time == end_time:
			break
		
		    
		for voice in voices:
			if voice['time_of_next_event'] == current_time:
				voice['time_of_next_event'] += voice['events'][voice['current_event_index']]['duration']

	return list(map(lambda voice: voice['events'], voices))


def get_line_end_time(voices):
	"""
	Input:
	- voices: a list of voices, where each voice is a list of Events, where each Event has at least a 'duration'-field.
	
	Output: Fraction object. The time of the line, where the last note ends.
    
	Checks whether all the given voices have the same end_time. If this is not true, an exception is raised.
	If all voices have the same end_time, it returns this end_time.
	"""
	if voices == []:
		return Fraction(0, 1)
	end_times = list(map(lambda voice: get_voice_end_time(voice), voices))
	for end_time in end_times:
		if end_time != end_times[0]:
			raise Exception("There are different end_times in the same line!")
	return end_times[0]


def get_voice_end_time(voice):
    """
    Input:
    - voice: a list of Events, where each Event has at least a 'duration'-field.
    
	Output: Fraction object. The time of the voice, where the last note ends.
    """
    end_time = Fraction(0, 1)
    for event in voice:
        end_time += event['duration']
    return end_time


def remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter):
	"""
	Input:
	- barlines_with_time: List of objects, each with a 'type' field and a 'time' field.
	The 'type' field is either 'bar_thin', 'bar_thin_thin', 'bar_thick_thin', 'bar_thin_thick', 'bar_right_repeat', 'bar_left_repeat', 'bar_dbl_repeat'.
	The 'time' field is a Fraction.
	- meter: Fraction. Die Länge eines Taktes.
	
	Output:
	- barlines_with_time: List of objects, each with a 'type' field and a 'time' field.

	Removes barlines with type 'bar_thin_thin' if their time is not exactly a meter bigger than the time of the previous barline or a meter bigger than 0.
	"""
	new_barlines_with_time = []

	if barlines_with_time == None:
		raise Exception('barlines_with_time is None.')

	if len(barlines_with_time) == 0:
		return new_barlines_with_time

	if barlines_with_time[0]['type'] == 'bar_thin_thin':
		if barlines_with_time[0]['time'] == 0 or barlines_with_time[0]['time'] == meter:
			new_barlines_with_time.append(barlines_with_time[0])
	else:
		new_barlines_with_time.append(barlines_with_time[0])
	barlines_with_time = barlines_with_time[1:]
	
	for i in range(len(barlines_with_time)):
		if barlines_with_time[i]['type'] == 'bar_thin_thin':
			if barlines_with_time[i]['time'] == new_barlines_with_time[-1]['time'] + meter:
				new_barlines_with_time.append(barlines_with_time[i])
		else:
			new_barlines_with_time.append(barlines_with_time[i])
	
	return new_barlines_with_time


def voices_to_poac_and_bar_lines(voices, is_compound):
	"""
	Input:
	- voices: List of voices of one staff, where each voice is a unprocessed list (a true abcjs voice) of abcjs-objects, each with a el_type-field like 'bar', 'stem', 'note'
	- is_compound: Boolean. True, wenn die Taktart ein Vielfaches von 3 an Achteln, 16teln etc. ist, sonst False.
	
	Output:
	- voices: List of voices, where each voice is a list of poac-events: {'pitches': [{'pitch': 0-6, 'octave_pitch': int, 'acc': ''}, ...], 'duration': Fraction}
	- barlines_with_time: List of objects, each with a 'type' field and a 'time' field.

	Converts each voice of abcjs-objects to a voice of poac-events. Also returns a list of the barlines of the staff with their time.
	"""
	voices = list(map(lambda voice: voice_to_poac_with_bar_lines(voice, is_compound), voices))
	barlines_with_time = get_barlines_with_time(voices)
	voices = list(map(lambda voice: list(filter(lambda x: 'pitches' in x, voice)), voices)) # Remove barlines
	
	return voices, barlines_with_time
	

def get_barlines_with_time(voices):
	"""
	Input:
	- voices: List of voices of one staff, where each voice is a list of poac-events and bar_lines:
	[
		{'pitches': [{'pitch': 0-6, 'octave_pitch': int, 'acc': ''}, ...], 'duration': Fraction},
		{'type': 'bar_thin'},
		...
	]

	Output:
	- barlines_with_time: List of objects, each with a 'type' field and a 'time' field.

	Returns a list of the barlines of the staff with the time when they occur in the staff,
	calculated by adding up the durations of the notes and rests of the first voice in the staff.
	"""
	if len(voices) == 0:
		return []
	
	barlines_with_time = []
	time = Fraction(0, 1)
	for event in voices[0]:
		if 'pitches' in event:
			time += event['duration']
		if 'type' in event:
			barlines_with_time.append({'type': event['type'], 'time': time})
	return barlines_with_time


def voice_to_poac_with_bar_lines(voice, is_compound):
	"""
	Input:
	- voice: List of objects, each with a el_type-field like 'bar', 'stem', 'note'
	- is_compound: Boolean. True, wenn die Taktart ein Vielfaches von 3 an Achteln, 16teln etc. ist, sonst False.

	Output:
	- voice: List of objects, but now only with notes(chords) and bars. 
	Durations has been converted to fractions.
	Notes has been breaked down to poac-events: objects with only pitches and duration field. bars only have a type field now. pitches have been converted to poac-pitches, which has the additional octave_pitch field, which is an int of unspecified range: 0 is middle c, 1 is d above middle c, -1 is b below middle c, -7 is c below that, 7 is c above middle c, etc.
	"""
	voice = list(filter(lambda x: x['el_type'] in ['note', 'bar'], voice))
	voice = durations_to_fractions(voice, is_compound)
	voice = abcjs_to_poac_events_with_bar_lines(voice)
	return voice


def abcjs_to_poac_events_with_bar_lines(voice):
	"""
	Input:
	- voice: List of abcjs-objects, each with a el_type-field like 'bar', 'stem', 'note'

	Output:
	- voice: List of objects, but now only with poac-events and bars (objects with only a 'type' attribute).

	Converts abcjs-objects of a abcjs-voice to a voice of poac-events and bars.
	"""
	return list(map(lambda x: abcjs_to_poac_event_or_bar_line(x), voice))

def abcjs_to_poac_event_or_bar_line(x):
	"""
	Input:
	- x: abcjs-object, which is either a abcjs-event ('duration', 'pitches' (with 'pitch' and possibly 'accidental' field, if the event is a chord, rests do not have this field), 'el_type') or a bar (with fields 'type' and 'el_type').
	
	Output:
	- x: poac-event ('pitches' and 'duration' field, pitches are poac-pitches with 'pitch', 'octave_pitch' and 'acc' fields) or, for a bar, a object with only the 'type' field.

	Converts abcjs-events to poac-events. Or bars to bars with only the 'type' field.
	"""
	if x['el_type'] == 'note':
		return {
	    	'pitches': abcjs_to_poac_pitches(x['pitches']) if 'pitches' in x else [], # "if 'pitches' in x else []" handles rests
	    	'duration': x['duration']
		}
	elif x['el_type'] == 'bar':
		return {
			'type': x['type']
		}

def abcjs_to_poac_pitches(pitches):
	"""
	Input:
	- pitches: List of objects, each with a 'pitch' field (an int where 0 is middle c, 1 is d above middle c, -1 is b below middle c, -7 is c below that, 7 is c above middle c, etc.)
	and possibly a 'accidental' field ('sharp', 'flat', 'natural', 'dblsharp', 'dblflat')
	(There are other fields like 'name', but they are not relevant here.)
	
	Output:
	- pitches: List of poac-pitches, each with a 'pitch' field (0-6), a 'octave_pitch' field (int, same as input pitch) and a 'acc' field ('sharp', 'flat', 'natural', 'none', 'dblsharp', 'dblflat')

	Converts abcjs-pitches to poac-pitches.
	"""
	for i, p in enumerate(pitches):
		pitches[i] = {
			'pitch': p['pitch'] % 7,
			'octave_pitch': p['pitch'],
			'acc': p['accidental'] if 'accidental' in p else 'none' 
		}
	return pitches


def get_accidentals(staff):
	'''
	Input:
	- staff: Staff-Objekt, welches ein Attribut 'key' hat.
	
	Output:
	- accidentals: List of objects, each with a 'pitch' field (0-6) and a 'acc' field ('sharp', 'flat', 'dblsharp', 'dblflat')

	Bekommt ein Staff-Objekt, welches ein Attribut 'key' hat und erstellt daraus eine Liste aller Vorzeichen der Tonart:
	accidentals = [
				{
					'acc': 'sharp', 'flat', 'dblsharp', 'dblflat'
					'pitch': int in range 0-6, für c,d,e,f,g,a,b
				},
				...
			]
	'''
	return list(map(lambda a: {'acc': a['acc'], 'pitch': abcjs_name_to_pac_pitch(a['note'])}, staff['key']['accidentals'])) if 'key' in staff and 'accidentals' in staff['key'] else []


def determine_mode(lines):
	"""
	Input:
	- lines: [
		{
			staff: [Notenzeile]
		}
	]. Das Array kann mehrere Objekte enthalten.
	Dieses Objekt ist Rückgabewert von der renderABC()-Methode aus der abcjs-Bibliothek, welches noch von einer Javascript-Funktion reduziert wurde.

	Output: String. Entweder 'single' oder 'bar'.

	Bestimmt, ob Versetzungszeichen immer für einen Takt gelten sollen ('bar') oder nur für die Note, vor der sie direkt stehen ('single'). Wenn meter (Taktlänge) definiert ist und innerhalb eines Taktes eine barline auftaucht, ist der Modus 'bar', sonst 'single'.   
	"""

	if len(lines) == 0:
		raise Exception('No lines defined.')
	
	if not ('staff' in lines[0]):
		raise Exception('No staff defined.')

	meter, is_compound = get_meter(lines[0])

	if meter is None:
		return 'single'

	first_voice = lines[0]['staff'][0]['voices'][0] # first line, first staff, first voice

	first_voice_with_fractions_as_durations = durations_to_fractions(copy.deepcopy(first_voice), is_compound)

	time = Fraction(0, 1)
	for event in first_voice_with_fractions_as_durations:
		if event['el_type'] == 'note':
			time += event['duration']
			if time > meter: # if there is no barline within the first bar
				break
		if event['el_type'] == 'bar':
			return 'bar'

	return 'single'


def get_meter(line):
	"""
	Input:
	- line: {staff: [Notenzeile]}. Dieses Objekt ist Rückgabewert von der renderABC()-Methode aus der abcjs-Bibliothek, welches noch von einer Javascript-Funktion reduziert wurde.
	
	Output: Fraction. Die Länge eines Taktes, wenn ein meter in der ersten Notenzeile der line existiert und der type davon specified ist, sonst None.
	"""
	first_staff = line['staff'][0]
  
	if not ('meter' in first_staff):
		return None, None
	
	if first_staff['meter']['type'] == 'common_time' or first_staff['meter']['type'] == 'cut_time':
		return Fraction(1, 1), False # Fraction wird intern eh auf den kleinsten gemeinsamen Nenner gekürzt, also ist Fraction(1, 1) das gleiche wie Fraction(2, 2) oder Fraction(4, 4)
		
  
	if not (first_staff['meter']['type'] == 'specified'):
		return None, None

	# Siehe https://abcnotation.com/wiki/abc:standard:v2.1#duplets_triplets_quadruplets_etc für die Verwendung von compound meter
	is_compound = True if int(first_staff['meter']['value'][0]['num']) in [3,6,9,12,15,18,21,24] and int(first_staff['meter']['value'][0]['den']) in [8,16,32,64,128] else False

	return meter_to_fraction(first_staff['meter']), is_compound