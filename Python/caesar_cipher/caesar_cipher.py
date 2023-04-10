# Caesar cipher
def caesar_cipher(text, shift): #Shit is how much letters the text move 
    
    cipher_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char.upper()) - 65 + shift)% 26 +65) #ASCII VALUE
            if char.islower():
                cipher_text += shifted_char.lower()
            else:
                cipher_text += shifted_char
        else:
            cipher += char
    return cipher_text

def caesar_decipher(cipher_text,shift):
    text = ""
    for char in cipher_text:
        if char.isalpha():
            shifted_char = chr((ord(char.upper()) - 65 - shift)% 26 +65) #ASCII VALUE
            if char.islower():
                text += shifted_char.lower()
            else:
                text += shifted_char
        else:
            cipher += char
    return text
 

if __name__ == "__main__":
    text = input("Type a text: ")
    shift = 3
    encrypted = caesar_cipher(text,shift)
    print(caesar_cipher(text,shift))
    print(caesar_decipher(encrypted,shift))
