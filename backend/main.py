from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rsa import generate_keys, encrypt_text, decrypt_text

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

@app.post("/encrypt")
async def encrypt_route(data: dict):
    public_key, private_key = generate_keys()
    cipher = encrypt_text(public_key, data["text"])
    return {
        "cipher": cipher,
        "public": public_key,
        "private": private_key
    }

@app.post("/decrypt")
async def decrypt_route(data: dict):
    decrypted = decrypt_text(data["private"], data["cipher"])
    return { "text": decrypted }
