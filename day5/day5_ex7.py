# Create a program to find and replace all email addresses in a text using regex
import re

def replaceEmail(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    replaced_text = re.sub(email_pattern, "XXXXX@XXX.XX", text)
    return replaced_text

text = input("Enter the sentence: ")
print(replaceEmail(text))
