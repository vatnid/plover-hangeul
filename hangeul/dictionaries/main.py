import hangul_jamo
import re

# Length of the longest supported key (number of strokes).
LONGEST_KEY = 1

# Lookup function: return the translation for <key> (a tuple of strokes)
# or raise KeyError if no translation is available/possible.
def lookup(outline):
    assert len(outline) <= LONGEST_KEY

    stroke = outline[0]

    # Fingerspelling
    fingerspelling = {
                     "K*":   "ㄱ",   "SK*":   "ㄲ",   "KP*":   "ㅋ",
                     "TK*":  "ㄷ",   "STK*":  "ㄸ",   "T*":    "ㅌ",
                     "TP*":  "ㅂ",   "STP*":  "ㅃ",   "P*":    "ㅍ",
                     "KR*":  "ㅈ",   "SKR*":  "ㅉ",   "KH*":   "ㅊ",
                     "TPH*": "ㄴ",   "PH*":   "ㅁ",   "R*":    "ㄹ",
                     "S*":   "ㅅ",   "ST*":   "ㅆ",   "H*":    "ㅎ",
                     "W*":   "ㅜ",   "TKPW*": "ㅇ",
                     "A*":   "ㅏ",   "A*U":   "ㅑ",   "WA*":   "ㅘ",
                     "A*E":  "ㅐ",   "A*EU":  "ㅒ",   "WA*E":  "ㅙ",
                     "O*E":  "ㅓ",   "O*EU":  "ㅕ",   "WO*":   "ㅝ",
                     "*E":   "ㅔ",   "AO*E":  "ㅖ",   "W*E":   "ㅞ",
                     "O*":   "ㅗ",   "O*U":   "ㅛ",   "WO*E":  "ㅚ",
                     "*U":   "ㅜ",   "AO*U":  "ㅠ",   "W*EU":  "ㅟ",
                     "AO*":  "ㅡ",   "*EU":   "ㅣ",   "AO*EU": "ㅢ",
                     "*GS":   "ㄳ",  "*JPB":  "ㄵ",   "*JLPB": "ㄵ",
                     "*PBH":  "ㄶ",  "*LG":   "ㄺ",   "*LPH":  "ㄻ",
                     "*LB":   "ㄼ",  "*LS":   "ㄽ",   "*LT":   "ㄾ",
                     "*LP":   "ㄿ",  "*LH":   "ㅀ",   "*BS":   "ㅄ"
                     }
    if stroke in fingerspelling:
        return "{^" + fingerspelling[stroke] + "^}"

    p = re.compile("([STKPWHR]*)([-AOEU*]*)([JLPBHGTSDZ]*)")
    m = p.match(stroke)
    if not m:
        raise KeyError
    initial = m.group(1)
    vowel = m.group(2)
    final = m.group(3)

    # Put W to vowel part
    if "W" in initial:
        vowel = "W" + vowel
        initial = re.sub(r"W", r"", initial)

    initial_jamo = { "":     "ㅇ",
                     "K":    "ㄱ",   "SK":    "ㄲ",   "KP":   "ㅋ",
                     "TK":   "ㄷ",   "STK":   "ㄸ",   "T":    "ㅌ",
                     "TP":   "ㅂ",   "STP":   "ㅃ",   "P":    "ㅍ",
                     "KR":   "ㅈ",   "SKR":   "ㅉ",   "KH":   "ㅊ",
                     "TPH":  "ㄴ",   "PH":    "ㅁ",   "R":    "ㄹ",
                     "S":    "ㅅ",   "ST":    "ㅆ",   "H":    "ㅎ" }
    vowel_jamo =   { "W":    "ㅜ",
                     "A":    "ㅏ",   "AU":    "ㅑ",   "WA":   "ㅘ",
                     "AE":   "ㅐ",   "AEU":   "ㅒ",   "WAE":  "ㅙ",
                     "OE":   "ㅓ",   "OEU":   "ㅕ",   "WO":   "ㅝ",
                     "E":    "ㅔ",   "AOE":   "ㅖ",   "WE":   "ㅞ",
                     "O":    "ㅗ",   "OU":    "ㅛ",   "WOE":  "ㅚ",
                     "U":    "ㅜ",   "AOU":   "ㅠ",   "WEU":  "ㅟ",
                     "AO":   "ㅡ",   "EU":    "ㅣ",   "AOEU": "ㅢ" }
    final_jamo =   { "":     "",
                     "G":    "ㄱ",   "HG":    "ㄲ",   "GS":   "ㄳ",
                     "PB":   "ㄴ",   "JPB":   "ㄵ",   "JLPB": "ㄵ", "PBH":  "ㄶ",
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
