def sort_list(characters: list[str]):
    for i in range(len(characters)):
        min = i

        for j in range(i + 1, len(characters)):
            if characters[j] < characters[min]:
                min = j
        characters[min], characters[i] = characters[i], characters[min]
    return characters


def list_strings(word: str):
    list_string = list(word.lower())
    sort_word = sort_list(list_string)
    return sort_word


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return (first_string, second_string, False)

    list_first_string = list_strings(first_string)
    list_second_string = list_strings(second_string)
    first = ''.join(list_first_string)
    second = ''.join(list_second_string)
    return (first, second, list_first_string == list_second_string)
