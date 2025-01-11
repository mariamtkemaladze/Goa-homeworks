score = input("enter your score:")

if score > 90:
    print("A")

elif score > 80 and score < 89:
    print("B")

elif score > 70 and score < 79:
    print("C")

elif score > 60 and score < 69:
    print("D")

elif score < 60:
    print("F")




    age = input("enter your age:")

    if age < 13:
        print("child")

    elif age > 13 and age <19:
        print("teenager")

    elif age > 20:
        print("adult")




        number = input("enter number:")
        

        if number == 0:
            print("zero")

        elif number > 0:
            print("positive number")

        elif number < 0:
            print("nehative number")