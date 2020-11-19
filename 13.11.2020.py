import math

def exercice_1():
    my_string = input("Write your string: ")
    vowels = ["a", "e", "u", "i", "o"]
    res = " "
    for i in my_string.split(" "):
        for j in i:
            if j in vowels:
                for i in range(4):
                    res = res + j
            else:
                res = res + j
        res = res + " "
    print(res)

def exercice_2():
    my_num = int(input("Write your number: "))
    lenght = 0
    num = 1
    while True:
        lenght += 1
        if (my_num / num) <= 1:
            break
        num *= 10
    print(lenght)

def exercice_3():
    my_num = int(input("Write your number: "))
    tymes = 0
    while True:
        tymes += 1
        my_num = math.sqrt(my_num)
        if my_num < 2:
            break
    print(tymes)

def exercice_4():
    my_num = int(input("Write your number: "))
    res = 0
    simple = 1
    for x in range(my_num + 1):
        if x > 1:
            for y in range(2, x):
                if x % y == 0 and y != x:
                    simple = 0
                    break
                else:
                    simple = 1
            if simple == 1:
                res +=  x
    print(res)


answer = int(input("Which exercice do you want to check: "))
if answer == 1:
    exercice_1()
elif answer == 2:
    exercice_2()
elif answer == 3:
    exercice_3()
elif answer == 4:
    exercice_4()