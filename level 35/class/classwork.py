#task 1
distance ="7425 miles"
speed = "550 miles/hour"
print("Total flight time:", 7425 / 550, "hours")


#task 2

bill = int(input("enter your bill amount:"))

tip = bill * 20/100

print(tip)


#task 3 


weight = float(input("enter your weight:"))
height = float(input("enter your height:"))
bmi = weight / (height ** 2)

print("underweight" if bmi < 18.5 else "normal weight" if bmi < 25 else "overweight" if bmi < 30 else "obesity")



#task 4

text = input("Enter the text: ")
word = input("Enter the word to search: ")

def search(text, word):

    if word in text:
        return "word found"
    else:
        return "word not found"

result = search(text, word)
print(result)


