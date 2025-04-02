def lcg(seed):
    a, c, m = 16807, 0, 2**31 - 1
    return (a * seed + c) % m

# Реалізація MD5
class MD5:
    def __init__(self):
        self.a, self.b, self.c, self.d = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    def left_rotate(self, x, c):
        return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

    def hash(self, message):
        pass

def main():
    print("Виберіть алгоритм:")
    print("1 - Генерація випадкових чисел (LCG)")
    print("2 - Хеш-функція (MD5)")
    choice = input("Ваш вибір: ")

    if choice == '1':
        seed = int(input("Введіть початкове значення (seed): "))
        random_number = lcg(seed)
        print("Згенероване псевдовипадкове число:", random_number)
    elif choice == '2':
        message = input("Введіть повідомлення для хешування: ")
        md5 = MD5()
        hash_value = md5.hash(message)
        print("MD5 хеш:", hash_value)
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()