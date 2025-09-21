characters = {}

def get_book_text(filepath1):

    with open(filepath1) as f:
        file_contents = f.read()

    return file_contents

def word_number(asd):
    text = get_book_text(asd)
    words = text.split()
    word_count = 0

    for e in words:
        word_count += 1

    return word_count

def character_count(asd):
    text1 = get_book_text(asd)
    text = text1.lower()
    
    for char in text:

        if char not in characters:
            characters[char] = 1
        elif char in characters:
            characters[char] += 1

    return characters

def sort_on(items):
    return items["num"]

def sort():
    sorted_list = []

    for n in characters:
        dic = {}
        
        if n.isalpha():
            dic["char"] = n
            dic["num"] = characters[n]
        if "char" in dic and "num" in dic:
            sorted_list.append(dic)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


