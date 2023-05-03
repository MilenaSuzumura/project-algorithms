def sort_list(characters: list[str]):
    for i in range(len(characters)):
        value = characters[i]
        position = i

        while (position > 0) and (characters[position - 1] > value):
            characters[position] = characters[position - 1]
            position = position - 1
        characters[position] = value
    return characters


def is_anagram(first_string, second_string):
    list_first_string = list(first_string.lower())
    list_second_string = list(second_string.lower())

    first = ''.join(sort_list(list_first_string))
    second = ''.join(sort_list(list_second_string))

    if len(first) == 0 or len(second) == 0:
        return (first, second, False)
    
    return (first, second, list_first_string == list_second_string)
