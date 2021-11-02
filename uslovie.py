#решение первой домашней работы, обернутое в классы

def dz_01(a):
    if (int(a)<100) or (int(a)>999) :
        print("ВВеденное число не удовлятворяет условию")
    elif (a[0] == '0')or(a[0] == '9')or(a[1] == '0')or(a[1] == '9')or(a[2] == '0')or(a[2] == '9'):
            #print("Во введенном числе присутствует 0 или 9")
            result = 'ОК'
    else :
        #print("в числе нет 0 или 9")
        result = 'NO'
    return result

def dz_02(P,Q):
    if Q <= P:
        #print("Зачем работать то в убыток?")
        result = 'NaN'
        return result
    else:
        day = 0
        while P < Q:
            P += P * 0.03
            day += 1
        #print("Через ", day, "дней сумма составит ", int(P), " рублей.")
        return int(P)

count = 0
def dz_2(a,b):
    global count
    if (a > 0) and (b > 0):
        re_kvadrat(a,b)
    else:
        #print ('На таких значениях квадрата не построишь!')
        count = 0
    return count

def re_kvadrat(a,b):
    global count
    if b > a:
        b -= a
        count += 1
        #print (count, '-й квадрат, с ребром :',a)
        return re_kvadrat(a,b)
    elif a == b:
        count += 1
        #print(count, '-й последний квадрат, с ребром :', a)
        #return print('Итого, количество квадратов: ', count)
    else:
        a -= b
        count += 1
        #print(count, '-й квадрат, с ребром :', b)
        return re_kvadrat(a, b)


# chislo = str(input("Введите трехзначное число: \n"))
# print(dz_01(chislo))
# P = float(input("Введите сумму выручки: \n"))
# Q = int(input("Введите максимальное значение: \n"))
# print(dz_02(1000,2000))
# st_a = int(input("Введите сторону А: \n"))
# st_b = int(input("Введите сторону В: \n"))
# print(dz_2(st_a,st_b))

