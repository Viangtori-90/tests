#4 задание под номеров 6
n = int(input('Введите значение числа(/цифры) n='))
if n > 0:
    k = 1
    while n > 1:
        k = k * n
        n = n-1
    print('Факториал введённого числа=', k)
if n==0: print('Факториал нуля = 1')
if n<0:
    print('Вычислить факториал введёного числа невозможно, введите положительное число(/цифру)')
    exit(0)



    
    
