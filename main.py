def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    lowered_text = text.lower()
    characters = {}

    for letter in lowered_text:
        if letter.isalpha():
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1

    return characters

def dict_to_list(dictionary):
    character_list = []

    for letter in dictionary:
        character_list.append({ "letter": letter, "count": dictionary[letter] })

    return character_list

def sort_on(dict):
    return dict["count"]

def main():
    book_path = "books/frankenstein.txt"

    book_contents = read_book(book_path)
    words_count = count_words(book_contents)
    characters_count = count_characters(book_contents)
    characters_list = dict_to_list(characters_count)
    characters_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print("")
    for letter in characters_list:
        print(f"The '{letter['letter']}' character was found {letter['count']} times")
    print("--- End report ---")

main()
