cath1 = float(input('Введите значение первого катета: '))
cath2 = float(input('Введите значение второго катета: '))
gip = (cath1 ** 2 + cath2 ** 2) ** 0.5
print('Площадь треугольника равна', int(cath1 * cath2 / 2))
print('Периметр треугольника равен', round(cath1 + cath2 + gip, 2))