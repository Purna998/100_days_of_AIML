# File Handling

#Opening Files
# - use the built-in open() function to open a file
# - r | w | a | r+

with open("sample.txt","w") as file: #with make sure file closed automatically and no additional content can occur so, make secure
    # content=file.read()
    # print(content)
    file.write("Hello, World!")
    file.writelines(["Alice","Bob","Cherry"])

#Reading Files
# .read() | .readline() | .readlines()

#Writing to Files
# write() | writelines()
