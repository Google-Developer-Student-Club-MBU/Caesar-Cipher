"""
caesar cipher overview:
The Caesar cipher is cryptogrraphy technique which shifts all the letters in a piece of text by a certain number
of places. The key for this cipher is a letter which represents the number of
place for the shift. So, for example, a key D means “shift 3 places” and a
key M means “shift 12 places”. Note that a key A means “do not shift” and
a key Z can either mean “shift 25 places” or “shift one place backwards”.
For example, the word “CAESAR” with a shift P becomes “RPTHPG”.

"""

# Python code for caesar cipher problem
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            encrypted_code = (char_code + shift) % 26
            encrypted_char = chr(encrypted_code + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            decrypted_code = (char_code - shift) % 26
            decrypted_char = chr(decrypted_code + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = caesar_encrypt(message, shift)
    decrypted_message = caesar_decrypt(encrypted_message, shift)

    print("Original message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
