# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:42:58 2019

@author: LOGYKAL
"""
import random
import time


def randomisingNumber():
    rand = random.randrange(0, 50)
    return rand


continuing = True
balance = 100
while continuing == True:
    print('You have ' + str(balance) + '$ in your account\n')
    nbChoice = input(
        'Hi, please choose a number between 0 and 49 included:\nThe peer numbers are red and the odd numbers are black\n')
    while int(nbChoice) < 0 or int(nbChoice) > 49:
        print("Your number isn't between 0 and 50\n")
        nbChoice = input('Please choose a number between 0 and 49 included:\n')
    nbChoice = int(nbChoice)
    amount = input('How much do you want to bet?\n')
    while balance < int(amount):
        print("You don't have enought money, you have " + str(balance) + '$\n')
        amount = input('How much do you want to bet?\n')
    amount = int(amount)
    balance -= amount
    print('Rolling the dice (a very big dice)\n')
    randNb = randomisingNumber()
    for i in range(13):
        print('░')
        time.sleep(0.04)
    if nbChoice == randNb:
        print('Congratulation, your number is won! You won ' +
              str(int(amount)*3) + '$\n')
        balance += amount*3
        print('Your balance is equal to ' + str(balance) + '$\n')
    else:
        print('Sorry! You choose the wrong number\n')
    if nbChoice % 2 ==  randNb % 2:
        print('The two numbers have the same color! You won ' +
              str(int(amount)*0.5) + '$\n')
        balance += amount*0.5
        print('Your balance is equal to ' + str(balance) + '$\n')
    else:
        print('Try again and may the luck be with you! ↔YODA↔')
    response = input(
        "Do you want to try again?\nIf yes, enter 'yes' else press enter.\n")
    if response == 'Yes':
        continuing = True
    else:
        continuing = False
