# fmt: off
#
#   H T P Y *   * J P H T D
#   S K R W *   * L B G S Z
#
#         A O   E U
#
KEYS = (
    '#',
    'H-', 'S-', 'T-', 'K-', 'P-', 'R-', 'Y-', 'W-',
    'A-', 'O-',
    '*',
    '-E', '-U',
    '-J', '-L', '-P', '-B', '-H', '-G', '-T', '-S', '-D', '-Z',
)
# fmt: on

IMPLICIT_HYPHEN_KEYS = ('Y-', 'W-', 'A-', 'O-', '-E', '-U', '*')
SUFFIX_KEYS = ()
NUMBER_KEY = None
NUMBERS = {}
FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = "*"

ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'H-'        : 'S1-',
        'S-'        : 'S2-',
        'T-'        : 'T-',
        'K-'        : 'K-',
        'P-'        : 'P-',
        'R-'        : 'W-',
        'Y-'        : 'H-',
        'W-'        : 'R-',
        'A-'        : 'A-',
        'O-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-U'        : '-U',
        '-J'        : '-F',
        '-L'        : '-R',
        '-P'        : '-P',
        '-B'        : '-B',
        '-H'        : '-L',
        '-G'        : '-G',
        '-T'        : '-T',
        '-S'        : '-S',
        '-D'        : '-D',
        '-Z'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'H-'        : 'q',
        'S-'        : 'a',
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'R-'        : 'd',
        'Y-'        : 'r',
        'W-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-U'        : 'm',
        '-J'        : 'u',
        '-L'        : 'j',
        '-P'        : 'i',
        '-B'        : 'k',
        '-H'        : 'o',
        '-G'        : 'l',
        '-T'        : 'p',
        '-S'        : ';',
        '-D'        : '[',
        '-Z'        : '\'',
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
}
KEYMAPS["Plover HID"] = KEYMAPS["Gemini PR"]

DICTIONARIES_ROOT = None
DEFAULT_DICTIONARIES = ()
