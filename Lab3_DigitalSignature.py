def sign_message(message, d, n):
    hash_value = int(message) % n
    signature = pow(hash_value, d, n)
    return signature

def verify_signature(message, signature, e, n):
    return pow(signature, e, n) == int(message) % n

def main():
    print("Виберіть дію:")
    print("1 - Підписати повідомлення")
    print("2 - Перевірити підпис")
    choice = input("Ваш вибір: ")

    if choice == '1':
        message = input("Введіть повідомлення: ")
        d = int(input("Введіть секретний ключ d: "))
        n = int(input("Введіть модуль n: "))
        signature = sign_message(message, d, n)
        print("Цифровий підпис:", signature)
    elif choice == '2':
        message = input("Введіть повідомлення: ")
        signature = int(input("Введіть цифровий підпис: "))
        e = int(input("Введіть відкритий ключ e: "))
        n = int(input("Введіть модуль n: "))
        valid = verify_signature(message, signature, e, n)
        print("Підпис дійсний:" if valid else "Підпис недійсний")
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()