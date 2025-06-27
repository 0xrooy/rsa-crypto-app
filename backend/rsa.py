from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys(bits=2048):
    key = RSA.generate(bits)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    return public_key, private_key

def encrypt_text(public_key_str, plaintext):
    key = RSA.import_key(public_key_str)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext).decode()

def decrypt_text(private_key_str, ciphertext_b64):
    key = RSA.import_key(private_key_str)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = base64.b64decode(ciphertext_b64)
    return cipher.decrypt(ciphertext).decode()
