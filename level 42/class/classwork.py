#codewars

#1

#The wide-mouth frog is particularly interested in the eating habits of other creatures.He just can't stop asking the creatures he encounters what they like to eat. But, then he meets the alligator who just LOVES to eat wide-mouthed frogs!When he meets the alligator, it then makes a tiny mouth.Your goal in this kata is to create complete the mouth_size method this method takes one argument animal which corresponds to the animal encountered by the frog. If this one is an alligator (case-insensitive) return small otherwise return wide.

#code:

#def mouth_size(animal): 
    #if animal.lower() == 'alligator':
     #   return 'small'
   #  else:
      #  return 'wide'


#2

#Clock shows h hours, m minutes and s seconds after midnight.Your task is to write a function which returns the time since midnight in milliseconds.

#code:

#def past(h, m, s):
   # return 3600000 * h + 60000 * m + 1000 * s


#42 part 2 classwork

#1

#Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

#def replace_exclamation(st):
    #  return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


#2

#Given an array of integers.Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.If the input is an empty array or is null, return an empty array.


#def count_positives_sum_negatives(arr):
 #   if not arr: return []
 #   pos = 0
   # neg = 0
  #  for x in arr:
    #      if x > 0:
        #          pos += 1
      #  if x < 0:
       #     neg += x
   # return [pos, neg]