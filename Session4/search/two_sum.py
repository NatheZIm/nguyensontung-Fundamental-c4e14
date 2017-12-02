base = [0,1,3,5,8,4,-1,-3,-4,9,8]
found = False
for i in range(0,len(base)-1):
    x1 = base[i]
    x2=0
    for j in range(1,len(base)):
        if x1 + base[j] == 0:
            x2=base[j]
            print(x1,x2)
            found=True
            break
if found == False:
    print("Not found")
