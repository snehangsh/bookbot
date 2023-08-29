
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"********** Begin report of {book_path} **********")
    num = get_number_words(text)
    print(f"{num} words found in the document")
    #count = get_number_words(text)
    count = get_count_letters(text)
    ls = list(count.items())
    ls.sort()
    for char in ls:
        print(f"The '{char[0]}' character was found {char[1]} times")
    print("********** End Report **********")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_words(text):
    str = text.split()
    return len(str)

def get_count_letters(text):
    dict ={}
    for char in text:
        if char.isalpha():
            if char.lower() in dict:
                dict[char.lower()] +=1
            else:
                dict[char.lower()] =1
    return dict

main()
