def sort_list(list_character: list, start: int, end: int):
    if end > start:
        metade = len(list_character) // 2
        primeira_metade = list_character[metade:]
        segunda_metade = list_character[:metade]
        sort_list(primeira_metade, 0, len(primeira_metade) - 1)
        sort_list(segunda_metade, 0, len(primeira_metade) - 1)
    return list_character


def list_strings(word: str):
    list_string = list(word.lower())
    sort_word = sort_list(list_string)
    return sort_word


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return (first_string, second_string, False)

    list_first_string = list_strings(first_string)
    list_second_string = list_strings(second_string)
    return (
        list_second_string,
        list_first_string,
        list_first_string == list_second_string
    )
