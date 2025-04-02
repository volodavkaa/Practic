import hashlib
import random

# Генерація випадкового числа
random_number = random.getrandbits(128)
print("Випадкове число:", random_number)

# Хешування MD5
hash_md5 = hashlib.md5(b'Hello World').hexdigest()
print("MD5:", hash_md5)

# Хешування SHA-1
hash_sha1 = hashlib.sha1(b'Hello World').hexdigest()
print("SHA-1:", hash_sha1)