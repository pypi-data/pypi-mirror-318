from analyze_harmonic_states import analyze_harmonic_states
from calc_harmonies import calc_harmonies
from preprocess import preprocess
from to_abc_strings import analysis_to_abc_strings
from representation import to_analyze_representation
from analyze_sauterian_formula import analyze_sauterian_formula
from analyze_degree_of_dissonance_or_atonal import analyze_degree_of_dissonance_or_atonal
from type import parse_harmonic_state


def get_analyzed_abc_strings(truncated_lines, start_harmonic_state = '[All]'):
    """
	Input:
	- lines: Liste. Das lines-Objekt aus der Rückgabe von renderABC() in Javascript, wovon einige Felder durch eine Javascript-Funktion gelöscht wurden.
    Siehe Funktion del(lines) in abcjs11.astro im Astro-Projekt.
	Jede line enthält eine grafische Notenzeile mit allen Instrumenten und Stimmen.
	Dieses Objekt enthält eine Codierung aller für die harmonischen Analyse benötigten musikalischen Information wie Notennamen und Dauer von Noten.
    - start_harmonic_state: String. A String representing a HarmonicState which will be used as the HarmoncState before the first harmony in the music.
	
	Output:
    - analysis_abc_string: Dictionary with the following fields:
    - header: String. The header of the abc analysis: '\nL:1\n'.
    - events: List of strings. Format: '[V: Analysis] [CE^^G]1/4 [C_EGB]1/4\n'. Each string represents the harmonies of one line of music.
    - harmonic_states: List of strings. Format: 'w: [C,Cis,Dm] [C,Cis,Dm]\n'. Each string corresponds to the events of one line.
    - sauterian_formula: List of strings. Format: 'w: T15D15S3 D35S1A3,11\n'. Each string corresponds to the events of one line.
    - degree_of_dissonance_or_atonal: List of strings. Format: 'w: / low\n'. Each string corresponds to the events of one line.

    - informations: Liste. Enthält Informationen über die Analyse, die in der GUI angezeigt werden sollen.
    - error: String. Enthält eine Fehlermeldung, falls ein Fehler aufgetreten ist.
	"""

    if not truncated_lines:
        return '', [], 'No lines found.'

    informations = []
    try:
        lines_with_pac_voices, preprocess_infos = preprocess(truncated_lines)

        pac_harmony_lines = list(map(lambda line: calc_harmonies(line), lines_with_pac_voices))

        pac_music = [] # list of events
        for harmonies in pac_harmony_lines:
            pac_music.extend(harmonies)

        music = to_analyze_representation(pac_music)
        
        analysis = analyze_harmonic_states(music, parse_harmonic_state(start_harmonic_state))
        
        analysis = analyze_sauterian_formula(analysis)
        
        analysis = analyze_degree_of_dissonance_or_atonal(analysis)
        
        analysis_abc_strings = analysis_to_abc_strings(analysis, pac_harmony_lines)

        return analysis_abc_strings, informations + preprocess_infos, None
    
    except Exception as e:
        return '', informations, str(e) 
