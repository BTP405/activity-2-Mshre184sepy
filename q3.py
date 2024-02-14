#3
#Write a Python function wordCount(t) which retrieves data from a text file t
#and returns a dictionary where the keys are unique words in the file, and the
#corresponding values are lists of line numbers where the words are found in the text.'''

def wordCount(t):
    #Reads data from a text file t and returns a dictionary.
    word_dict = {}

    with open(t, 'r') as file:
        # Iterate over each line in the file
        for line_number, line in enumerate(file, start=1):
            # Split the line into words
            words = line.strip().split()

            # Iterate over each word in the line
            for word in words:
                # Removing punctuation and convert to lowercase for uniformity
                word = word.strip('.,!?').lower()

                # If the word is not in the dictionary, add it with a new list
                if word not in word_dict:
                    word_dict[word] = [line_number]
                else:
                    # appending the line number, if the word is already in the dictionary,
                    word_dict[word].append(line_number)

    return word_dict

# testing
text_file = '/Users/shreya/Desktop/BSD/BSDsem4/BTP/A2/count.txt'
result = wordCount(text_file)

#results
for word, line_numbers in result.items():
    print(f"{word}: {line_numbers}")
