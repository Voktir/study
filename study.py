# print(" погнали шпацувати")
# a = input()

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(a))
# a = a.replace ('a' + 'b', '')
# print(a)

# message = "rr r"
# search = "r"
# result = 0
# result = int(result)
# for c in message:
#     result -= c == "r"
#     print(result)
# #    (c == "r") and (result += 1)
# print('')
# print(result)

# s = "s"
# r = 1
# print(id(r))
# r = int(r)
# print(id(r))
# r += "1" and s == "s"
# print(id(r))
# print(type(r))
# print(r)

# s = "s"
# r = 0
# r = int(r)
# r = (r + 10 + 10) and s == "s"
# print(r)

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool / quantity
#     print (chunk)
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# def greeting(): print("Hello /world!")
# greeting()

# def invite_to_event(username):    
#     return f"Dear {username}, we have the honour to invite you to our event"
# username = "XXX"
# print(invite_to_event(username))

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price *= (1-discount)
#     apply_discount()
#     return price

# price = 100
# discount = 0.3
# print(discount_price(price, discount))

#(middle_name := (" " + middle_name) if middle_name else "")
#= f" {middle_name}" if middle_name else ""

    #space = ""
    # if middle_name:        
    #space = f" {middle_name}" if middle_name else ""

# def get_fullname(first_name, last_name, middle_name = ""):
#     space = f" {middle_name}" if middle_name else ""
#     return f"{first_name}{space} {last_name}"

# print(get_fullname("Віктор", "Кожем'яка", "Валерійович"))

# def get_fullname(first_name, last_name, middle_name = ""):
#     return f"{first_name}{f" {middle_name}" \
#     if middle_name else ""} {last_name}"

# def get_fullname(first, last, middle = ""):
#     f"{first}{(" "+middle) if middle else ""} {last}"

# print(get_fullname("1", "3", "2"))



# print(add_numbers(5, 10))  # Виведе: 15

# words = ["banana", "apple", "cherry"]
# words.sort(key=len)
# print(words)  # Виведе ['apple', 'banana', 'cherry'

# def format_string(string, length):
#     if len(string) < length:
#         return f"{"*" * ((length - len(string)) // 2)}{string}"
#     else: pass
#     return string

# print(format_string("123", 11))

# def first(size, *args):
#     # for arg in args:
#     #     size += 1
#     return size + len(args)
# # print(first(5, "first", "second", "third"))
# # print(first(1, "Alex", "Boris"))
# def second(size, **kwargs):
#     return size + len(kwargs)
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def number_of_groups(n, k):
#     return int(factorial(n)/((factorial(n-k))*factorial(k)))

# print(number_of_groups(8, 7))

# import datetime
# now = datetime.datetime.now()
# print(now.year)

# from datetime import datetime
# print(datetime.now().year)

# from datetime import timedelta
# delta = timedelta(
#     days=1,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29,
#     minutes=5,
#     hours=8,
#     weeks=0
# )
# print(delta)

# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)

# print('He said, "Hello"')

# cars = [
#     {"car": "Ford", "year": 2005},
#     {"car": "Mitsubishi", "year": 2000},
#     {"car": "BMW", "year": 2019},
#     {"car": "VW", "year": 2011},
# ]


# def get_key(element):
#     return element["year"]


# print(cars)

# cars.sort(key=get_key)

# print(cars)

# import re

# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())
#     print("Електронна адреса:", match.group())

# import re

# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)

# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)

# import re

# text = "Python - це %_° 34534 проста5345, але 345потужна мова програмування."
# pattern = r"\w+"
# matches = re.findall(pattern, text)

# print(matches)

# import re

# text = "apple#banana!!mango@orange;kiwi!!"
# pattern = r"[#@;!]+"
# fruits = re.split(pattern, text)

# print(fruits)

from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')  
    except ValueError:
        return 0
    today = datetime.today()
    delta = today - date
    return delta.days

print(get_days_from_today('2024-04-23'))

