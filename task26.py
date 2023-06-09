# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def raisApowB(a, b):
    """Возведение А в степень В"""
    if b == 0:
        return 1
    return a * raisApowB(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(raisApowB(a, b))
