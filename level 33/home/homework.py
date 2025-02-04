#task 1

name = input("Enter your name: ")
age = input("Enter your age: ")

sentence = "Hello, {}! You are {} years old.".format(name, age)

print(sentence)


#task 2

words = ["Python", "is", "fun"]
sentence = " ".join(words)

print(sentence)


#task 3

sentence = input("Enter a sentence: ")

words = sentence.split()

print(words)



#task 4

sentence = input("Enter a sentence: ")

word_to_replace = input("Enter the word to replace: ")

new_word = input("Enter the new word: ")

modified_sentence = sentence.replace(word_to_replace, new_word)

print("Modified sentence:", modified_sentence)


#task 5

mixed_case_string = input("Enter a mixed-case string: ")

lowercase_string = mixed_case_string.lower()

print("Lowercase version:", lowercase_string)


#task 6

sentence = input("Enter a sentence: ")

uppercase_sentence = sentence.upper()

print("Uppercase version:", uppercase_sentence)




