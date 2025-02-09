#variables

fruit = "apple"
print(fruit)


#math operators

print(5 + 5)
print(10 - 5)
print(5 ** 2)
print(10/2)
print(20//5)


#if/else

score = int(input("enter your score:"))

if score < 50:
    print("you failed a test!")
else:
    if score >= 50:
        print("congrats, you passed the test!")



#for loop

fruit = "strawberry"

for i in fruit:
    print(i)


#while loop

count = 100
while count > 0:
    print(count)
    count -= 1


#string functions

word = "goa"

print(word.upper())


sentence = "GOA iS ThE bEsT!"

print(sentence.lower())


#list functions

values = ["cat", "dog", "hamster"]

print(values[1])

print(values[0] + values[2])

values[2] = "cow"

values += ["aligator"]

print(values)
