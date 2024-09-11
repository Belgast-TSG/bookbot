def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = count_characters(text)
    print(text)
    print(f"{words} in document")
    print(characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    text_dict = {}
    for c in lowered_text:
        if c in text_dict:
            text_dict[c] += 1
        else:
            text_dict[c] = 1
    return text_dict

main()