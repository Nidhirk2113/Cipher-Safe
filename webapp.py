from flask import Flask, render_template, request, jsonify
from src.ciphers.vigenere import VigenereCipher
from src.ciphers.vernam import VernamCipher

app = Flask(__name__)
vigenere = VigenereCipher()
vernam = VernamCipher()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get('text', '')
    mode = data.get('mode', 'vigenere')
    key = data.get('key', '')

    if mode == 'vigenere':
        result = vigenere.encrypt(text, key)
    elif mode == 'vernam':
        result, key = vernam.encrypt(text)
    else:
        return jsonify({'error': 'Invalid mode'}), 400

    return jsonify({'cipher': result, 'key': key})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    text = data.get('text', '')
    mode = data.get('mode', 'vigenere')
    key = data.get('key', '')

    if mode == 'vigenere':
        result = vigenere.decrypt(text, key)
    elif mode == 'vernam':
        result = vernam.decrypt(text, key)
    else:
        return jsonify({'error': 'Invalid mode'}), 400

    return jsonify({'plain': result})

if __name__ == '__main__':
    app.run(debug=True)
