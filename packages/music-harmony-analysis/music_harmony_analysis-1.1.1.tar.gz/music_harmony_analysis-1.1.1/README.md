This library implements some functions for analyzing the harmonic happenings in music. The algorithms are based on a relatively unknown theory of harmony in music by Franz Sauter, specified for implementation by Louis Krüger. This Theory is described in the book of Franz Sauter 'Tonal music: Anatomy of the Musical Aesthetics' (German: 'Die tonale Musik: Anatomie der musikalischen Ästhetik').
One interesting aspect of the theory is that modulations are defined in a way that it can be implemented in a computer program: A modulation occurs if we hear a tone which is not part of the key in which we were before. Instead, we are modulating to the key which
1. has all the tones of the new harmony we are hearing and
2. has the most tones in common with the old key we were in.


This library offers the following functions:
- calc_harmonies: This calculates the resulting harmonies of different simultaneous voices (for example different instruments playing together) in music. The result can be used for:
- analyze_harmonic_states: From the harmonies that a listener hears the 'harmonic state' in which the listener is is calculated. This term belongs to the theory and describes the key that a listener would assume as the current key in which the music is. A harmonic state can consist of multiple keys simultaneously.
- analyze_sauterian_formula: Gives back the sauterian formula for each harmony, where the harmonic state has exactly one key. This roughly corresponds to whether the scale degrees for the individual notes of the tonic, dominant and subdominant chords of a key are used in the sounding harmony.
- analyze_degree_of_dissonance: Based of the sauterian formula of a harmony this gives the degree of dissonance for this harmony: It can be consonant, 'false consonant', can ba a low, medium or high level of dissonanca or it can be an atonal harmony of one of 5 degrees, if the tones of the harmony do not occur in any key.


This library is used in a tool for automatic music harmony analysis that can be found on the website www.notenentwickler.com
Also some additional explanation of the theory can be found there.
The other modules abcjs_interface, preprocess and to_abc_strings in this package are developed for this project and are not specifically intended for general use.