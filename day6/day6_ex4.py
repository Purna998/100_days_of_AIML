# Write and Read a List of Items

def writeItemToFile(filename,items):
    with open(filename,"w") as file:
        for item in items:
            file.write(item+"\n")
def readItemsFromFile(filename):
    try:
        with open(filename,"r") as file:
            items=file.readlines()
            print("Items in the file:")
            for item in items:
                print(item.strip())

    except FileNotFoundError as e:
        print(f"Error: {e}")

fruits=["Apple","Banana","Cherry","Dates"]
writeItemToFile("fruits.txt",fruits)
readItemsFromFile("fruits.txt")