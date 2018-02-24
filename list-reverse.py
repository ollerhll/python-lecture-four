def reverse_loop(my_list):
    length = len(my_list)
    for i in range(length // 2):
        temp_value = my_list[i]
        my_list[i] = my_list[-(1 + i)]
        my_list[-(1 + i)] = temp_value
    return my_list

def reverse_recurse(my_list):
    length = len(my_list)
    if length <= 1:
        return my_list
    else:
        reversed_list = reverse_recurse(my_list[1:])
        reversed_list.append(my_list[0])
        my_list = reversed_list
        return my_list

lloyd_list = [7, 5, 7, 3, 2, 4, 1, 2, 6]
print(reverse_loop(lloyd_list))
print(reverse_recurse(lloyd_list))
print(lloyd_list == (reverse_recurse(reverse_loop(lloyd_list[:]))))
