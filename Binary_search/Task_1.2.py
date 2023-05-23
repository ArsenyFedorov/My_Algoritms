# Предположим размер списка увеличелся вдвое . 
# Как изменится макс количество проверок 
# O(log2 n) => количество поиска увеличется на 1 cтепень двойки
def binar (num):
    search = 0
    while num > 0:
        num//=2
        search +=1
    return search
examination = 128 

print(f"макс количество проверок:{binar(examination)}")
print(f"макс количество проверок:{binar(examination*2)}")