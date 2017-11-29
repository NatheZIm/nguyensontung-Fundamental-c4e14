from random import *
num = randint(1,50)
print(num)
wrong =True
count=0;
print("You only have 5 guess ! ")
while wrong and count < 5:
    n = int(input("Guess a number from 1 to 50 : "))
    count += 1
    if n < num:
        print("you need a bigger number ")
    elif n > num:
        print("You need a smaller number")
    else:
        print("We have a winner ! ")
        wrong = False
    if count == 4:
        print("1 last chance !")
    elif count==5:
        print("The number is ",num)
        print("YOU LOSE !! ")
