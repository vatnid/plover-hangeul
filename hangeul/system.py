# fmt: off
#
#   S T P H *   * J P H T D
#   S K W R *   * R B G S Z
#
#         A O   E U
#
KEYS = (
    '#',
    'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
    'A-', 'O-',
    '*',
    '-E', '-U',
    '-J', '-R', '-P', '-B', '-H', '-G', '-T', '-S', '-D', '-Z',
)
# fmt: on

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '-E', '-U', '*')
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
        'S-'        : ('S1-', 'S2-'),
        'T-'        : 'T-',
        'K-'        : 'K-',
        'P-'        : 'P-',
        'W-'        : 'W-',
        'H-'        : 'H-',
        'R-'        : 'R-',
        'A-'        : 'A-',
        'O-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-U'        : '-U',
        '-J'        : '-F',
        '-R'        : '-R',
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
        'S-'        : ('q', 'a'),
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'W-'        : 'd',
        'H-'        : 'r',
        'R-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-U'        : 'm',
        '-J'        : 'u',
        '-R'        : 'j',
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
