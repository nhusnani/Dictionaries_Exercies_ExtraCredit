work_file = open("info_security.txt", "r")
encrypted_file = open("enrypted_info_security.txt", "w")
info_text = work_file.read()
info_list = info_text.split()

values = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    '"',
    "'",
    "+",
    "=",
    "-",
    ",",
    "|",
    "/",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "}",
    "{",
    "]",
    "[",
    ":",
    ";",
    "<",
    ">",
    "‡",
    "º",
    "Æ",
    "±",
    "»",
    "¼",
    "½",
    "¾",
    "·",
    "¸",
    "_",
    "~",
    "´",
    "µ",
    "¶",
    "¿"
]


key = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


encrypt_dict = {}
i = 0
for a in key:
    encrypt_dict[a] = values[i]
    i += 1

for i in info_list:
    encrypt_word = ""
    i = list(i)
    for char in i:
        cha = encrypt_dict.get(char, char)
        encrypt_word += cha
    encrypted_file.write(encrypt_word + " ")

encrypted_file.close()