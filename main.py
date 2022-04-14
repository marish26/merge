num = int(input('Введите натуральное число: '))
n = 0
for num in range(1, 10):
    while num != 0:
        if num == num % 10:
            n += 1
            num //= 10
            print('#')
        else:
            print('impossibale')
    break
    print('-')