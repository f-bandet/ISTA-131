# Faye Bandet
# Section Leader: Cedric Vicera
# Date : 1/22/2020
# ISTA 131 Hw1
# This model focuses on transversing data structures using Python functions, methods, and operations.

# I shared my code and helped people, but I wrote this code myself. The people who used my code/help
# were William Fusillo and Austin Nebgen.

def is_diagonal(matrix):
    '''
    The function purpose is to return a boolean value whether the argument is a diagonal matrix or not.
    Parameters: matrix, a non-empty list of lists.
    '''
    index = 0
    for lists in matrix:
        for i in range(len(lists)):
            if i != index and lists[i] != 0:
                return False
        index += 1
    return True            
    
def is_upper_triangular(matrix):
    '''
    This Boolean function takes a square, nonempty matrix as its sole argument and returns 
    True if the argument is an upper triangular matrix, False otherwise.  In upper 
    triangular matrices, all elements below the diagonal are zero.
    '''
    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            if num < row:
                if (matrix[row][num] != 0):
                    return False
    return True
      
def contains(matrix, value):
    '''
    This Boolean function takes a matrix, matrix, and a value, value, as its arguments.  It returns True if 
    the value is in the matrix, False otherwise. This is a membership test.
    '''
    for lists in matrix:
        for element in lists:
            if element == value:
                return True
    return False

def biggest(matrix):
    '''
    This function returns the largest value in its sole argument, matrix, a nonempty matrix.
    '''
    number = matrix[0][0]
    for lists in matrix:
        for element in lists:
            if element > number:
                number = element
    return number

def indices_biggest(matrix):
    '''
    This function returns a list containing the indices of the largest value in its sole 
    argument, a nonempty matrix, matrix.  If there is only one element in the matrix, 
    return [0, 0].If there are multiples of the same max value, return the first occurrence going from left 
    to right and then down the matrix.
    '''
    indices = [0,0]
    biggest = matrix[0][0]    
    if len(matrix) == 1 and len(matrix[0]) == 1:  
        return indices
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] > biggest:
                biggest = matrix[row][column]
                indices = [row, column]
    return indices      

def second_biggest(matrix):
    '''
    This function returns the second largest value in its sole argument, a matrix 
    containing at least two elements. If the largest value occurs more than once, it counts as the second 
    largest also.
    '''
    nums = []
    for row in matrix:
        for element in row:
            nums.append(element)
    nums.sort()
    return nums[-2]
   
def indices_second_biggest(matrix):
    '''
    This function returns a list containing the indices of the second largest 
    value in its sole argument, a nonempty matrix. If the largest value occurs 
    more than once, it counts as the second largest also.  If there is only one element in the matrix, return [0, 0].
    '''
    indices = [0,0] 
    nums = []
    if len(matrix) == 1 and len(matrix[0]) == 1:    #means there's one column
        return indices
    for row in matrix:
        for element in row:
            nums.append(element)
    nums.sort()
    secondbiggest = nums[-2]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == secondbiggest:
                indices = [row, column]
                return indices

def substr_in_values(dict1, string):
    '''
    This function takes a dictionary, dict1 that maps keys to lists of strings and a string, string.  
    Return a sorted list of all keys that have an associated value containing a string that case-insensitively 
    contains the second argument.
    '''
    keys = []
    for key, value in dict1.items():
        for i in range(len(value)):
            if string.lower() in value[i].lower():
                keys.append(key)
                break
    keys.sort()
    return keys
    
def indices_divisible_by_3(matrix):
    '''
    This function returns a list containing every element in its argument, matrix, a matrix, that has
    indices whose sum is divisible by three. Traverse by row on your outer loop, column on your inner to get the elements in the correct order.
    '''
    div3 = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (row + col) % 3 == 0:
                div3.append(matrix[row][col])
    return div3
                            
def sort_int_string(string2):
    '''
    This function takes one string parameter, string2. Assume the string will be a series of 
    integers separated by spaces. The empty string or a whitespace string 
    return the empty string.  Otherwise, the function returns a string with the argument’s integers 
    separated by spaces but now in sorted order.
    '''
    nums = []
    if string2 == '':
        return ''
    string2 = string2.split()
    if string2 == []:
        return ""
    for i in string2:
        nums.append(int(i))
    nums.sort()   
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    string3 = " ".join(nums)
    return string3
    
def dups_lol(lol):
    '''
    The argument lol is a list of lists, returns True if the lol contains any value more than once; False otherwise.
    '''
    values = []
    for lists in lol:
        for value in lists:
            if value in values:
                return True
            else:
                values.append(value)
    return False

def dups_dict(dict2):
    '''
    Parameter is dict2, a dictionary that maps keys to lists of values. Return True if any values in 
    the lists occur more than once anywhere in the lists; False otherwise.
    '''
    values = []
    for lists in dict2.values():
        for value in lists:
            if value in values:
                return True
            else:
                values.append(value)
    return False
