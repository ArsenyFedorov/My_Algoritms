# Написать рекурсивную функцию для потсчёта элементов массива
def count_element(ele_list: list) -> int:
    if ele_list == []:
        return 0
    return 1 + count_element(ele_list[1:])
my_list = [11,3,4,5,6]
print(count_element(my_list))
