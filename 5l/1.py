import math
N = input('Введите число   ')
while (not N.isdigit and not (N*(-1)).isdigit):
    N = input('Неправильный ввод. Введите число ещё раз')

Radian=math.radians(float(N))
cosinus = math.cos(Radian)

sinus = 1-cosinus**2
print(f"Cos(x) = {cosinus:.4f}")
print(f"Sin(x) = {sinus:.4f}")
if int(cosinus)==0:
    print("tg(x) не существует")
else:
    tangens=float(sinus)/float(cosinus)
    print(f"tg(x) = {tangens:.4f}")