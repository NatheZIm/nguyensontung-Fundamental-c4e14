base = [3,7,20,2,11,19,96,35,15,64]
mark = False
false_index = -1
loop = True
Guess = int(input("Enter a number : "))
for i in range(len(base)):
    if Guess == base[i]:
        false_index = i+1;
        mark=True
        break
if not mark:
    print("Not found")
else:
    print("Found {0} at index {1}".format(Guess,false_index))
