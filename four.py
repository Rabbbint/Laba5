def is_alphabetical(words):
    if not words:
        return True

    sorted_words = [sorted(word) for word in words]

    for i in range(len(sorted_words) - 1):
        if sorted_words[i] != sorted_words[i + 1]:
            return False

    return True


def main():
    words = input("Введите слова через пробел: ").split()
    print(is_alphabetical(words))


if __name__ == "__main__":
    main()