def append_n_elements(input_list, n):
    for i in range(n):
        new_element = int(input())
        input_list.append(new_element)
    
def append_new_elements(input_list):
    print("How many new elements?")
    number_of_elements = int(input())
    append_n_elements(input_list, number_of_elements)

def reverse(input_list):
    length = len(input_list)
    for i in range(length // 2):
        temp_value = input_list[i]
        input_list[i] = input_list[-(1 + i)]
        input_list[-(1 + i)] = temp_value
