from random import randint

name_list = ['Karol', 'Krzysiek', 'Barbara', 'Sebastian', 'Kacper', 'Gosia']
first_letter_list = [element[0] for element in name_list]
print(first_letter_list)

rand_int_list = [[randint(1, 10) for element in range(4)] for element in range(5)]
print(rand_int_list)