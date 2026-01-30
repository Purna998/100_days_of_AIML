# Write a program to copy the contents of one file to another

def copyContenttoAnotherFile(source,destination):
    try:
        with open(source,"r") as file:
            content=file.read()
            print(content)

        with open(destination,"w") as file:
            file.write(content)
        print("File copied Successfully.")

    except FileNotFoundError as e:
        print(f"Error: {e}")

copyContenttoAnotherFile("fruits.txt","demo.txt")