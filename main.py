def main(): # Read the text from the file and print the number of words
    path = "books/frankenstein.txt"
    text = book_text(path)
    print(f"{word_count(text)} number of words")   # Prints the number of words


def book_text(path):                        # Read the text from a file
    with open(path) as f: # Opens the file
        return f.read()

def word_count(text): # Count the number of words in a string
        words = text.split() # Split the text into words
        return len(words) # Returns the number of words


def lowercase(text):                # Convert a string to lowercase
    lowercase_text = text.lower()  
    return lowercase_text
 




main() # Calls the main function

