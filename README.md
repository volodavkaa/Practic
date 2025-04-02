

## Опис
Цей проєкт містить реалізації лабораторних робіт з курсу криптографії. Основна мета - реалізація алгоритмів симетричного та асиметричного шифрування, генерації псевдовипадкових чисел, цифрового підпису та криптоаналізу.

### Структура проєкту
- `Lab1_DES_RSA.py` - реалізація алгоритмів симетричного (DES) та асиметричного (RSA) шифрування.
- `Lab2_RNG_Hash.py` - генерація псевдовипадкових чисел та хеш-функції (MD5, SHA-1).
- `Lab3_DigitalSignature.py` - реалізація цифрового підпису на основі RSA та приклади криптоаналізу.
- `Lab4_Keylogger_Stegano.py` - реалізація клавіатурного шпигуна та стеганографії методом LSB.

### Запуск проєкту
1. Встановіть необхідні бібліотеки:
```
pip install pycryptodome hashlib numpy opencv-python pyxhook
```

2. Запустіть лабораторну роботу:
```
python3 Lab1_DES_RSA.py
```

### Лабораторна робота №1
**Тема:** Симетричні алгоритми шифрування. DES. Асиметричні алгоритми шифрування. RSA.

#### Опис коду
У цій лабораторній роботі реалізовано два основні алгоритми:
1. **DES (Data Encryption Standard)** - блочний алгоритм симетричного шифрування з використанням 56-бітового ключа. Реалізація здійснюється за допомогою бібліотеки `pycryptodome`, яка дозволяє ефективно шифрувати та дешифрувати файли.
2. **RSA (Rivest–Shamir–Adleman)** - алгоритм асиметричного шифрування на основі факторизації великих простих чисел. Реалізовано генерацію ключів, шифрування та дешифрування текстових файлів.

Код реалізує:
- Генерацію ключів.
- Шифрування та дешифрування файлу розміром не менше 50 КБ.
- Порівняння швидкості роботи алгоритмів.


**Тема:** Симетричні алгоритми шифрування. DES. Асиметричні алгоритми шифрування. RSA.

#### Опис коду
У цій лабораторній роботі реалізовано два основні алгоритми:
1. **DES (Data Encryption Standard)** - блочний алгоритм симетричного шифрування з використанням 56-бітового ключа. Реалізація здійснюється за допомогою бібліотеки `pycryptodome`, яка дозволяє ефективно шифрувати та дешифрувати файли.
2. **RSA (Rivest–Shamir–Adleman)** - алгоритм асиметричного шифрування на основі факторизації великих простих чисел. Реалізовано генерацію ключів, шифрування та дешифрування текстових файлів.

Код реалізує:
- Генерацію ключів.
- Шифрування та дешифрування файлу розміром не менше 50 КБ.
- Порівняння швидкості роботи алгоритмів.

**Тема:** Симетричні алгоритми шифрування. DES. Асиметричні алгоритми шифрування. RSA.

#### Контрольні питання та відповіді:
1. Симетричні алгоритми шифрування використовують один ключ для шифрування та дешифрування.
2. Алгоритм DES працює з 64-бітовими блоками та 56-бітовим ключем.
3. S-блоки - це таблиці підстановок, що перетворюють вхідні біти в інші біти.
4. Довжина ключа в DES - 56 біт.
5. Генерація підключів у DES здійснюється шляхом перестановок та циклічних зсувів.
6. Асиметричні алгоритми використовують два ключі: відкритий для шифрування і закритий для дешифрування.
7. Алгоритм RSA базується на факторизації великих простих чисел.
8. Алгоритм Евкліда знаходить найбільший спільний дільник двох чисел і використовується в RSA для знаходження взаємно простих чисел.
9. Довжина ключів в RSA - від 1024 до 4096 біт.
10. Розподіл ключів передбачає наявність відкритих для шифрування та закритих для дешифрування.

### Лабораторна робота №2
**Тема:** Генератори псевдовипадкових чисел. Хеш-функції. MD5 та SHA-1.

#### Опис коду
У цій лабораторній роботі реалізовано:
1. **Генератори псевдовипадкових чисел** - використовується алгоритм Рабіна-Міллера для перевірки чисел на простоту.
2. **Хеш-функції (MD5 та SHA-1)** - обчислення дайджесту повідомлень.


**Тема:** Генератори псевдовипадкових чисел. Хеш-функції. MD5 та SHA-1.

#### Опис коду
У цій лабораторній роботі реалізовано:
1. **Генератори псевдовипадкових чисел** - використовується алгоритм Рабіна-Міллера для перевірки чисел на простоту. Здійснено генерацію великих простих чисел для криптографічних застосувань.
2. **Хеш-функції (MD5 та SHA-1)** - використовуються для обчислення дайджесту повідомлень. Реалізація на основі бібліотеки `hashlib`, яка забезпечує надійне та швидке хешування файлів.

Код реалізує:
- Генерацію випадкових чисел із перевіркою на простоту.
- Обчислення хешу файлу за алгоритмами MD5 та SHA-1.
- Порівняння швидкості хешування різними алгоритмами.

**Тема:** Генератори псевдовипадкових чисел. Хеш-функції. MD5 та SHA-1.

#### Контрольні питання та відповіді:
1. Хеш-функція - це функція, що перетворює дані довільної довжини у фіксовану.
2. Хеш-функції використовуються для створення цифрових підписів та аутентифікації.
3. Алгоритм SHA-1 створює 160-бітовий хеш.
4. Алгоритм MD5 створює 128-бітовий хеш.
5. SHA-1 більш надійний, оскільки формує довший хеш та складнішу структуру.
6. Випадкові числа генеруються з фізичних джерел, а псевдовипадкові - за допомогою алгоритмів.
7. Генерація псевдовипадкових чисел здійснюється математичними методами.
8. Алгоритм Рабіна-Міллера перевіряє числа на простоту.
9. Джерела випадкових чисел - апаратні генератори шуму.
10. Як ключі можна використовувати великі прості числа.

### Лабораторна робота №3
**Тема:** Аутентифікація даних і цифровий підпис. Криптоаналіз.

#### Опис коду
У цій лабораторній роботі реалізовано:
1. **Цифровий підпис на основі RSA** - створення та перевірка підпису.
2. **Криптоаналіз RSA** - демонстрація атаки на підпис.


**Тема:** Аутентифікація даних і цифровий підпис. Криптоаналіз.

#### Опис коду
У цій лабораторній роботі реалізовано:
1. **Цифровий підпис на основі RSA** - створення підпису та його перевірка. Реалізація на основі генерації RSA ключів та підписання хешу повідомлення.
2. **Криптоаналіз RSA** - демонстрація атак на підпис та методів захисту. Реалізовано приклад атаки з обраним шифротекстом.

Код реалізує:
- Генерацію відкритого та закритого ключа.
- Підписання документа та перевірку підпису.
- Демонстрацію атаки на RSA-підпис.

**Тема:** Аутентифікація даних і цифровий підпис. Криптоаналіз.

#### Контрольні питання та відповіді:
1. Безключове читання RSA передбачає підбір відкритого тексту до шифротексту.
2. Атака на підпис RSA через нотаріуса дозволяє отримати підпис на підроблене повідомлення.
3. Атака по обраному шифротексту дозволяє отримати відкритий текст.
4. Методи ефективні при слабких ключах або неправильній реалізації.
5. Захист - використання довгих ключів та додаткових параметрів підпису.
6. Аутентифікація захищає документи від підробки та несанкціонованого доступу.
7. Електронний підпис - цифровий аналог рукописного підпису.
8. Алгоритми ЕЦП використовують закритий ключ для підпису та відкритий - для перевірки.
9. Накладання ЕЦП - хешування даних та шифрування хешу закритим ключем.
10. Перевірка ЕЦП - розшифрування хешу відкритим ключем та порівняння.

### Лабораторна робота №4
**Тема:** Програмні закладки. Клавіатурний шпигун. Стеганографія.

#### Опис коду
У цій лабораторній роботі реалізовано:
1. **Клавіатурний шпигун** - реєстрація натискань клавіш за допомогою `pyxhook`.
2. **Стеганографія методом LSB** - приховування тексту у BMP зображення.


**Тема:** Програмні закладки. Клавіатурний шпигун. Стеганографія.

#### Опис коду
У цій лабораторній роботі реалізовано:
1. **Клавіатурний шпигун** - програма для перехоплення натискань клавіш. Реалізовано на основі бібліотеки `pyxhook`, що дозволяє реєструвати кожне натискання та зберігати його у файл.
2. **Стеганографія методом LSB** - приховування текстового повідомлення у зображенні формату BMP. Реалізація на основі модифікації найменш значущого біта пікселів.

Код реалізує:
- Реєстрацію натискань клавіш з прив’язкою до активного вікна.
- Вбудовування тексту у зображення та вилучення його назад.
- Збереження результатів шпигунства у лог-файлі.

**Тема:** Програмні закладки. Клавіатурний шпигун. Стеганографія.

#### Контрольні питання та відповіді:
1. Стеганографія приховує факт передачі, криптографія - зміст.
2. Структура BMP-файлу включає заголовок, таблицю кольорів та растровий масив.
3. Метод LSB змінює останні біти пікселів для приховування інформації.
4. Дані LSB можна виявити аналізом спектру бітів.
5. Ускладнення: випадковий розподіл бітів у зображенні.
6. Програмна закладка - прихований код для несанкціонованого доступу.
7. Види закладок: клавіатурні шпигуни, драйверні, замасковані.
8. Реалізація через системні пастки або заміну програмних модулів.
9. Захист: контроль системних процесів, моніторинг API.
10. Методи пошуку шпигунів: сигнатурний, евристичний, моніторинг API.
