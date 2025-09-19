def sort_on(items):
    return items["num"]


def count_letters(textstring):
    lower_case_string = textstring.lower()
    character_dictionary = {}
    for character in lower_case_string:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary


def count_words(textstring):
    return len(textstring.split())


def sort_letters(character_dictionary):
    sorted_list = []
    for key, value in character_dictionary.items():
        sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
