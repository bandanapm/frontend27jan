"""
Date : Sep 27th / 23
Topic : Repetition structures
---- 1) Condition control (AKA while loop)
---- 2) Count control (AKA for loops)

Modularization (Module) ---> Menu-driven programming
Basic functions, how import packages.
"""

x = 6
y = 12
# you need to have an update to condition otherwise will repeat
# indefinitely ! (infinite loop)
while y > x:
    print('Hello!')
    x += 1 # x = x + 1
# for loop! --
# for (int i = 0; i < 5 ; i ++)

i = 0
while i < 5:
    i += 1

# for loops : iterator ----> it designed to go through anything iterable
# iterable : its object (Complex(collection) data structure which are
# sequential
name = "Hesam"
for ch in name:
    print(ch)
print('---------------------------')
for number in [1, 2, 3, 4]:
    print('H')
print('------------------------------')
# Range() ---> 3 arg --> start = 0, stop , step = 1
# this loop repeats five times
# start is inclusive [start, stop) , yet stop is exclusive
for i in range(5): #[0,1,2,3,4]
    print('A' , i , sep = '', end= '-')
print('--------------------------------')
for i in range(1,10):
    print('B' , i , sep = '', end= '-')

print('\n--------------------------------')
for i in range(100,-10,-10): # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    print('C' , i , sep = '', end= '-')

# I like to find the sum of all even numbers b/w 1 to 100
# range(start number, calculate part, upto i.e end)

add = 0
for even in range(2,101,2):
    add += even
print()
print(add)

#--------------------------------------------------------------------
# Modularization : breaking down the task into smaller more manageable
# sub - process (AKA function)
# module (function) 1- pre-defined  2) self-defined
# module(function) need to be called in order to process
# def define the function which is to be called later
print()


def message():
    print('Hello my name is')
    print('Hesam')

message()
# ----------------local vs global variables--------------
# passing by value vs passing by reference
# we can use global variables in local scope if there is no local variable
# present?  can I make make a local variable global? yes
# yet is not a good practice
v = 2
def double_value():
    global v
    v = 5
    print(v, end=" ")
    result = v * 2
    print(result, end=" ")

print(v, end = " ")
double_value()
print(v, end = " ")
print()

v = 1
def demo():
    v = 2
    def demo2():
        nonlocal v
        v = 3
        print(v, end = " ")
    def demo3():
        global v

        v = 4
        print(v, end=" ")
    print(v, end=" ")
    demo2()
    print(v, end=" ")
    demo3()
    print(v, end=" ")
print(v, end = " ")
demo()
print(v, end = " ")

# -------------------------------------------------------------
#import math
from math import factorial as fac
print('\n')

print(fac(5))

# guessing game, which user can guess a random number b/w 1 to 100 and
# the program provides the user a feedback, if user_input < rand_number :
# guess something bigger , and user_input > rand_num ,guess something smaller
# program provides the number of guesses
from random import randint
def game():
    rand_num = randint(1,100)
    counter = 0
    while True:
        user_input = int(input('Enter your guess b/w 1 to 100: '))
        counter += 1
        if user_input > rand_num:
            print('Guess something smaller!')
        elif user_input < rand_num:
            print('Guess something bigger!')
        else:
            print(f'the game is over it took you {counter} to guess!')
            break

# how do we make this game 2 player?

def twoPlayers():
    p1name = input('Enter the player 1 name : ')
    p2name = input('Enter the player 2 name : ')
    # how to I randomize the start player
    # how do I keep track of the turns
    if randint(0, 1):
        turn = p1name
    else:
        turn = p2name
    rand_num = randint(1,100)
    while True:
        user_input = int(input(f' {turn} Enter your guess b/w 1 to 100: '))
        if user_input > rand_num:
            print('Guess something smaller!')
        elif user_input < rand_num:
            print('Guess something bigger!')
        else:
            print(f'the game is over {turn} is the winner!')
            break
        # I have to switch the turn
        if turn == p1name:
            turn = p2name
        else:
            turn = p1name


twoPlayers()