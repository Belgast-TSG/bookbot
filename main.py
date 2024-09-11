def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    print(text)
    print(f"{words} in document")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)
main()