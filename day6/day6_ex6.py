# #Write a program to counts the number of occurences of a specific words in a text file
# def countWords(filename,target_word):
#     try:
#         with open(filename,"r") as file:
#             lines=file.readlines()
#             words_combined=[]
#             for line in lines:
#                 words=line.split()
               
#                 for word in words:
#                     words_combined.append(word)
            
#         count=0
#         target_word=target_word.lower()
#         for word in words_combined:
            
#             word=word.lower()
#             if target_word==word:
#                 count+=1
#         return count    

#     except FileNotFoundError as e:
#         print(f"Error: {e}")
# target_word=input("Enter the target word: ")
# print(f"The number of occurrences of {target_word} is: {countWords('sample.txt',target_word)}")

def countWords(filename,target_word):
    count=0
    target_word=target_word.lower()
    with open(filename,"r") as file:
        for line in file:
            for word in line.split():
                word=word.lower()
                if word==target_word:
                    count+=1
        return count
target_word=input("Enter the target word: ")
print(f"The number of occurrences of {target_word} is: {countWords('sample.txt',target_word)}")