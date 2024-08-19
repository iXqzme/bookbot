def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = count_characters(text)
    char_list = [{"character": char, "count": count} for char, count in characters.items()]
    char_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for item in char_list: 
        print(f"The '{item['character']}' character was found {item['count']} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_characters(text):
    lowered_string = text.lower()
    char_count = {}
    for char in lowered_string:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(dict_item):
    return dict_item["count"]

main()
