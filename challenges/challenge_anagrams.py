def same_string(first_list: list, second_list: list):
    for index in len(first_list):
        if first_list[index] != second_list[index]:
            return False

    return True


def sort_list(list_character: list):
    sort_character = []

    for index in len(list_character):
        for lower in sort_character:
            if lower > list_character[index + 1]:
                sort_character.append(list_character[index + 1])

    return sort_character


def list_strings(word: str):
    list_string = list(word.lower())
    sort_word = sort_list(list_string)
    return sort_word


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return ('', '', False)

    list_first_string = list_strings(first_string)
    list_second_string = list_strings(second_string)
    validate = same_string(list_first_string, list_second_string)

    return (list_second_string, list_first_string, validate)
