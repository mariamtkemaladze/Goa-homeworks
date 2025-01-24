#nums.insert()- es funqcia gvexmareba imashi rom davamatot itemebi listshi.
#nums.remove()- es funqcia gvexmareba listidan itemebis amoshlashi.

#1 homework

fruits = [ "apple", "banana", "cherry", "date", "elderberry" ]

print (fruits)

print (fruits[1] + " " + fruits[-1])

fruits.append("fig")

fruits.remove("banana")

fruits[1] = "blueberry"

print(fruits) #printing renewed list all over again just in case.

print(len(fruits))



#2 homework

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90 ]

nums.append(100)

nums.insert(0, 5)

nums.remove(30)

nums.sort()

nums.reverse()

index_of_50 = nums.index(50)

count_of_20 = nums.count(20)

print(nums)


#3 homework

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_half = numbers[:5]
print("First half:", first_half)

second_half = numbers[5:]
print("Second half:", second_half)

squares = [x**2 for x in numbers]
print("Squares:", squares)
