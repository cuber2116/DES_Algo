# Define a function for initial and final permutation
def mapped(num, order):
    bin_num = format(num, '064b')  
    binary_array = [int(i) for i in bin_num]  
    mapped_order = [0] * 64
    for j in range(len(order)):
        mapped_order[j] = binary_array[order[j] - 1]
    return mapped_order
