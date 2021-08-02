print('введите год:')
year = int(input())

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("не високосный год")
else:
    print("високосный год")
