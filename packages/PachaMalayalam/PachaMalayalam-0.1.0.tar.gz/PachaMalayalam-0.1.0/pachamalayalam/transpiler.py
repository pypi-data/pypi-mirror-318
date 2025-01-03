import sys

KEYWORD_MAP = {
    # keywords okke ivdend
    'ചെജ്ജ്': 'def',
    'അതിപ്പോ': 'if',
    'അല്ലെങ്കിൽ': 'else',
    'അതുക്കുംമേലെ': 'elif',
    'സത്യം': 'True',
    'പച്ചനൊണ': 'False',
    'ഒന്നുല്ല': 'None',
    'കൈഞ്ഞു': 'return',
    'അയില്': 'for',
    'അങ്ങന്യാണേൽ': 'while',
    'നിർത്തിക്കോളി': 'break',
    'നടക്കട്ടെ': 'continue',
    'സോപ്പുമ്പെട്ടി': 'class',
    'ഇണ്ടെങ്കില്': 'in',
    'അയിന്ന്': 'from',
    'ഇറക്കിക്കോളി': 'import',
    'അത്രമതി': 'pass',
    'ആണേൽ': 'is',
    'അല്ലേൽ': 'not',
    'അതുംകൂടി': 'and',
    'ഏതേലും': 'or',
    'കളഞ്ഞോളി': 'del',
    # builtin functions
    'പറഞ്ഞോളി': 'print',
    'കടൽ': 'range',
    'എഴുതിക്കോളി': 'input',
    'പട്ടിക': 'list',
    'ആവർത്തനം': 'len',
    'ആകുന്നു': 'type',
    'ഉയർത്തുക': 'raise',
    'എല്ലാ': 'all',
    'ഒന്നെങ്കിലും': 'any',
    'വിശദീകരിക്കുക': 'help',
    # kidilan per kitteella, pinne updateyyaam (suresh_krishna.jpg)
    'ജോഡി': 'tuple',
    'നിഘണ്ടു': 'dict',
    'കുറുക': 'set',
    'സൂചിക': 'index',
    'തരം': 'sort',
    # ithokke enthonnu, humm!
    'ഇതോക്ക്': 'try',
    'നടന്നിട്ടില്ലേൽ': 'except',
    'ഒക്കെകൈഞ്ഞു': 'finally',
    'എന്തായാലും': 'assert',
    'കൊടുക്കിം': 'yield',
}

def transpile(malayalam_code):
    python_code = malayalam_code
    for mal_keyword, py_keyword in KEYWORD_MAP.items():
        python_code = python_code.replace(mal_keyword, py_keyword)
    return python_code

def main():
    if len(sys.argv) != 2:
        print("ഇതിങ്ങനെ ചെയ്യണം: pachalang <ഫയൽ.pymal>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            malayalam_code = file.read()

        python_code = transpile(malayalam_code)

        # print("Transpiled Python Code:")
        # print(python_code)
        # print("-" * 40)

        # Ivide execute cheyyanam!
        exec(python_code)
    except FileNotFoundError:
        print(f"പ്രശ്നാണല്ലോ! : ഫയൽ '{file_path}' കണ്ടില്ല.")
    except Exception as e:
        print(f"എന്തോ ഒരു വിഷയണ്ട്: {e}")

if __name__ == "__main__":
    main()
