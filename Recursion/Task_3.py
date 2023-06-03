# Найти наибольшее число в списке
def max_num(my_list: list) -> int:
    if len(my_list) == 2:
        return my_list[0] if my_list[0] > my_list[1] else my_list[1]
    sub_max = max_num(my_list[1:])
    return my_list[0] if my_list[0] > sub_max else sub_max
my_list = [1,2,3,4,5,6]
print(max_num(my_list))
