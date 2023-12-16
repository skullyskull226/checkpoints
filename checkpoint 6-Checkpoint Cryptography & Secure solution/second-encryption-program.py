from cryptography.fernet import Fernet

# Generate a symmetric key
key = Fernet.generate_key()
cipher = Fernet(key)

# User input
user_input = input("Enter the text to encrypt: ")

# Encrypt the user's input
encrypted_text = cipher.encrypt(user_input.encode())

print("Symmetric Key:", key)
print("Encrypted text:", encrypted_text)
