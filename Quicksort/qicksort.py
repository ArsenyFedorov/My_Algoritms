# Быстрая сортировка
def qicksort(my_list: list) ->list:
    if len(my_list) < 2:
        return my_list
    pivot = my_list[0]
    les = [i for i in my_list[1:] if i < pivot]
    greater = [i for i in my_list[1:] if i > pivot]
    return qicksort(les) + [pivot] + qicksort(greater)
print(qicksort([1,2,6,3,7,6,4,3,62,676]))

