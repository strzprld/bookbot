def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        text = f.read()
    print (word_count(text))
def word_count(text): # Count the number of words in a string
            return len(text.split())

main()

