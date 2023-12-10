# # my_str = "Hello this is my string"
# # #Type checking
# # print(type(my_str))
# # #check length of string
# # print(len(my_str))
#
# # reading user input from command line
# # user_input = input("Pleas enter your name: ")
# #
# # print("Hello"+ user_input)
# # print (f"Hello {user_input}")
# #
# # age =input("Enter your age: ")
# #
# # in_a_decade =age +10
# # print(in_a_decade)
# #
# #
# #
# # user_input =input("Please enter a sentence: ")
# # replaced_str=user_input.replace("e","!")
# # print(user_input)
# # print(replaced_str)
#
#
# # sample = "String"
# # sample[0]="r"
# # print(sample[0])
# #
# # array_sample =[0,1,2,3]
# # array_sample[0]=10
# # print(array_sample[0])
#
# # def main():
# #  print("Hello world !")
# #
# # main()
# # current_age = input("Enter your current age: ")
# # years_left = 90 - int(current_age)
# #
# # days_left = years_left * 365
# # weeks_left = years_left * 52
# # months_left = years_left * 12
# #
# # message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
# # print(message)
#
#
# total_living = 90
#
# age = int(input("Enter your age"))
#
#
# def calculate_age(value):
#
#     age = 40
#     return total_living - value
#
#
# def main():
#     remaining = calculate_age(age)
#
#     print(f"You have {remaining} years to live")
#
#
# main()
from turtle import *
from random import randint
import time

speed(10)
penup()
goto(-140, 140)
for step in range(16):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

# add Turtles
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

sag = Turtle()
sag.color('orange')
sag.shape('turtle')

sag.penup()
sag.goto(-160, 70)
sag.pendown()

for turn in range(100):
    ada.forward(randint(1, 5))
    sag.forward(randint(1, 5))
time.sleep(10)
