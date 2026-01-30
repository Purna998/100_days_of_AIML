# Count words and lines in a File
def count_words_and_lines(filename):
    try:
        with open(filename,"r") as file:
            lines=file.readlines()
            line_count=len(lines)
            word_count=0
            for line in lines:
                word_count=word_count+len(line.split()) #sum(len(line.split()))
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

count_words_and_lines('sample.txt')