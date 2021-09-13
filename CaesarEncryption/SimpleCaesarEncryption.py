import string

TextToEncrypt = input("input the text you want to encrypt: ")
shift = 13

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = TextToEncrypt.translate(table)

print(encrypted)
