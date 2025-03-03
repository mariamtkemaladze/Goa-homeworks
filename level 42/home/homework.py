#codewars

#1

#Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise.

#code:
# def set_alarm(employed, vacation):
# return employed==True and vacation==False


#2

#You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.For example, when the input is green, output should be yellow.

#code:

#def update_light(current):
    #if current == "green":
      #  return "yellow"
   # elif current == "yellow":
      #  return "red"
    #elif current == "red":
      #  return "green"

#3

#Complete the function which returns the weekday according to the input number:

#1 returns "Sunday"
#2 returns "Monday"
#3 returns "Tuesday"
#4 returns "Wednesday"
#5 returns "Thursday"
#6 returns "Friday"
#7 returns "Saturday"
#Otherwise returns "Wrong, please enter a number between 1 and 7"


#code:

#def whatday(num):
   # if num == 1:
   #     return "Sunday"
   # elif num == 2:
   #     return  "Monday"
   # elif num == 3:
   #     return "Tuesday"
   # elif num == 4:
   #     return "Wednesday"
   # elif num == 5:
   #     return "Thursday"
   # elif num == 6:
   #     return "Friday"
   # elif num == 7:
   #     return "Saturday"
   # else:
   #     return "Wrong, please enter a number between 1 and 7"