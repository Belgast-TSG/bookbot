def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = count_characters(text)
    characters.sort(key=sort_on, reverse=True)
    title, total_words, char_report = generate_report(book_path, words, characters)

    print(title)
    print(total_words + "\n")
    print(char_report)
    

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

def generate_report(path, words, characters):
    title = f"--- Begin report of {path} ---"
    total_words = f"{words} words found in the document"

    char_reports = []

    for i in characters:
        char = i["character"]
        count = i["count"]
        char_count = f"The '{char}' characters was found {count} times"
        char_reports.append(char_count)

    return title, total_words, "\n".join(char_reports)

main()