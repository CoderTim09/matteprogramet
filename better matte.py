#imports
from random import randint
import os

#functions!

def pluss(Rundor = 3):
    Rundor_gjorda = 0
    rätta = 0
    while Rundor > Rundor_gjorda:
        num1, num2, answer = randomize_nums("+", 1, 100)

        choice = input(f"{num1} + {num2} = ")
        choice = int(choice)

        rätta = checka_ifall_rätt(choice, answer, rätta)
        
        Rundor_gjorda += 1
    print(f"{rätta} / {Rundor}") 


def minus(Rundor = 3):
    Rundor_gjorda = 0
    rätta = 0
    while Rundor > Rundor_gjorda:
        num1, num2, answer = randomize_nums("-", 1, 100)
        choice = input(f"{num1} - {num2} = ")
        choice = int(choice)

        rätta = checka_ifall_rätt(choice, answer, rätta)
        
        Rundor_gjorda += 1
    print(f"{rätta} / {Rundor}") 


def multiplikation(Rundor = 3):
    Rundor_gjorda = 0
    rätta = 0
    while Rundor > Rundor_gjorda:
        num1, num2, answer = randomize_nums("*", 1, 10)
        choice = input(f"{num1} * {num2} = ")
        choice = int(choice)

        rätta = checka_ifall_rätt(choice, answer, rätta)
        
        Rundor_gjorda += 1
    print(f"{rätta} / {Rundor}") 


def division(Rundor = 3):
    Rundor_gjorda = 0
    rätta = 0
    while Rundor > Rundor_gjorda:
        num1, num2, answer = randomize_nums()

        while answer % 1 != 0:
            num1, num2, answer = randomize_nums()

        choice = input(f"{num1} / {num2} = ")
        choice = int(choice)

        rätta = checka_ifall_rätt(choice, answer, rätta)
        
        Rundor_gjorda += 1
    print(f"{rätta} / {Rundor}") 

def randomize_nums(räknesätt, from1 = 1, to2 = 100):
    num1 = randint(from1,to2)
    num2 = randint(from1,to2)

    if räknesätt == "+":
        answer = num1 + num2
    elif räknesätt == "-":
        answer = num1 - num2
    elif räknesätt == "/":
        answer = num1 / num2
    elif räknesätt == "*":
        answer = num1 * num2
    else:
        print("you dont make sense!")

    return num1, num2, answer

def checka_ifall_rätt(choice, answer, rätta):
    if choice == answer:
        print("good job")
        rätta+=1
    else:
        print("Wrong!")
    return rätta


def välj(val):
    if val == "add":
        os.system("cls")
        pluss()
    elif val == "sub":
        os.system("cls")
        minus()
    elif val == "mul":
        os.system("cls")
        multiplikation()
    elif val == "div":
        os.system("cls")
        division()
    else:
        print("No!")


# körs
while True:
    välj(input("add, sub, mul, div: "))