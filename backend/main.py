from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rsa import generate_keypair, encrypt, decrypt

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "RSA API up"}

@app.post("/encrypt")
async def encrypt_text(data: dict):
    pub, priv = generate_keypair(61, 53)
    ciphertext = encrypt(pub, data["text"])
    return {"cipher": ciphertext, "public": pub, "private": priv}

@app.post("/decrypt")
async def decrypt_text(data: dict):
    decrypted = decrypt(tuple(data["private"]), data["cipher"])
    return {"text": decrypted}
