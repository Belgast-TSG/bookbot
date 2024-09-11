def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = count_characters(text)
    characters.sort(key=sort_on, reverse=True)
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
        if c.isalpha():
            if c in text_dict:
                text_dict[c] += 1
            else:
                text_dict[c] = 1
    return [{"character": char, "count": count} for char, count in text_dict.items()]

def sort_on(dict):
    return dict["count"]
main()