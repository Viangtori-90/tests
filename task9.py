#задание 9 под номером 6

m=int(input('Введите kол-во строк '))
n=int(input('Введите kол-во стоблцов '))
a = []
for i in range(m):
    b=[]
    for j in range(n):
        print('Введите[',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
print('Исходный массив:')
for i in range(m):
    for j in range(n):
        print(a[i][j], end='')
    print()

for i in range(m):
    for j in range(n):
        if a[i][j]<0:a[i][j]=0
        elif a[i][j]>0:a[i][j]=1
print(a[i],max(a[i]))

for i in range(n):
    x=[x[i] for x in a]
    print(min(x), end=' ')

#2 задача
