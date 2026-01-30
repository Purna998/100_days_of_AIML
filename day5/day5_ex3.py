# Regular Expressions
import re

text="Contact me at 123-456-7890"

# search() method
searched_txt=re.search("me",text)
if searched_txt:
    print("Pattern Matched!")
else:
    print("Not Match!")

# findall() method
digits=re.findall(r"\d+",text)
print(digits)

# sub() method
updated_text=re.sub(r"\d","X",text)
print(updated_text)

# split() method - returns a list where the string has been split at each match
txt="The rain in Spain"
x=re.split("\s",txt,1) # This is maxsplit=1(Maximum 1 split)
print(x)