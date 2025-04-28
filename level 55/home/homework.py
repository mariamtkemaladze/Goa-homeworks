#codewars

#1

#You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.You can assume all values in the array are numbers.

#def small_enough(array, limit):
    #for num in array:
        #if num > limit:
            
            #return False
    
    #return True


#2

#Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.[10, 343445353, 3453445, 3453545353453] should return 3453455.

#def sum_two_smallest_numbers(numbers):
    #first_num = min(numbers)
    #numbers.remove(first_num)
    #second_num = min(numbers)
    
    #return first_num + second_num


#3

#You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.


