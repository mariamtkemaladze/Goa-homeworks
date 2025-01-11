password="group55"
user_pass=''

tries=3
while tries > 0 and user_pass != password:
    user_pass = input("enter password"+ "(you have" + " " + str(tries)+ " " +"tries left:")

tries -= 1

if user_pass == password:
    print("access granted.")
elif tries == 0:
    print("you don't have any tries left")
else:
    print("access denied, try again.")