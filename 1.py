name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth_year = int(input('Введите год рождения: '))
print(name, surname, birth_year)
name, surname = surname, name
print(name, surname, birth_year + 60)
