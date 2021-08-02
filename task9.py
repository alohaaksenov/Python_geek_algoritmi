list_numbers = input('Введите 3 числа x,y,z: ').split(',')
list_numbers = [int(x) for x in list_numbers]
list_numbers.sort()
print('Среднее число {}'.format(list_numbers[1]))
