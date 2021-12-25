import secrets
from base64 import b64encode, b64decode
from binascii import unhexlify

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Sinh ngau nhien IV
iv = secrets.token_hex(16)
key = "3e83b13d99bf0de6c6bde5ac5ca4ae68"
pText = "mynameisbuidanhtungdeptrai"

print(f"IV: {iv}")
print(f"Key: {key}")
print(f"Plain Text: {pText}")

# chuyen chuoi hex ve dang binary
iv = unhexlify(iv)
key = unhexlify(key)

# Encode và Padding 
print("pText-encode : ",pText.encode())
pText = pad(pText.encode(), AES.block_size)
print("after-padding : ",pText)

# Encipher chuoi
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = cipher.encrypt(pText)


# Encode Cipher_text as Base 64 and decode to String
out = b64encode(cipher_text).decode('utf-8')
print(f"Cipher Text: {out}")


#####DECRYPTION##########

# Decipher ban ma
decipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = decipher.decrypt(b64decode(out))

# UnPadding
plaintext = unpad(plaintext, AES.block_size).decode('utf-8')
print(f'Plain Text: {plaintext}')

