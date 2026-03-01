import re

SLANG_MAP = {
    "andhaa": "if",
    "ath_anda": "else",
    "onji-onji": "for",
    "adaga": "while",
    "yavuyaa": "break",
    "panyaa": "print",
    "put_yaa": "input",
    "poyi" : "exit"
}

filename = "sample.mng"

with open(filename, "r") as f:
    code = f.read()

def translate_code(code):
    # Split into string and non-string parts
    parts = re.split(r'(".*?"|\'.*?\')', code)

    for i in range(len(parts)):
        # Only modify parts that are NOT strings
        if not (parts[i].startswith('"') or parts[i].startswith("'")):
            for slang, python_word in SLANG_MAP.items():
                pattern = r'\b' + re.escape(slang) + r'\b'
                parts[i] = re.sub(pattern, python_word, parts[i])

    return "".join(parts)

code = translate_code(code)

exec(code)