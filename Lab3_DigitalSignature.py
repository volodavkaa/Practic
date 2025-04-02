from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Генерація RSA ключів
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Підписання повідомлення
message = b'Hello digital signature!'
hash_obj = SHA256.new(message)
signature = pkcs1_15.new(key).sign(hash_obj)

# Перевірка підпису
try:
    pkcs1_15.new(key.publickey()).verify(hash_obj, signature)
    print("Підпис вірний")
except (ValueError, TypeError):
    print("Підпис невірний")