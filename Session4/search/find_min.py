base = [9,6,-99,4,8,9]
little=base[0]
for i in range(len(base)):
    if base[i]<little:
        little = base[i]
print("Min :",little)
