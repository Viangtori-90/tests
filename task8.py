#7 задание, вариант 6

#1 задача
a = int(input('Введите число'))
b = int(input('Введите число'))
if a<=0 or b<=0:print('!!!Необходимо ввести натуральное число!!!')
if a>0 and b>0:
    u=a*b
    while a!=0 and b!=0:
        if a>b: a=a%b
        else: b = b%a
        nod=a+b
        nok = u//nod
print('NOD=', nod, '\nNOK=', nok)

#2
import math
 
def s(p1, p2):
    space1 = math.sqrt(p1*(p1-ab)*(p1-bc)*(p1-ac)) + math.sqrt(p2*(p2-ad)*(p2-cd)*(p2-ac))
 
ab = int (input('Введите длину стороны AB'))
bc = int (input('Введите длину стороны BC'))
cd = int (input('Введите длину стороны CD'))
ad = int (input('Введите длину стороны AD'))
ac = int (input('Введите длину стороны AC'))
 
p1 = (ab + bc + ac) // 2
p2 = (ad + cd + ac) // 2
 
print(s(p1, p2))
