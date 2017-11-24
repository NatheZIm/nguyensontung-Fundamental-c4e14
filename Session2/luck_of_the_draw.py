from random import *
boss=randint(0,10)
luck=randint(0,3)
intel=randint(0,3)
hit=luck+intel
if hit < boss:
    print("Né nhẹ nè ! ")
else:
    print("Hự !! ")
