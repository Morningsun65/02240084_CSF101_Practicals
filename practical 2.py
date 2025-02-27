# Text File Analyzer

#Step 1: Open and Read a Text File
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
    
# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters

#Step 2: Count the Number of Lines

def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

#Step 3: Count Words

def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

#Step 4: Find the Most Common Word
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

#Step 5: Calculate Average Word Length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

#Step 6: Combine Everything into a Main Function

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')

#Exercises for Students
#Modify the program to count the number of unique words in the text.
#Add a function to find the longest word in the text.
#Implement a feature to count the occurrences of a specific word (case-insensitive).
#Create a function to calculate the percentage of words that are longer than the average word length.