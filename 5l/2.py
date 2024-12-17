import math
def NOD(n1, n2, nod):
    if n1%nod==0 and n2%nod==0:
        return nod
    else:
        return NOD(n1,n2,nod-1)


try:
    n1=int(input("Введите первое число : "))
    n2=int(input("Введите второе число : "))
    if n1>n2:
        nod=n2
    else:
        nod=n1

    if n1<=0 or n2<=0:
        print('Введены не натуральные числа\n')
        exit()
    else:
        nod = NOD(n1, n2,nod)
        print('Через свою функцию - ', nod)
        print('Через функцию math - ', math.gcd(n1,n2))
except:
    print('Неверный ввод.')
    exit()


    

    
