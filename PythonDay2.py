print("hello world")
score = 0
score += 1 
print(score)
print("your score is " + str(score))

score = 0
height = 168.0
is_winning = True
print(f"{score} {height} {is_winning}")


print("Welcome to the rollcoaster!")
height = input("What is your height?")
height > 150

if height >= 150:
    print("you are eligible congrats!")
else:
    print("Sorry Grow faster next time")


#Nested if / else

print("welcome to the rollcoaster")
height = int(input("What is your hieght in cm?"))

if hight >= 120:
    print("congrats you are eligible")
else:
    print("Sorry grow faster next time")
    
age = int(input("What is you age?"))
if age <= 18:
    print("You need to pay $12")
elif age <= 12:
    print("you need to pay $5")
else:
    print("you need to pay $15")

# Nested if / else

print("welcome to the rollcoaster")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("congrats you are eligible")

age = int(input("What is you age?"))
if age >= 18:
    bill = 12
    print("You need to pay $12")
elif age <= 12:
    bill = 5
    print("you need to pay $5")

wants_photos = input("Do you want to take a photo? type y for yes and n for no")
if wants_photos == "y":
    bill += 3
    print(f"your total bill is ${bill}")
else:
    print("Sorry grow faster next time")