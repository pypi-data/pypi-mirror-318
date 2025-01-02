from fractions import Fraction


def meter_to_fraction(meter):
    """
    Input:
    - meter: Dictionary mit den Feldern 'type' und 'value'. value ist ein Array mit einem Element, welches ein Dictionary mit den Feldern 'num' und 'den' ist.
    
    Output: Fraction. Der Wert von meter.
    """
    m = meter['value'][0]
    return Fraction(int(m['num']), int(m['den']))


def voice_duration(voice):
    """
    Input:
    - voice: List. Eine Liste von PAC-Events oder PC-Events oder custom-Events. Ein Event muss ein dictionary sein, welches ein 'duration'-Feld hat.
    Output: Fraction. Die Gesamtlänge aller Events in voice.
    """
    time = Fraction(0, 1)
    for event in voice:
        time += event['duration']
    return time


def durations_to_fractions(voice, is_compound = None):
    """
    Input:
    - voice: List. Eine Liste von abcjs-Events:
    abcjs_event: Dictionary mit unter anderem folgenden keys: 'duration', ('startTriplet'), ('endTriplet')
    - is_compound: Boolean. True, wenn die Taktart ein Vielfaches von 3 an Achteln, 16teln etc. ist, sonst False. Default: None.
    
    Output List. Eine Liste von abcjs-Events, wobei die Dauer jedes Events ein Fraction-Objekt ist.
    """
    isTriplet = False
    triplet_divisor = -1
    for event in voice:
        if event['el_type'] == 'note':
            if 'startTriplet' in event:
                isTriplet = True
                triplet_divisor = event['startTriplet']
            event['duration'] = duration_to_fraction(event['duration'], isTriplet, triplet_divisor, is_compound)
            if 'endTriplet' in event:
                isTriplet = False
    
    return voice


def duration_to_fraction(duration, is_triplet = False, triplet_divisor = None, is_compound = None):
    """
    Input:
    - duration: Float. Die Notenlänge, wie sie von abcjs zurückgegeben wird.
    - is_triplet: Boolean. Gibt an, ob die Note in einem Triolen- Quintolen- etc. -abschnitt ist. Default: False.
    - triplet_divisor: Integer. Gibt den Typ der ntole an. 3 für Triolen, 5 für Quintolen, etc. Muss im Bereich 2-9 liegen, da abc höhere Werte nicht unterstützt. Default: None.
    - is_compound: Boolean. True, wenn die Taktart ein Vielfaches von 3 an Achteln, 16teln etc. ist, sonst False. Default: None.
    
    Output:
    - Fraction-Objekt. Mit dem gleichen Wert wie duration, wenn is_triplet False ist.
      Wenn is_triplet=True, wird der Wert je nach Art der ntole mit 2 oder 3 multipliziert und durch triplet_divisor geteilt:

    triplet_divisor | Meaning
    2 | 2 notes in the time of 3
    3 | 3 notes in the time of 2
    4 | 4 notes in the time of 3
    5 | 5 notes in the time of n
    6 | 6 notes in the time of 2
    7 | 7 notes in the time of n
    8 | 8 notes in the time of 3
    9 | 9 notes in the time of n
    If the time signature is compound (3/8, 6/8, 9/8, 12/8) then n is three, otherwise n is two.
    ATTENTION: Because abcjs does not support this differentiation between compound and not compound time signatures, but uses 2 for n even in compound time signatures, this functionality is commented out in the code below.
    Alignment to the lengths of the abcjs notes is more important for my use case now.
    Could be implemented in the future, if needed.
    Then the following tests have to be changed:
    tests/preprocess/test_duration.py::test_duration_to_fraction: test case 6,11
    tests/preprocess/test_duration.py::test_durations_to_fractions: test case 6
    tests/preprocess/to_poac_test.py::test_voices_to_poac_and_bar_lines: test case 7,8


    Konvertiert eine Notenlänge aus dem Format, welches von abcjs zurückgegeben wird, in ein Fraction-Objekt. Die Änderungen der Länge durch ntolen werden berücksichtigt.
    Geschachtelte ntolen werden nicht unterstützt.
    Siehe https://abcnotation.com/wiki/abc:standard:v2.1#duplets_triplets_quadruplets_etc für mehr Informationen zu ntolen.
    """
    if is_triplet:
        if triplet_divisor in [2,4,8]:
            n = 3
        elif triplet_divisor in [3,6]:
            n = 2
        elif triplet_divisor in [5,7,9]:
            #if is_compound is None:
            #    raise Exception("Triplet divisor " + str(triplet_divisor) + " is not allowed without meter.")
            #if is_compound:
            #    n = 3
            #else:
            n = 2
        else:
            raise Exception("Triplet divisor must be in range 2-9. Got " + str(triplet_divisor) + ".")
        
        return switch(duration) * n / triplet_divisor
    else:
        return switch(duration)


def switch(duration):
    """
    Input:
    - duration: Float. Die Notenlänge, wie sie von abcjs zurückgegeben wird.
    
    Output:
    - Fraction-Objekt. Mit dem gleichen Wert wie duration.

    Konvertiert eine Notenlänge aus dem Format, welches von abcjs zurückgegeben wird (Float), in ein Fraction-Objekt.
    Dies ermöglicht bessere Berechnungen mit den Notenlängen.
    Mit dieser Methode sollten alle möglichen Werte in einem von abcjs zurückgegebenen 'duration'-Feld abgedeckt sein.
    """
    if duration == 2: return Fraction(2, 1) # Brevis
    elif duration == 1: return Fraction(2, 2) # Ganze Note
    elif duration == 0.5: return Fraction(2, 4) # Halbe Note
    elif duration == 0.25: return Fraction(2, 8) # Viertelnote
    elif duration == 0.125: return Fraction(2, 16) # Achtelnote
    elif duration == 0.0625: return Fraction(2, 32) # Sechzehntelnote
    elif duration == 0.03125: return Fraction(2, 64) # Zweiunddreißigstelnote
    elif duration == 0.015625: return Fraction(2, 128) # Vierundsechzigstelnote

    elif duration == 3: return Fraction(3, 1) # Brevis mit einem Punkt
    elif duration == 1.5: return Fraction(3, 2) # Ganze Note mit einem Punkt
    elif duration == 0.75: return Fraction(3, 4) # ...
    elif duration == 0.375: return Fraction(3, 8)
    elif duration == 0.1875: return Fraction(3, 16)
    elif duration == 0.09375: return Fraction(3, 32)
    elif duration == 0.046875: return Fraction(3, 64)
    elif duration == 0.0234375: return Fraction(3, 128)

    elif duration == 3.5: return Fraction(7, 2) # Brevis mit zwei Punkten
    elif duration == 1.75: return Fraction(7, 4) # ...
    elif duration == 0.875: return Fraction(7, 8)
    elif duration == 0.4375: return Fraction(7, 16)
    elif duration == 0.21875: return Fraction(7, 32)
    elif duration == 0.109375: return Fraction(7, 64)
    elif duration == 0.0546875: return Fraction(7, 128)
    elif duration == 0.02734375: return Fraction(7, 256)

    elif duration == 3.75: return Fraction(15, 4) # Brevis mit drei Punkten
    elif duration == 1.875: return Fraction(15, 8) # ...
    elif duration == 0.9375: return Fraction(15, 16)
    elif duration == 0.46875: return Fraction(15, 32)
    elif duration == 0.234375: return Fraction(15, 64)
    elif duration == 0.1171875: return Fraction(15, 128)
    elif duration == 0.05859375: return Fraction(15, 256)
    elif duration == 0.029296875: return Fraction(15, 512)
    
    elif duration == 3.875: return Fraction(31, 8) # Brevis mit vier Punkten
    elif duration == 1.9375: return Fraction(31, 16) # ...
    elif duration == 0.96875: return Fraction(31, 32)
    elif duration == 0.484375: return Fraction(31, 64)
    elif duration == 0.2421875: return Fraction(31, 128)
    elif duration == 0.12109375: return Fraction(31, 256)
    elif duration == 0.060546875: return Fraction(31, 512)
    elif duration == 0.0302734375: return Fraction(31, 1024)
    
    elif duration == 3.9375: return Fraction(63, 16) # Brevis mit fünf Punkten
    elif duration == 1.96875: return Fraction(63, 32) # ...
    elif duration == 0.984375: return Fraction(63, 64)
    elif duration == 0.4921875: return Fraction(63, 128)
    elif duration == 0.24609375: return Fraction(63, 256)
    elif duration == 0.123046875: return Fraction(63, 512)
    elif duration == 0.0615234375: return Fraction(63, 1024)
    elif duration == 0.03076171875: return Fraction(63, 2048)
    
    elif duration == 3.96875: return Fraction(127, 32) # Brevis mit sechs Punkten
    elif duration == 1.984375: return Fraction(127, 64) # ...
    elif duration == 0.9921875: return Fraction(127, 128)
    elif duration == 0.49609375: return Fraction(127, 256)
    elif duration == 0.248046875: return Fraction(127, 512)
    elif duration == 0.1240234375: return Fraction(127, 1024)
    elif duration == 0.06201171875: return Fraction(127, 2048)
    elif duration == 0.031005859375: return Fraction(127, 4096)
    
    elif duration == 3.984375: return Fraction(255, 64) # Brevis mit sieben Punkten
    elif duration == 1.9921875: return Fraction(255, 128) # ...
    elif duration == 0.99609375: return Fraction(255, 256)
    elif duration == 0.498046875: return Fraction(255, 512)
    elif duration == 0.2490234375: return Fraction(255, 1024)
    elif duration == 0.12451171875: return Fraction(255, 2048)
    elif duration == 0.062255859375: return Fraction(255, 4096)
    elif duration == 0.0311279296875: return Fraction(255, 8192)
    
    elif duration == 3.9921875: return Fraction(511, 128) # Brevis mit acht Punkten
    elif duration == 1.99609375: return Fraction(511, 256) # ...
    elif duration == 0.998046875: return Fraction(511, 512)
    elif duration == 0.4990234375: return Fraction(511, 1024)
    elif duration == 0.24951171875: return Fraction(511, 2048)
    elif duration == 0.124755859375: return Fraction(511, 4096)
    elif duration == 0.0623779296875: return Fraction(511, 8192)
    elif duration == 0.03118896484375: return Fraction(511, 16384)
    
    else:
        raise Exception("Could not find specified note length: " + str(duration) + """\nMaybe you have used a disallowed muliplier after a note? Allowed mulipliers are:

[L=1 or smaller]: 1,2,3
[L=1/2 ...]: additionaly 4,6,7
[L=1/4]: + 8,12,14,15
[L=1/8]: + 16,24,28,30,31
[L=1/16]: + 32,48,56,60,62,63
[L=1/32]: + 64,96,112,120,124,126,127 
[L=1/64]: + 128,192,224,240,248,252,254,255
[L=1/128]: + 256,384,448,480,496,504,508,510,511

The only divisors allowed are: 2,4,8,16,32,64, in rare cases also 128 for a Brevis note.

You can combine multipliers and divisors to get, for example, a 64th with 8 points:
[L=1/128] a511/128""")