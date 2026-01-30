try: 
    with open("sample.txt","r") as file:
        content=file.read()
        print(content)
except FileNotFoundError as e:
    print(f"Error: {e}")

#Common File Handling Exceptions
# - FileNotFoundError
# - PermissionError
# - IOError
