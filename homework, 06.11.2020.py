def exercice_1():
    num = int(input("num: "))
    count = int(input("count:"))
    res = 0
    for x in range(count):
        res += num
        print(res)

def exercice_2():
    my_string = input("My string: ")
    length = len(my_string)
    res = 0
    for x in range(length):
        if isvowel(my_string[x]):
            res += 1
    print(res)
def isvowel(my_char):
    if my_char == "A" or my_char == "a":
        return True
    elif my_char == "E" or my_char == "e":
        return True
    elif my_char == "I" or my_char == "i":
        return True
    elif my_char == "O" or my_char == "o":
        return True
    elif my_char == "U" or my_char == "u":
        return True
    else:
        return False

def exercice_3():
    my_list = []
    num_of_elments = int(input("How many elements do you want your list to have: "))
    res = []
    for x in range(num_of_elments):
        element = input("Write the element that you want to add: ")
        my_list.append(element)
    for x in range(num_of_elments):
        if my_list[x].isdigit() == False:
            res.append(my_list[x])
    print(res)

def exercice_4():
    my_num = input("Write your number: ")
    symmetrical = 1
    length = len(my_num)
    middle = int(length/2)
    even = 1
    if length%2 == 1:
        middle += 1
        even = 0
    if even == 1:
        change = 0
        while middle - change != 0:
            if middle - change == middle:
                if my_num[middle] == my_num[middle + 1]:
                    symmetrical = 1
                else:
                    symmetrical = 0
                    break
            else:
                if my_num[middle - change] == my_num[middle + change]:
                    symmetrical = 1
                else:
                    symmetrical = 0
                    break
            change += 1
    elif even == 0:
        change = 1
        while middle - change != 0:
            if my_num[middle - change] == my_num[middle + change]:
                symmetrical = 1
            else:
                symmetrical = 0
                break
            print(symmetrical)
            change += 1
    print("This is not working. Please help me to solve the problem")


answer = int(input("Which exercice do you want to check: "))
if answer == 1:
    exercice_1()
elif answer == 2:
    exercice_2()
elif answer == 3:
    exercice_3()
elif answer == 4:
    exercice_4()