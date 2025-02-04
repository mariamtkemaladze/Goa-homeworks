#1
message = input("enter message:")

correct_message = message.replace('#', ' ')
 
print(correct_message)



#2

name = input("enter your name:")
age = input("enter your age:")

message =f"Hello, {name}! You are {age} years old."

print(message)


#3
list = ", " .join (["python", "is", "fun"])

print(list)



#4


sentence = input("enter a sentence:")

words_list = sentence.split()

print(words_list)




#5

sentence = input("enter a sentence:")

word = input("enter the word to replace:")

new_word = input("enter the new word:")

modified_sentence = sentence.replace(word, new_word)

print(modified_sentence)

