chars = 'abcdefghijklmnopqrstuvwxyz'

char_range = input('Введите диапазон символов от a до z в формате x,y: ').split(',')
print(char_range)
a = chars.index(char_range[0]) + 1
b = chars.index(char_range[1]) + 1

c = b - a

print('Первая буква: {} - находится на {} позиции,\
      вторая буква {} - находится на {} позиции.\
      Расстояние между ними {}'.format(char_range[0], a, char_range[1], b, c))
