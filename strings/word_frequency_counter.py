'''Clean Word Frequency Counter

Write a function count_words(paragraph) that takes a string paragraph and returns a dictionary. 
> The keys of the dictionary must be the unique words found in the text, and the values must be the number of times each word appears.
> Constraints & NotesThe count must be case-insensitive (e.g., "Python" and "python" are the same word).
> You must strip out standard punctuation marks: ., ,, !, ?, -, ;.Words should be separated by standard whitespace.

Example 1: Text with punctuation and capitalisation
Input: "Python is great, and coding in Python is fun!"
Output: {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'coding': 1, 'in': 1, 'fun': 1}

Example 2: Repeated single words separated by punctuation
Input: "Help! Help me, please.
"Output: {'help': 2, 'me': 1, 'please': 1}Example 3: Empty text inputInput: ""Output: {}
'''

def count_words(paragraph):
    # Remove basic punctuation and lower the case
    for punctuation in [".", ",", "!", "?", "-", ";"]:
        paragraph = paragraph.replace(punctuation, "")
    
    words = paragraph.lower().split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count


text_sample = input("Enter the string: ")
print(count_words(text_sample))

# Output: 
# Enter the string: Betty bought a Butter, but butter was bitter.              
# {'betty': 1, 'bought': 1, 'a': 1, 'butter': 2, 'but': 1, 'was': 1, 'bitter': 1}