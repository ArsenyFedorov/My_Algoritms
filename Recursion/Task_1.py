# Написать код для функции sum(cm,выше)
def sum_list(num_list: list) -> int:
    if len(num_list) == 1:
        return num_list[0]
    return num_list.pop(0) + sum_list(num_list)
my_list = [1,2,3,6,4,6]
print(sum_list(my_list))

