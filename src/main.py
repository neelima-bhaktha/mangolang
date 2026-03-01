import re
import sys
import traceback

SLANG_MAP = {
    "andhaa": "if",
    "bete": "else",
    "onji-onji": "for",
    "adaga": "while",
    "yavuyaa": "break",
    "panyaa": "print",
    "put_yaa": "input",
    "that_means": "def",
    "tikkuga": "return",
    "bka" : "and",
    "ath_anda" :"or",
    "ijji" : "not"
}


def translate_code(code):
    parts = re.split(r'(".*?"|\'.*?\')', code)

    for i in range(len(parts)):
        if not (parts[i].startswith('"') or parts[i].startswith("'")):
            for slang, python_word in SLANG_MAP.items():
                pattern = r'\b' + re.escape(slang) + r'\b'
                parts[i] = re.sub(pattern, python_word, parts[i])

    return "".join(parts)


def main():
    if len(sys.argv) < 2:
        print("Usage: mangolang <file.mng>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding="utf-8-sig") as f:
            original_code = f.read()
    except FileNotFoundError:
        print("[ MANGOLANG ERROR ] File not found.")
        sys.exit(1)

    original_lines = original_code.splitlines()
    translated_code = translate_code(original_code)

    try:
        exec(translated_code)

    except SyntaxError as e:
        print("\n[ PONDU POORA PONDU (SYNTAX ERROR) ]")
        line_no = e.lineno
        if line_no and line_no <= len(original_lines):
            print(f"Line {line_no}: {original_lines[line_no - 1]}")
        else:
            print(f"Line {line_no}")

    except Exception as e:
        print("\n[ PONDU POORA PONDU (RUNTIME ERROR) ]")
        tb = traceback.extract_tb(e.__traceback__)
        last_call = tb[-1]
        line_no = last_call.lineno
        if line_no and line_no <= len(original_lines):
            print(f"Line {line_no}: {original_lines[line_no - 1]}")
        else:
            print(str(e))


if __name__ == "__main__":
    main()