def main(): # Prints the report of the book
    path = "books/frankenstein.txt"
    text = book_text(path)
    full_report(text,path)
    


def book_text(path): # Read the text from a file
    with open(path) as f: # Opens the file
        return f.read()

def word_count(text): # Count the number of words in a string
        words = text.split() # Split the text into words
        return len(words) # Returns the number of words


def lowercase(text):   # Convert a string to lowercase
    lowercase_text = text.lower()  
    return lowercase_text

def split_to_characters(text): # Split a string into characters
    characters = list(lowercase(text))
    return characters
     
def count_characters(characters): # Count the number of characters in a list
    character_count = {}
    for character in characters:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def full_report(text,path):
   print (f"Beginning report of {path}")
   print(f"{word_count(text)} number of words") # Prints the number of words in the text
   for character, count in count_characters(split_to_characters(text)).items():
         print(f"The {character} was found {count} times")
   return full_report



main() # Calls the main function