#задание 7 под номером 6
mas=[]
m=[]
b=[]
p=[]
while len(mas) < 10:
    x = int(input('Введите числа массива(макс. кол-во чисел=10)'))
    mas.append(x)
    #1 задача 
    sr = sum(mas)/ len(mas)
for x in mas:
    if x > sr: b.append(x)
    if x < max(mas): m.append(x)
    #2 задача 
    if x > 5: p.append(x)
print('Задача выполнена.\nСреднеарефметическое заданного массива=', sr, '\nКоличество больших арифметического=', len(b),'\nКоличество меньших максимального=', len(m), '\nКоличество чисел >5=',len(p),', их сумма=',sum(p))
   
    
    