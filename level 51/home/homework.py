#codewars

#1

#The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.


#def open_or_senior(data):
    #result = []
    #for age, handicap in data:
       # if age >= 55 and handicap > 7:
           # result.append("Senior")
       # else:
           # result.append("Open")
    #return result

#data = [(56, 10), (60, 5), (54, 8), (30, 12)]
#print(open_or_senior(data))


#2

#You might know some pretty large perfect squares. But what about the NEXT one?Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

#def find_next_square(sq):

    #root = sq ** 0.5
    
    #if root.is_integer():
         #return (int(root) + 1) ** 2
    #else:
        #return -1


#3

#Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

#def row_sum_odd_numbers(n):
    #first_num = (n * (n - 1)) + 1

    #total_sum = 0
    #for i in range(n):
        #total_sum += first_num + 2 * i 
    
    #return total_sum


#4

#In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?

#def nb_year(p0, percent, aug, p):
    #years = 0
    #while p0 < p:
     #   p0 += p0 * (percent / 100) + aug
      #  p0 = int(p0)  
     #   years += 1
    #return years


#print(nb_year(1500, 5, 100, 5000)) 
#print(nb_year(1500000, 2.5, 10000, 2000000))  

#5

#In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.The string has a length greater or equal to one and contains only letters from ato z.

#def printer_error(s):
    #errors = 0
    #for i in s:
        #if i > 'm': 
            #errors = errors + 1 
    #return str(errors) + "/" + str(len(s))
