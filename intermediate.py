def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        return chr((ord(letter) - 65 + shift) % 26 + 65)
    
def caesar_cipher(message, shift):
    result = ""
    for char in message:
        result += shift_letter(char, shift)
    return result

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    shift = ord(letter_shift) - 65
    return shift_letter(letter, shift)

def vigenere_cipher(message, key):
    key = key * ((len(message) // len(key)) + 1)
    result = ""
    for i in range(len(message)):
        if message[i] != " ":
            shift = ord(key[i]) - 65
            result += shift_letter(message[i], shift)
        else:
            result += " "
    return result
 
def scytale_cipher(message, shift):
    message += "_" * (len(message) % shift)
    result = ""
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        result += message[index]
    return result

def scytale_decipher(message, shift):
    message += "_" * (len(message) % shift)
    result = [""] * len(message)
    for i in range(len(message)):
        index = (i % (len(message) // shift)) * shift + (i // (len(message) // shift))
        result[index] = message[i]
    return "".join(result).rstrip("_")
