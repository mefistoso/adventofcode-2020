import numpy as np

in_data = np.loadtxt("input")

# brute forcing it
for number in in_data:
    other_number = 2020-number
    if other_number in in_data: 
        print("found it, product is", number*other_number)
        break

# Part 2 - three numbers that sum up 2020
# brute forcing it
# Now I want it to be a common python list
in_data_2 =  list(in_data)
for index, number in enumerate(in_data_2):
    rest_of_numbers =  in_data_2[index+1:]
    for other_number in rest_of_numbers:
        yet_another_number = 2020-(number+other_number)
        if yet_another_number in rest_of_numbers:
            print("Found them: {}, {}, {}".format(number, other_number, yet_another_number))
            print("The product is {}".format(number*other_number*yet_another_number))
            break
