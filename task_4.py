# import csv
# import string
# import random
#
#
# def create_initials(s: string):
#     names = s.split()
#     return f"{names[0]}_{names[1][0]}{names[2][0]}"
#
#
# def create_password():
#     characters = string.ascii_letters + string.digits
#     password = ''.join(random.choice(characters) for _ in range(8))
#     return password
#
#
# students_with_password = []
# with open('students.csv', encoding='utf8') as file:
#     reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
#     for row in reader:
#         row['login'] = create_initials(row['Name'])
#         row['password'] = create_password()
#         students_with_password.append(row)
#
# with open('students_new.csv', 'w', encoding='utf8') as file:
#     w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
#     w.writeheader()
#     w.writerows(students_with_password)
# import csv
# import random
# import string
#
#
# def create_initials(s: string):
#     names = s.split()
#     return f'{names[0]}_{names[1][0]}{names[2][0]}'
#
#
# def create_password():
#     characters = string.ascii_letters + string.digits
#     password = ''.join(random.choice(characters) for _ in range(8))
#     return password
#
#
# students_with_password = []
# with open('students.csv', encoding='utf8') as file:
#     reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
#     for row in reader:
#         row['login'] = create_initials(row['Name'])
#         row['password'] = create_password()
#         students_with_password.append(row)
#
# with open('students_new.csv', 'w', encoding='utf8', newline='') as file:
#     w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
#     w.writeheader()
#     w.writerows(students_with_password)
# import csv
# import string
# import random
#
#
# def create_initials(s: string):
#     names = s.split()
#     return f'{names[0]}_{names[1][0]}{names[2][0]}'
#
#
# def create_password():
#     characters = string.ascii_letters + string.digits
#     password = ''.join(random.choice(characters) for _ in range(8))
#     return password
#
#
# students_with_password = []
# with open('students.csv', encoding='utf8') as file:
#     reader = csv.DictReader(file, delimiter=',', quotechar='"')
#     for row in reader:
#         row['login'] = create_initials(row['Name'])
#         row['password'] = create_password()
#         students_with_password.append(row)
#
# with open('students_new.csv', 'w', encoding='utf8', newline='') as file:
#     w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
#     w.writeheader()
#     w.writerows(students_with_password)
import csv
import string
import random


def create_login(s: string):
    names = s.split()
    return f'{names[0]}_{names[1][0]}{names[2][0]}'


def create_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(8))
    return password


students_with_password = []
with open('students.csv', encoding='utf8') as file:
    reader = csv.DictReader(file, delimiter='', qoutechar='"')
