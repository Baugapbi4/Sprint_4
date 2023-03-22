import random as random_simbols

def name_of_user():
    name = ''
    for x in range(8):
        name = name + random_simbols.choice(list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                               'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'))
    return name

def lastname_of_user():
    lastname = ''
    for x in range(8):
        lastname = lastname + random_simbols.choice(list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                               'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'))
    return lastname

# def mail():
#     group_number = '_07_'
#     last_name = 'Bartal'
#     number = random_numbers.randint(100, 999)
#     fake_mail = last_name + group_number + str(number) + '@toster.com'
#     return fake_mail
def commentary():
    comment = ''
    for x in range(8):
        comment = comment + random_simbols.choice(list('1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                               'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'))
    return comment

def adress():
    adr = ''
    for x in range(8):
        adr = adr + random_simbols.choice(list('1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                               'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'))
    return adr

def random_phone():
    country_code = '+7'
    operator_code = random_simbols.randint(100,999)
    last_digits = random_simbols.randint(1000000,9999999)
    fake_number = country_code + str(operator_code) + str(last_digits)
    return fake_number

def wrong_phone():
    code = random_simbols.randint(100, 999)
    amount = random_simbols.randint(1000000, 9999999)
    wrong_number = str(code) + str(amount)
    fin = open("data.txt", "a")
    fin.write(wrong_number);
    fin.close()
    return wrong_number
def random_date():
    date = ''
    for x in range(8):
        date = date + random_simbols.choice(list('1234567890'))
    return date