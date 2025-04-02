from Crypto.Cipher import DES, PKCS1_OAEP
from Crypto.PublicKey import RSA

# Генерація ключа RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Шифрування DES
cipher = DES.new(b'8bytekey', DES.MODE_ECB)
encrypted = cipher.encrypt(b'Hello World!   ')

# Дешифрування RSA
cipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted = cipher_rsa.decrypt(encrypted)
print(decrypted)