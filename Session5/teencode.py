teen = {
    "ns": "Hành động giao tiếp của con người",
    "cng":"Con người (tên gọi chung của loài người)",
}
loop = True
while loop:
    for key in teen.keys():
        print(key)

    word = str(input("Enter a word :"))
    if word not in teen:
        print("Word not found")
        cont = str(input("You want to add to dictionary ? (Y/N) "))
        if cont == "Y" or cont == "y":
            mean = str(input("Meaning of the word : "))
            teen[word]=mean
    else:
        print(word)
        print(teen[word])
        loop = False
