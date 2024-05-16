def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Ensure shift is within the range of 0-25
            if mode == 'encrypt':
                if char.islower():
                    encrypted_char = chr((ord(char) - 97 + shift_amount) % 26 + 97)
                else:
                    encrypted_char = chr((ord(char) - 65 + shift_amount) % 26 + 65)
            elif mode == 'decrypt':
                if char.islower():
                    decrypted_char = chr((ord(char) - 97 - shift_amount) % 26 + 97)
                else:
                    decrypted_char = chr((ord(char) - 65 - shift_amount) % 26 + 65)
                encrypted_char = decrypted_char
            result += encrypted_char
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (an integer): "))
        
        if choice == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, 'encrypt')
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_cipher(message, shift, 'decrypt')
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
