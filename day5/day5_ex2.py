# Common Strings Methods
#split(), join(), replace(), strip()

# split() Method
sentence="Python is fun"
words=sentence.split(" ")
print(words)

# join() Method - Join the word or character from a list of strings
new_sentence="|".join(words) #Added | in between every words ['Python', 'is', 'fun']
print(new_sentence)

# replace Method - Replace the text, words or character
text="I love Java"
upadated_text=text.replace("Java","Python")
print(upadated_text)

# strip() - Remove whitespaces
messy="   Hello, world  "
print(messy)
cleaned_text=messy.strip()
print(cleaned_text)
