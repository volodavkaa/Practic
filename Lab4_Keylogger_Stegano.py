def keylogger():
    log = []
    try:
        print("Натискайте клавіші, для виходу натисніть Ctrl+C")
        while True:
            key = input("Натисніть клавішу: ")
            log.append(key)
            print("Збережено: ", key)
    except KeyboardInterrupt:
        print("Лог клавіш:", ''.join(log))

def embed_lsb(image_path, message):
    with open(image_path, 'rb') as file:
        data = bytearray(file.read())
    binary_message = ''.join(format(ord(c), '08b') for c in message) + '11111111'
    for i in range(len(binary_message)):
        data[54 + i] = (data[54 + i] & ~1) | int(binary_message[i])
    with open('stego_image.bmp', 'wb') as file:
        file.write(data)

def main():
    print("Виберіть дію:")
    print("1 - Клавіатурний шпигун")
    print("2 - Стеганографія")
    choice = input("Ваш вибір: ")

    if choice == '1':
        keylogger()
    elif choice == '2':
        image_path = input("Введіть шлях до зображення (.bmp): ")
        message = input("Введіть повідомлення для приховування: ")
        embed_lsb(image_path, message)
        print("Повідомлення вбудовано в зображення.")
    else:
        print("Невірний вибір!")

if __name__ == "__main__":
    main()