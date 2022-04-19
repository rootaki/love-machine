
import random
import time

# love machine <3

print("Welcome to Love Machine Mister, have fun here")
time.sleep(0.7) # in seconds

name1 = str(input("Put your name here: "))
time.sleep(0.6)

name2 = str(input("Put the second name here: "))
time.sleep(0.6)

print("\nOK, Now i'm going to calculate love intensity. ")
time.sleep(1.00)

number = random.randint(1, 100)

print("The percents of love from {} to {} is: {} % ".format(name1, name2, number))

if (number >= 80):
    print(" ")
    print("Oh, wow, great lovers!")

if (number == 100):
    print(" ")
    print("That's incredible! ")

if (number <= 10):
    print(" ")
    print("Oh, not good lovers :( ")

time.sleep(1.00)
print(" ")
input("Press 'Enter' to close. ")
