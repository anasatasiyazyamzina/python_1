##########################################
# 1 слайд
##########################################
# 1 задание
def daysforsomekm(km):
    a = 0
    days = 1
    while a <= km:
        a += 2 ** days
        days = days + 1
    return days


k = 10000
day = daysforsomekm(k)
print("1. Понадобится", day, "дней для", k, "километров")

""" Если задание без функции
a = 0
days = 1
km = 10000
while a <= km:
    a = a + 2**days
    # print("summ a", a)
    days = days + 1
print("1. Понадобится", days, "дней для", km, "километров")
"""
# 2 задание
sledchislo = 10
days = 0
a = 1 + 2 + 3 + 5 + 7  # рассматривается случай, когда a больше суммы первых простых чисел
km = 1000
while a <= km:
    if sledchislo % 2 != 0 and sledchislo % 3 != 0 and sledchislo % 5 != 0 and sledchislo % 7 != 0:
        a += sledchislo
        days = days + 1
        # print("простые числа", sledchislo)
    sledchislo += 1
print("2. Понадобится", days, "день(дней) для", km, "километров")

# 3 задание
km = 10
sum = 1
norm = km
while sum != 30:
    sum += 1
    if sum % 2 != 0:
        norm = norm * 1.15  # увеличиваем норму
        # print("new norm", norm)
    km += norm
    # print("Пробежит за ", sum, "дней км:", km)
print("3. Спортсмен пробежит:", round(km), "км")

# 4 задание (a)
day = 1
norm = 10
while norm <= 20:
    day += 1
    norm = norm * 1.1  # увеличиваем норму
print("4(а). Спортсмен будет пробегать в день больше 20km на", day, "день")

# 4 задание (б)
km = 10
norm = km
days = 1
while km <= 100:
    norm = norm * 1.1  # увеличиваем норму
    km += norm
    days += 1
print("4(б). Спортсмен пробежит в сумме 100 км за:", days, "дней")


##########################################
# 2 слайд
##########################################

# 1 задание
def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


print("2.1 ", fib(7))


# 2 задание
# я больше люблю спорт, чем влгоритмы, так что Трибонначи бегут у меня боком
# в отдельном файле trib


# 3 задание
new_l = [(2*i-1)**2 for i in range(1,8,1)]
print(new_l)

# 4 задание
a = 1
b = 7
# четные
new_l = [i for i in range(a,b,1) if i % 2 == 0]
print("Четные ",new_l)
new_l = [i for i in range(a,b,1) if i % 2 != 0]
print("Нечетные ",new_l)

# 5 задание
a = [1, -1, 3, -5, -6, 4, 5, -8]
b = 7
# четные
new_l = [int(i) for i in a if i >= 0]
print("Положительные ",new_l)
new_l = [int(i) for i in a if i < 0]
print("Отрицательные ",new_l)

##########################################
# 3 слайд
##########################################
def ramOchka(w=12, h=7, f=1, symb="*"):
    for i in range(h):
        if i in range(f) or i in range(h - f, h):
            print(symb * w)
        else:
            print((symb * f) + (" " * (w - f - f)) + (symb * f))
    print()

print("Введите свои значения для рамочки","\nШирина:")
w=int(input())
print("Высота:")
h=int(input())
print("Толщина:")
f=int(input())
print("Символ:")
symb=input()
ramOchka(w, h, f, symb)


# Задание по вариантам
var = len("Анастасия")% 4 + 1
print("Вариант: ",var)


def conNS(x, si1 ,si2):
    he_max = ['','A','B','C','D','E','F']
    x = int(str(x), si1) # Преобразуем по основанию в 10-тичную систему
    b = ''
    if  x % si2 >= 9: # Для 16-тиричной
        b = he_max[x % si2 - 9]
    while x > 0:  # Пока не закончится остаток
        ost = x % si2
        x = x // si2
        if ost > 9: # Для 16-тиричной
            b += he_max[x % si2 - 9]
        else: b += str(ost)

    return b[::-1] # Как при вычислении на бумаге начинаем с конца

chislo = conNS('111', 2, 10)
print("Переводим 111 из 2 в 10: ",chislo)

chislo = conNS('7', 10, 8)
print("Переводим 7 из 10 в 8: ",chislo)

chislo = conNS('9', 10, 8)
print("Переводим 7 из 10 в 8: ",chislo)

chislo = conNS('AA16342F', 16, 8)
print("Переводим AA16342F из 16 в 8: ",chislo)

chislo = conNS('AA', 16, 8)
print("Переводим AA16342F из 16 в 8: ",chislo)
