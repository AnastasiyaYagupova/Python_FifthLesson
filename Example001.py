a = int(input("Введите число "))
b = int(input("Введите степень числа "))
def degree(a,b):
    if b == 0:
        return 1
    elif b > 0:
        return a * degree(a,b-1)

print(degree(a,b))