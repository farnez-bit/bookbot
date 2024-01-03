def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    char_sorted_list = chars_dict_to_sorted_list(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for char_obj in char_sorted_list:
        char = char_obj["char"]
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {char_obj["num"]} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    counter = {}
    for char in text:
        new_char = char.lower()
        if new_char in counter:
            counter[new_char] += 1
        else:
            counter[new_char] = 1
    return counter

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({
            "char": char,
            "num": char_dict[char]
        })
    sorted_list.sort(key=sort_by_num, reverse=True)
    return sorted_list

def sort_by_num(char_obj):
    return char_obj["num"]


main()
