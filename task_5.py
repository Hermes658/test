import csv


def generate_hash(s: str):
    alfabet = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ '
    d = {l: i for i, l in enumerate(alfabet, 1)}
    p = 67
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


student_with_hash = []
with open('students.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for row in reader:
        row['id'] = generate_hash(row['Name'])
        student_with_hash.append(row)

with open('student_with_hash.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writeheader()
    w.writerows(student_with_hash)
