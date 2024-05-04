def roman_to_int(s):
    # Словарь для соответствия римских цифр и их значений
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Проверка на корректность входной строки
    if not s or any(char not in roman_values.keys() for char in s):
        return None

    result = 0
    prev_value = 0

    # Перебираем римские цифры справа налево
    for char in s[::-1]:
        curr_value = roman_values[char]
        if curr_value < prev_value:
            result -= curr_value
        else:
            result += curr_value
        prev_value = curr_value

    return result
n = input('Введите римскую цифру(число): ')
print(roman_to_int(n))
