def binare_search (list,item):
    low = 0
    nigh = len(list)-1

    while low <=nigh:
        mid = int((low + nigh)/2)
        guess = int(list[mid])
        if guess == item:
            return mid
        if guess > item:
            nigh = mid - 1
        else:
            nigh = mid + 1
    return "тут такого нет ("

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binare_search(my_list, 5)) # => 4
print(binare_search(my_list, -1)) # => "тут такого нет ("