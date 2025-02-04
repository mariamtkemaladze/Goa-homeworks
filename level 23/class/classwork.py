#1
def math_operations(x, y):
    print(f"ჯამი (+): {x + y}")
    print(f"გამოკლება (-): {x - y}")
    print(f"გამრავლება (*): {x * y}")
    print(f"გაყოფა (//): {x // y}")

x = int(input("შეიყვანეთ x რიცხვი: "))
y = int(input("შეიყვანეთ y რიცხვი: "))

math_operations(x, y)


#2

def greet_user(name):
    print(f"გამარჯობა {name}, კეთილი იყოს შენი მობრძანება, გისურვებ წარმატებას და წინსვლას!")

user_name = input("გთხოვთ შეიყვანოთ თქვენი სახელი: ")

greet_user(user_name)



#3

def love_letter(name):
    letter = f"""
საყვარელო {name},

მიყვარხარ პაწ (სასიყვარულო ტექსტი ცხოვრებაში არდამიწერია ბოდიში დდ;)

სიყვარულით {name}
"""
    print(letter)

user_name = input("გთხოვთ შეიყვანოთ თქვენი სახელი: ")

love_letter(user_name)















