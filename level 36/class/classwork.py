#codewars


#task 1

#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"



#task 2 

#Given a non-empty array of integers, return the result of multiplying the values together in order.

def grow(arr):

    result = 1 
    for num in arr:
        result *= num 
    return result