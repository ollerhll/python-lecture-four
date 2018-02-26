import abstraction_functions

my_list = [1,2,3,4]
print(my_list)
abstraction_functions.append_new_elements(my_list)
abstraction_functions.reverse(my_list)
abstraction_functions.append_n_elements(my_list, 5)
abstraction_functions.reverse(my_list)
new_list = my_list[2:]
abstraction_functions.reverse(new_list)
abstraction_functions.append_new_elements(new_list)
print(new_list)
