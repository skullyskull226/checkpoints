from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    # Generate a key
    key = generate_key()
    print("Generated Key:", key.decode())

    # User input
    user_input = input("Enter a message to encrypt: ")

    # Encrypt the user input
    encrypted_message = encrypt_message(user_input, key)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
