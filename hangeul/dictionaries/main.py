import hangul_jamo
import re

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 1

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(outline):
    assert len(outline) <= LONGEST_KEY

    p = re.compile("([HSTKPR]*)([-YWAOEU*]*)([JLPBHGTSDZ]*)")
    m = p.match(outline[0])
    if not m:
        raise KeyError
    initial = m.group(1)
    vowel = m.group(2)
    final = m.group(3)

    initial_jamo = { "":     "ㅇ",
                     "K":    "ㄱ",   "SK":    "ㄲ",   "KP":   "ㅋ",
                     "TK":   "ㄷ",   "STK":   "ㄸ",   "T":    "ㅌ",
                     "PR":   "ㅂ",   "SPR":   "ㅃ",   "P":    "ㅍ",
                     "KR":   "ㅈ",   "SKR":   "ㅉ",   "TP":   "ㅊ",
                     "HTP":  "ㄴ",   "HT":    "ㅁ",   "R":    "ㄹ",
                     "S":    "ㅅ",   "HS":    "ㅆ",   "H":    "ㅎ" }
    vowel_jamo =   { "":     "",
                     "A":    "ㅏ",   "YA":    "ㅑ",   "WA":   "ㅘ",
                     "AE":   "ㅐ",   "YAE":   "ㅒ",   "WAE":  "ㅙ",
                     "OE":   "ㅓ",   "YOE":   "ㅕ",   "WO":   "ㅝ",
                     "E":    "ㅔ",   "YE":    "ㅖ",   "WE":   "ㅞ",
                     "O":    "ㅗ",   "YO":    "ㅛ",   "OEU":  "ㅚ",
                     "U":    "ㅜ",   "YU":    "ㅠ",   "WEU":  "ㅟ",
                     "AO":   "ㅡ",   "EU":    "ㅣ",   "AOEU": "ㅢ" }
    final_jamo =   { "":     "",
                     "G":    "ㄱ",   "HG":    "ㄲ",   "GS":   "ㄳ",
                     "PB":   "ㄴ",   "JPB":   "ㄵ",   "PBH":  "ㄶ",
                     "D":    "ㄷ",   "L":     "ㄹ",   "LG":   "ㄺ",
                     "LPH":  "ㄻ",   "LB":    "ㄼ",   "LS":   "ㄽ",
                     "LT":   "ㄾ",   "LP":    "ㄿ",   "LH":   "ㅀ",
                     "PH":   "ㅁ",   "B":     "ㅂ",   "BS":   "ㅄ",
                     "S":    "ㅅ",   "Z":     "ㅆ",   "PBG":  "ㅇ",
                     "J":    "ㅈ",   "JP":    "ㅊ",   "BG":   "ㅋ",
                     "T":    "ㅌ",   "P":     "ㅍ",   "H":    "ㅎ" }

    # Check if all parts are valid
    if not all((initial in initial_jamo, vowel in vowel_jamo, final in final_jamo)):
        raise KeyError

    # Initialise result
    result_decomposed = f"{initial_jamo[initial]}{vowel_jamo[vowel]}{final_jamo[final]}"
    result = hangul_jamo.compose(result_decomposed)

    return "{^" + result + "^}"

# Optional: return an array of stroke tuples that would translate back
# to <text> (an empty array if not possible).
def reverse_lookup(translation):
    return []
