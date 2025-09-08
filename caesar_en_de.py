def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Welcome to Caesar Cipher Encryption/Decryption Program")
    
    # Choose operation
    operation = input("Would you like to Encrypt or Decrypt? (E/D): ").upper()
    if operation not in ['E', 'D']:
        print("Invalid input, please enter 'E' for encryption or 'D' for decryption.")
        return

    # Get user input
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (0-25): "))

    if operation == 'E':
        result = caesar_encrypt(text, shift)
        print("Encrypted Text:", result)
    else:
        result = caesar_decrypt(text, shift)
        print("Decrypted Text:", result)

if __name__ == "__main__":
    main()
