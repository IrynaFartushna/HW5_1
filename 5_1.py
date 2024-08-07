import string
import keyword

def is_valid_variable_name(name):
    if name == '_':
        return True
    if all(char == '_' for char in name):
        return False
    if name[0].isdigit():
        return False
    if any(char.isupper() or char in string.whitespace or char in string.punctuation.replace('_', '') for char in name):
        return False
    if name in keyword.kwlist:
        return False


    return True



user_input = input("Введіть рядок: ")
print(is_valid_variable_name(user_input))