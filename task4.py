import random

number_range = input('Для получения случайного числа, введите диапазон чисел от x до y в формате x,y: ').split(',')
rand_int = random.randint(int(number_range[0]), int(number_range[1]))
print('Случайное целое число: {}'.format(rand_int))

uni_range = input('Для получения случайного вещественного числа, введите диапазон чисел от x до y в формате x,y: ').split(',')
rand_uni = random.uniform(float(uni_range[0]), float(uni_range[1]))
print('Случайное вещественное число: {}'.format(rand_uni))

char_range = input('Для получения случайного символа, введите диапазон символов от x до y в формате x,y: ').split(',')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

a = chars.index(char_range[0])
b = chars.index(char_range[1])

rand_uni = random.choice(chars[a:b])
print('Случайное вещественное число: {}'.format(rand_uni))
