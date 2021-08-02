list_lenght = input('Введите длины сторон треугольника через  в формате x,y,z: ').split(',')
a = int(list_lenght[0])
b = int(list_lenght[1])
c = int(list_lenght[2])
print(a, b, c)
if (a > 0) & (b > 0) & (c > 0) & ((a+b) > c) & ((a+c) > b) & ((b+c) > a):
    match = 0
    if a == b:
        match += 1
    if a == c:
        match += 1
    if b == c:
        match += 1
    if match == 3:
        print('Это треугольник равносторонний')
    elif match == 1:
        print('Это треугольник равнобедренный')
    else:
        print('Это треугольник разносторонний')
else:
    print('Это не треугольник')
