# name = input("Enter your name")
# age = int(input("Enter age"))
# licence = int(input("Enter number your licence"))
# if name and age >= 18 and licence >= 1:
#     print(f"user {name} can rent a car")

# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# x = int(input("X: "))
# y = int(input("Y: "))
# if x >= 0:
#     if y >= 0:
#         print("First quarter")
#     else:
#         print("Fourth quarter")
# else:
#     if y >= 0:
#         print("Second quarter")
#     else:
#         print("Third quarter")

# pets = ["dog", "fish", "cat"]

# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")

# some_iterable = ["a", "b", "c"]

# for i in some_iterable:
#     print(i)

# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(i ** 2)

""" user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}") """

# k = 0
# while k < 10:
#     k = k + 1
#     print(k, end=" ")

# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

# while True:
#     user_input = input()
#     print(user_input)
#     if user_input == "exit":
#         break
# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break
# 
# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else:
#     is_next = False
# print(is_next)

# developer_type = None
# work_experience = int(input("Enter your full work experience in years: "))
# if work_experience <= 1:
#     developer_type = "Junior"
# elif work_experience <= 5:
#     developer_type = "Middle"
# else:
#     developer_type = "Senior"
# print(developer_type)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while True:
#     if num == 0:
#         break
#     sum = sum + num
#     num = num - 1

# print(sum)

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for letter in message:
#     if letter == "r":
#         result += 1
# print(result)

# for i in range(5):
#     print(i)

# for i in range(1, 7, 2):
#     print(i)

# some_list = ['apple', 'banana', 'cherry']
# for index, value in enumerate(some_list):
#     print(index, value)

# list_1 = ['green', 'ripe', 'red']
# list_2 = ['apple', 'cherry', 'tomato']
# for number, letter in zip(list_1, list_2):
#     print(number, letter)

# numbers = {1: 'one', 2: 'two', 3: 'three'}
# for key in numbers.keys():
#     print(key)
# for value in numbers.values():
#     print(value)
# for key, value in numbers.items():
#     print(key, value)

# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"value {val} is not number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")

# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant.")
# except ValueError:
#     print(f"{age} is not a number")

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
#     print(chunk)
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# def say_hello():
#     print('Hello world!')
# say_hello()

""" def print_max(a, b):
    if a > b:
        print(a, 'Максимально')
    elif a == b:
        print( a, 'дорівнює', b)
    else:
        print( b, 'максимально')
print_max (3, 4)
x = 5
y = 7
print_max(x, y)
x = 4
y = 4
print_max(x,y)
a = 9
b = 8
print_max(a,b) """

""" def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів """

# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum
# result = add_numbers(5, 10)
# print(result)

# def greet(name: str) -> str:
#     return f"Hello, {name}!"
# greeting = greet(input("input your name "))
# print(greeting)
    
""" def is_even(num: int) -> bool:
    return num % 2 == 0

check_even = is_even(5)
print(check_even) """

""" def modify_string(original: str) -> str:
    original = "змінено"
    return original

str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)                # виведе: оригінал """

# def modify_list(lst: list) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]

""" def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]
 """
# def string_to_codes(string: str) -> dict:
#     codes = {}
#     for ch in string:
#         if ch not in codes:
#             codes[ch] = ord(ch)
#     return codes
# result = string_to_codes("Hello world!")
# print(result)

# def greeting():
#     print("Hello world!")
# greeting()

""" x = 50
def  func() -> None:
    x = 2
    print('Зміна локального х на', x)
func()
print(x) """

# def outer_func():
#     enclosing_var = "Я змінна в функції, що охоплює"

#     def inner_func():
#         print("Всередині вкладеної функції:", enclosing_var)

#     inner_func()

# outer_func()

""" def greet(name, message='Привіт'):
    print(f'{message}, {name}!')
greet('Олексій')
greet('Марія', message='Добрий день') """

# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', c дорівнює', c)
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)

""" def say(Message, times=1):
    print(Message * times)
say('Hello')
say('World', 5) """

# def real_cost(base: int, discount: float = 0) -> float:
#     return base * (1 - discount)
# price_bread = 15
# price_butter = 50
# price_sugar = 60

# current_price_bread = real_cost(price_bread)
# current_price_butter = real_cost(price_butter, 0.05)
# current_price_sugar = real_cost(price_sugar, 0.07)
# print(f'Нова вартість хліба: {current_price_bread}')
# print(f'Нова вартість масла: {current_price_butter}')
# print(f'Нова вартість цукру: {current_price_sugar}')

""" def print_all_args(*args):
    for arg in args:
        print(arg)
print_all_args(1, 'Hello', True) """

# def concatenate(*args) -> str:
#     result = ""
#     for arg in args:
#         result += arg
#     return result

# print(concatenate("Hello", " ", "world", "!"))

""" def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25) """

# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print("Ключові аргументи:", kwargs)

# example_function(1, 2, 3, name="Alice", age=25)

""" def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3)) """

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))

""" def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5)) """

# def invite_to_event(username):
#     return f'Dear {username}, we have the honour to invite you to our event'
# invite = invite_to_event('Stas')
# print(invite)



""" def discount_price(price, discount):
    def apply_discount():
        nonlocal price
    apply_discount()
    return price * (1 - discount)
result = discount_price(20, 0.1)
print(result) """

# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name:
#         return f"{first_name} {middle_name} {last_name}"
#     else:
#         return f"{first_name} {last_name}"

""" user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}") """

""" def say(Message, times=1):
    print(Message * times)
say('Hello')
say('World', 5) """

# def format_string(string: str, length: int):
#     space_count = (length - len(string)) // 2
#     if len(string) >= length:
#         return f"{string}"
#     else:
#         return f"{' ' * space_count}{string}"
# result = format_string("Hello", 30)
# print(result)

""" def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "world", "!")) """

# def first(size, *args):
#     result = size + len(args)
#     print(result)
# first(25, 9, 5, 3854)

""" def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result

print(factorial(5)) """

# def factorial(arg):
#     if arg == 1:
#         return 1
#     else:
#         return arg * factorial(arg - 1)
# def number_of_groups(n, k):
#     result = int(factorial(n) / (factorial(n-k) * factorial(k)))
#     return result
# print(number_of_groups(7, 5))

""" num_one, num_two = 0, 1
for _ in range(10):
    print(num_one, end=" ")
    num_one, num_two = num_two, num_one + num_two """

# def sum_args(*args):
#     print(args)
#     sum = 0
#     for value in args:
#         sum += int(value)
#     return sum
# print(sum_args(1, 2, 3, "1000"))

""" def fibonacci(number):
    return number if number == 0 or number == 1 else fibonacci(number-2) + fibonacci(number-1)
print(fibonacci(6)) """


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)
# print(fibonacci(6))

 
""" import datetime
now = datetime.datetime.now()
print(now) """

# from datetime import datetime
# current_datetime = datetime.now()
# print(current_datetime.day)
# print(current_datetime.tzinfo)
# print(current_datetime.time())

""" import datetime
# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)
# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)
print(combined_datetime)  # Виведе "2023-12-14 12:30:15" """

# import datetime
# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7)
# print(specific_date)  # Виведе "2020-01-07 00:00:00"

""" import datetime
# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)
print(specific_datetime)  # Виведе "2020-01-07 14:30:15" """

# from datetime import datetime
# now = datetime.now()
# day_of_week = now.weekday()
# print(day_of_week)

""" from datetime import datetime
# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)
print(datetime1)
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2 """

# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

""" from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0 """

# from datetime import datetime, timedelta
# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)

""" from datetime import datetime
# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)
# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}") """

# from datetime import datetime
# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
# # Поточна дата
# current_date = datetime.now()
# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)

""" from datetime import datetime
now = datetime.now()
timestamp = datetime.timestamp(now)
print(timestamp) """

# from datetime import datetime
# timestamp = 1617183600
# dt_object = datetime.fromtimestamp(timestamp)
# print(dt_object)

""" from datetime import datetime
now = datetime.now()
# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 
# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)
# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)  
# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only) """

# from datetime import datetime
# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"
# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

""" from datetime import datetime
now = datetime.now()
iso_calendar = now.isocalendar()
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
 """

# from datetime import datetime, timezone
# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)
# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC

""" from datetime import datetime, timezone, timedelta
utc_time = datetime.now(timezone.utc)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
print(eastern_time) """

# from datetime import datetime, timezone, timedelta
# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)
# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)  # Виведе час в UTC

""" from datetime import datetime, timezone, timedelta
# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone) """

# import time
# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")

""" import time
current_time = time.time()
print(f"Поточний час: {current_time}")
readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}") """

# import time
# current_time = time.time()
# print(f"Поточний час: {current_time}")
# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}")

""" import time
# Записуємо час на початку виконання
start_time = time.perf_counter()
# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів
# Записуємо час після виконання операції
end_time = time.perf_counter()
# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд") """

# import random
# dice_roll = random.randint(1, 6)
# print(dice_roll) # Повертає ціле число

""" import random
num = random.random()
print(num)
 """

# import random
# fill_percentage = random.random() * 100
# print(f"Заповнення: {fill_percentage:.2f}%")

""" import random
target = random.randrange(1, 11, 2)
print(f"Ціль: {target}") """

# import random
# cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
# random.shuffle(cards)
# print(f"Перемішана колода: {cards}")

""" import random
fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits)) """

# import random
# items = ['яблуко', 'банан', 'вишня', 'диня']
# chosen_item = random.choices(items, k=1)
# print(chosen_item)  

""" import random
numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers) """

# import random
# colors = ['червоний', 'зелений', 'синій']
# weights = [10, 1, 1]
# chosen_color = random.choices(colors, weights, k=1)
# print(chosen_color)  

""" import random
participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}") """

# import random
# price = random.uniform(50, 100)
# print(f"Випадкова ціна: {price:.2f}") # Повертає дійсне число "Випадкова ціна: 64.71"

""" import math
# Вихідне число
x = 3.7
# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини
print(ceil_result, floor_result, trunc_result) """

# import math
# # Використання констант
# print(math.pi)  # Виведе приблизне значення π
# # Тригонометрія
# angle = math.radians(60)  # Конвертація з градусів у радіани
# print(math.sin(angle))  # Синус кута
# # Корінь числа
# print(math.sqrt(9))  # Квадратний корінь з 9
# # Логарифми
# print(math.log(10, 2))  # Логарифм 10 за основою 2

""" print(0.1 + 0.2 == 0.3)  # Це повертає False """
""" print(0.1 + 0.2) # Повертає "0.30000000000000004" """

""" import math
r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True """

# print("Hello my little\rsister")

""" s = "Hi there!"
start = 0
end = 7
print(s.find("er", start, end)) # 5
print(s.find("q")) # -1 """

# s = 'Some words'
# print(s.find("o"))
# print(s.rfind('o'))

# s = 'Some words'
# print(s.index("o"))
# print(s.rindex('o'))

""" text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world'] """

# text = "apple,banana,cherry"
# result = text.split(',')
# print(result)  # Виведе: ['apple', 'banana', 'cherry']

""" list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world' """

""" elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water' """

# clean = '   spacious   '.strip()
# print(clean) # spacious

""" text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) """

# text = "one fish, two fish, red fish, blue fish"
# new_text = text.replace("fish", "bird", 2)
# print(new_text)  

""" print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removesuffix('Hook')) # Test """

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)
# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)

""" user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!") """

# for char in "Hello 123":
#     if char.isdigit():
#         print(f"'{char}' - це цифра")
#     else:
#         print(f"'{char}' - не цифра")

""" intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "This is string example"
print(str.translate(trantab)) """

# intab = "aeiou"
# trantab = str.maketrans('', '', intab)
# str = "This is string example"
# print(str.translate(trantab))

""" symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]
MAP = {}
for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c
result = "34 DF 56 AC".translate(MAP)
print(result) """

# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}
# # Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v
# string = "Hello world"
# result = ""
# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)
# print(result)


""" for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s) """

# price = 19.99
# quantity = 3
# total = f"Total: {price * quantity:.2f}"
# print(total)

# price = 19.99
# quantity = 3
# total = price * quantity
# print(f'Total {total:.2f}')

""" width = 5
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}') """

# completion = 0.756
# formatted = f"{completion:.1%}"
# print(formatted)  # Виведе: '75.6%'

# progress = 0.5
# formatted = f"{progress:.0%}"
# print(formatted)

""" import re
text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)
if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено") """

# import re
# text = "Вивчення Python може бути веселим."
# pattern = r"в\w*м"
# match = re.search(pattern, text, re.IGNORECASE)
# if match:
#     print("Знайдено:", match.group())

# """ import re
# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)
# if match:
#     print("Електронна адреса:", match.group()) """


# import re
# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)
# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)

# """ import re
# text = "Рік 2023 був складнішим, ніж 2022, а 20 жовтня 2023 року був мій 41 день народження"
# pattern = r"\d+"
# matches = re.findall(pattern, text)
# print(matches) """

# import re
# text = "Python - це проста, але потужна мова програмування, і тому я вирішив вчити її у 2024 р."
# pattern = r"\w+"
# matches = re.findall(pattern, text)
# print(matches)  # Виведе список всіх слів у рядку

# import re
# text = "Контакти: example1@example.com, example2@sample.org"
# pattern = r"\w+@\w+\.\w+"
# matches = re.findall(pattern, text)
# print(matches)  # Виведе всі знайдені електронні адреси

# import re
# file_name = "Мій документ Python.txt"
# pattern = r"\s"
# replacement = "_"
# formatted_name = re.sub(pattern, replacement, file_name)
# print(formatted_name)  

# """ import re
# text = "Python - потужна, універсальна; мова!"
# pattern = r"[;,\-:!\.]"
# replacement = ""
# modified_text = re.sub(pattern, replacement, text)
# print(modified_text) """

# import re
# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)
# print(formatted_phone)

# import re
# text = "apple#banana!mango@orange;kiwi"
# pattern = r"[#@;!]"
# fruits = re.split(pattern, text)
# print(fruits)

""" from datetime import datetime
iso_date_string = "2023-03-14"
# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso) """

# from datetime import datetime
# today = datetime.today()
# def get_days_from_today(date):
#     given_date = datetime.fromisoformat(date)
#     return today.toordinal() - given_date.toordinal()
# print(get_days_from_today("24-10-02"))

# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")

def get_numbers_ticket(min, max, quantity):
    import random
    if min >= 1 and max <=1000 and min < quantity < max:
        return random.sample(range(min, max), quantity)
    else:
        return []

print(get_numbers_ticket(1, 89, 7))


from datetime import datetime
today = datetime.today()
def get_days_from_today(date):
    try:
        given_date = datetime.fromisoformat(date)
        return int(today.toordinal() - given_date.toordinal())
    except ValueError:
        return "The date is not correct"
print(get_days_from_today("07-10-2024"))

