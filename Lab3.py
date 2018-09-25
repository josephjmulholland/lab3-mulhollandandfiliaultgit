#programmers: Joe Mulholland and Ian Filiault
#Course: CS151 Dr. Kenyon
#Date: September 25th 2018
#Lab Assignment: Lab 3
#Problem Statement: Finding if a ski jump had enough points to pass based on the distance traveled and velocity, along with type of jump.
#Data In: Type of jump and velocity
#Data out: Distance, points,and if user had enough points or not
#Credits: none for this assignment

#imports math functions for use in the program
import math

#welcomes user to program and collects inputs
print("Welcome to the program! This program will tell you if you have enough points to pass, as well as your distance, based upon your sprcific ski jump.")
print("What is the velocity of the jump?")
velocityString = input()

print("What type of ramp are you on?")
rampType = input()

#change input of ramp type into all lowercase as well as changing the velocity into a float
velocity = float(velocityString)

rampTypeLower = (rampType.lower())

#calculate number of points scored/distance traveled if ramp is large
if rampTypeLower == "large":
    timeInAir = math.sqrt(140/9.8)
    distance = timeInAir * velocity
    points = (((distance - 120) * 1.8) + 60)

#calculate number of points scored/distance traveled if ramp is normal
elif rampTypeLower == "normal":
    timeInAir = math.sqrt(92/9.8)
    distance = timeInAir * velocity
    points = (((distance - 90) * 2) + 60)

#says to user how they did based on the amount of points that they scored
if points >= 61:
    print("Great job for doing better than par!")

elif points < 10:
    print("What happened?")

else:
    print("Sorry, you didn't go very far.")

#tells user how far they went and how much they scored
print("You traveled", str(distance), "meters.")
print("You scored", str(points), "points.")