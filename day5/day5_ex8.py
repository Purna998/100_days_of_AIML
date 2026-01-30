# Write a program to reverse the words in a sentences(not the letters).
import re
def reverseWords(sentence):
    words=re.split(" ",sentence)
    print(words)
    reversed_words_list=[]
    for word in words:
        reversed_word=word[::-1]
        reversed_words_list.append(reversed_word)
        new_sentence=" ".join(reversed_words_list)    
    return new_sentence
input_sentence=input("Enter a Sentence: ")
print(f"The reversed word in sentence: {reverseWords(input_sentence)}")