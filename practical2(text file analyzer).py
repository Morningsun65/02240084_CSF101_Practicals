
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




# MY CODES

#FOR FINDING UNIQUE WORDS

def count_unique_words(content):
    words = content.lower().split()  
    unique_words = []  

    for word in words:  
        if word not in unique_words:  # If the word is not already in the list
            unique_words.append(word)  # Add it to the list

    return len(unique_words) 

"""TO find unique words in the text file, i first made sure all words are lowercased and
split to be read as individual word. then create an empty list. so what will it do with the loop,
it will put words in tec=xt file one after another, and skip the word that is already in the list.
then print the length to show how many words are unique"""

#FOR LONGEST WORD

def for_longest_word(content):
    words = content.split()  
    longest_word = ""  # Start with an empty longest word
    longest_length = 0  # Start with length 0

    for word in words:  
        if len(word) > longest_length:  # If this word is longer than the current longest
            longest_word = word  # Update the longest word
            longest_length = len(word)  # Update the longest length

    return longest_word, longest_length 
"""to find the longest word, we compare it using the length of each word. if the length of the word
is longer than the previous one, it will update the longest word and it keeps on going till
the last word"""

# TO FIND SPECIFIC WORD

def count_specific_word(content, target_word):
    words = content.lower().split()  
    target_word = target_word.lower()  # Convert target word to lowercase
    count = 0  # Start the count at 0

    for word in words:  
        if word == target_word:  # If the word matches the target word
            count += 1  
    return count  

'''to find specific word count, we make the word count to 0 at the beginning, then, we make sure if the word
matches the target word whereby if it matches, we increase the count by 1 and so on till the last word inthe text.
for this we will need to make sure the user puts in a specific word they wanna check for, that will be the target
word that the prompt will search for in the text file'''



# PERCENTAGE OF WORD LONGER THAN AVERAGE WORD LENGTH
def percentage_long_words(content):
    words = content.split()  
    avg_length = average_word_length(content)  
    long_word_count = 0 
    total_words = len(words)  

    for word in words: 
        if len(word) > avg_length: 
            long_word_count += 1 

    percentage = (long_word_count / total_words) 
    return percentage 


'''what it does is split the words in the text file and compare it to the average length. if it is longer
than average length it wil add it to long word count and at last divide by total words times 100 for
percentage'''



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
