# Write a program to count the number of vowels in a string
# def countVowels(text):
#     if 
# import re
# text="i want to go"
# count=0
# vowels=re.findall('a|e|i|o|u',text)
# print(vowels)
# for i in vowels:
#     count+=1
# print(count)
import re
def countVowel(text):
    lower_text=text.lower()
    vowels=re.findall('a|e|i|o|u',lower_text)
    print(vowels)
    count=0
    for i in vowels:
        count+=1
    return f"The number of vower letter in text: {count}"
input_text=input("Enter characters or Sentences: ")
print(countVowel(input_text))