def swapFileData():
    firstFile = input("Enter the first file name: ")
    secondFile = input("Enter the second file name: ")

    with open(firstFile, "r") as f1:
        data_a = f1.read()

    with open(secondFile, "r") as f2:
        data_b = f2.read()

    with open(firstFile, "w") as f1:
        f1.write(data_b)

    with open(secondFile, "w") as f2:
        f2.write(data_a)

swapFileData()