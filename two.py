def roman_to_arabic(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_number = 0
    prev_value = 0

    for char in reversed(roman_numeral):
        if char not in roman_values:
            return "Ошибка: Недопустимый символ"

        current_value = roman_values[char]
        if current_value < prev_value:
            arabic_number -= current_value
        else:
            arabic_number += current_value
        prev_value = current_value

    return arabic_number

if __name__ == '__main__':
    roman_numeral = input("Введите римскую цифру (число): ")
    print(roman_to_arabic(roman_numeral))
