""""" Используется python 3.6
Нет вложенных циклов и сложных изменяемых типов данных.
Программа находит максимум числа. Изначально максимум- это первое число. Если входное число равно локальному максимуму, то к счетчику максимума прибавляется один.
Если найден новый максимум, то счетчик максимума становится равен 1.
k- счетчик максимума
m-максимум
N- кол-во чисел"""""
N=int(input())
m= None
k= 0
for i in range(N):
    a= int(input())
    if m is None:
        m= a
    else:
        if a>m:
            m= a
            k= 1
        elif a==m:
            k+=1
print(k)