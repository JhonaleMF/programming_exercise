def contiguous_subarray(array):
    ### Complexity of the model is quadratic O(n^2) 
    """Function returns the contiguous subarray with the largest sum.

    Args:
        array (np.array): array to extract the contiguous subarray

    Returns:
        tuple: It returns the subarray selected and the largests sum.
    """
    
    sub_array_sum = array[0]
    sub_array_return = array[0]
    n = 0
    while n < len(array):    
        for i in range(len(array)):
            if n < i + 1:
                if sub_array_sum < sum(array[n: i + 1]):
                    sub_array_sum = sum(array[n: i + 1 ])
                    sub_array_return = array[n: i + 1]     
        n += 1
        
    return sub_array_return, sub_array_sum

 

def contiguous_subarray_LC(array):
    """Function returns the contiguous subarray with the largest sum. Linear complexity O(n)

    Args:
        array (np.array): array to extract the contiguous subarray

    Returns:
        tuple: It returns the subarray selected and the largests sum.
    """
    
    max_sum_array = array[0]
    sub_array_sum = array[0]
    sub_array_sum_backwards = array[-1]
    max_sum_array_backwards = array[-1]

    initial_index = 0
    final_index = 0
    for i in range(1, len(array)):
        sub_array_sum = max(array[i], sub_array_sum + array[i])
        sub_array_sum_backwards = max(array[(i * -1) - 1], sub_array_sum_backwards + array[(i * -1) - 1])
        
        max_sum_array = max(max_sum_array, sub_array_sum)    
        max_sum_array_backwards = max(max_sum_array_backwards, sub_array_sum_backwards)
        
        if sub_array_sum == max_sum_array:
            final_index = i
        if sub_array_sum_backwards == max_sum_array_backwards:
            initial_index = (i * -1) - 1
        
    sub_array_return = array[initial_index: final_index + 1]
        
    return sub_array_return, max_sum_array