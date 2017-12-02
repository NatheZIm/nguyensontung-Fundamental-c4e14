base = [1,2,3,4,5,6,7,8,9,10]
loop = True
mark = False
found = False
lo = 0
hi = len(base)
while hi > lo:
    mid=(hi+lo) // 2
    guess = int(input("Enter a numer"))
    if guess == base[mid]:
        found=True
        print("Found it ")
        break
    elif guess < base[mid]:
        hi = mid
        print("Left")
        print(lo,hi)
    else:
        lo=mid+1
        print("Right")
        print(lo,hi)
    if not found:
        print("not found")
        break
