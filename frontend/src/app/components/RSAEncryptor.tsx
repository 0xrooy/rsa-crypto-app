'use client'
import { useState } from "react"
import axios from "axios"

export default function RSAEncryptor() {
  const [text, setText] = useState("")
  const [cipher, setCipher] = useState("")
  const [decrypted, setDecrypted] = useState("")
  const [privateKey, setPrivateKey] = useState("")
  const [publicKey, setPublicKey] = useState("")

  async function handleEncrypt() {
    try {
      const res = await axios.post("http://localhost:8000/encrypt", { text })

      setCipher(res.data.cipher)
      setPrivateKey(res.data.private)
      setPublicKey(res.data.public)

      const decryptedRes = await axios.post("http://localhost:8000/decrypt", {
        private: res.data.private,
        cipher: res.data.cipher,
      })
      setDecrypted(decryptedRes.data.text)
    } catch (err) {
      console.error("Error:", err)
    }
  }

  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">🔐 RSA Cryptography Demo</h1>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="border p-2 w-full"
        placeholder="Enter text to encrypt"
      />
      <button
        onClick={handleEncrypt}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Encrypt + Decrypt
      </button>
      <div className="space-y-2">
        <p><strong>Cipher:</strong> {cipher}</p>
        <p><strong>Decrypted:</strong> {decrypted}</p>
        <pre className="break-words whitespace-pre-wrap">
          <strong>Private Key:</strong>{'\n'}{privateKey}
        </pre>
        <pre className="break-words whitespace-pre-wrap">
          <strong>Public Key:</strong>{'\n'}{publicKey}
        </pre>
      </div>
    </div>
  )
}
