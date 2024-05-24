from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Directory to store received keys
KEY_STORAGE_DIR = "keys"
os.makedirs(KEY_STORAGE_DIR, exist_ok=True)

@app.route('/receive_key', methods=['POST'])
def receive_key():
    key = request.json.get('key')
    client_id = request.json.get('client_id')
    
    if not key or not client_id:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

    # Store the key in a file named after the client ID
    key_file = os.path.join(KEY_STORAGE_DIR, f"{client_id}.key")
    with open(key_file, 'wb') as f:
        f.write(key.encode())
    
    return jsonify({"status": "success", "message": "Key received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
