def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list_sorted = sort_dic(chars_dict)
    
   
   
   
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for char in chars_list_sorted:
        print(f"The '{char[0]}' character was found {char[1]} times")

    print("--- End report ---")
    

def sort_dic(dic):
    chars_list = [] 
    for key, val in dic.items(): 
        if key.isalpha():
            chars_list.append([key, val]) 
   
    chars_list.sort(reverse = True, key=lambda a: a[1])
    return chars_list
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()