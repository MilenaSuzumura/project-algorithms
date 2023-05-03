def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    else:
        if word[high_index] != word[low_index]:
            return False

        if low_index >= high_index:
            return True

        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
