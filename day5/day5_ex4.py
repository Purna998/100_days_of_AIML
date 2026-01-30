# Create a Text Cleaner
import re
def clean_text(text):
    # Remove Punctuation
    text=re.sub(r"[^\w\s]","",text)
    # Remove extra spaces
    text=" ".join(text.split())
    # Convert to lowercase
    return text.lower()

input_text="  Hello, World.!!! Welcome to Python, Programming..."
cleaned_text=clean _text(input_text)
print("Cleaned Text: ", cleaned_text)