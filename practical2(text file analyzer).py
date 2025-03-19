
#TO OPEN AND READ TEXT FILES
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = read_file('sample.txt') #testing
print(content[:100])  # Print the first 100 characters



# TO COUNT NUMBER OF LINES
def count_lines(content):
    return len(content.split('\n'))

num_lines = count_lines(content)#testing
print(f"Number of lines: {num_lines}")



#COUNTING WORDS
def count_words(content):
    return len(content.split())


num_words = count_words(content)#testing
print(f"Number of words: {num_words}")



#COUNTING MOST COMMON WORDS
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")



#CALCULATING AVERAGE WORD LENGTH
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")



#MY CODES

#FOR FINDING UNIQUE WORDS

def count_unique_words(content):
    words = content.lower().split()  # Convert to lowercase and split into words
    unique_words = []  # Create an empty list to store unique words

    for word in words:  # Loop through each word
        if word not in unique_words:  # If the word is not already in the list
            unique_words.append(word)  # Add it to the list

    return len(unique_words)  # Return the count of unique words



#FOR LONGEST WORD

def for_longest_word(content):
    words = content.split()  # Spliting the text into words
    longest_word = ""  # Start with an empty longest word
    longest_length = 0  # Start with length 0

    for word in words:  # Loop through each word
        if len(word) > longest_length:  # If this word is longer than the current longest
            longest_word = word  # Update the longest word
            longest_length = len(word)  # Update the longest length

    return longest_word, longest_length  # Return the result


# TO FIND SPECIFIC WORD

def count_specific_word(content, target_word):
    words = content.lower().split()  # Convert to lowercase and split into words
    target_word = target_word.lower()  # Convert target word to lowercase
    count = 0  # Start the count at 0

    for word in words:  # Loop through each word
        if word == target_word:  # If the word matches the target word
            count += 1  # Increase the count

    return count  # Return the total count

# percentage of word longer than average word length
def percentage_long_words(content):
    words = content.split()  # Split text into words
    avg_length = average_word_length(content)  # Get the average word length
    long_word_count = 0  # Counter for words longer than average
    total_words = len(words)  # Total number of words

    for word in words:  # Loop through each word
        if len(word) > avg_length:  # If word is longer than average
            long_word_count += 1  # Increase the counter

    percentage = (long_word_count / total_words) * 100  # Calculate percentage
    return percentage  # Return the percentage






#ALLTOGETHER (MAIN FUNCTION)
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    #MY CODES
    num_unique_words = count_unique_words(content)
    longest_word, longest_length = for_longest_word(content)
    long_word_percentage = percentage_long_words(content)
    
    
    
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
   
   
   #MY CODES
    print(f"Number of unique words: {num_unique_words}") 
    print(f"Longest word: '{longest_word}' ({longest_length} characters)") 
    
    target_word = input("Enter a word to count: ")
    word_count = count_specific_word(content, target_word)
    print(f"The word '{target_word}' appears {word_count} times in the text.")
    print(f"Percentage of words longer than average: {long_word_percentage:.2f}%")


analyze_text('sample.txt')
