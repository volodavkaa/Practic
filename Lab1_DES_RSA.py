class DES:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        def xor(a, b):
            return ''.join(['1' if x != y else '0' for x, y in zip(a, b)])

        def initial_permutation(block):
            table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
                     62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8]
            return ''.join([block[i - 1] for i in table])

        plaintext = initial_permutation(plaintext)
        for _ in range(16):
            plaintext = xor(plaintext, self.key)
        return plaintext

class RSA:
    def __init__(self, p, q):
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = 65537
        self.d = self.modinv(self.e, self.phi)

    def modinv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def encrypt(self, message):
        return pow(message, self.e, self.n)

    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)

def main():
    print("Виберіть алгоритм:")
    print("1 - DES")
    print("2 - RSA")
    choice = input("Ваш вибір: ")

    if choice == '1':
        key = input("Введіть ключ (8 біт): ")
        plaintext = input("Введіть текст (16 біт): ")
        des = DES(key)
        encrypted = des.encrypt(plaintext)
        print("DES зашифрований текст:", encrypted)
    elif choice == '2':
        p = int(input("Введіть просте число p: "))
        q = int(input("Введіть просте число q: "))
        message = int(input("Введіть повідомлення (число): "))
        rsa = RSA(p, q)
        cipher = rsa.encrypt(message)
        print("RSA зашифрований текст:", cipher)
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()