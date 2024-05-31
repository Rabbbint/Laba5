def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Введите порядковый номер числа Фибоначчи: "))
    print(f"Ваше число: {fibonacci(n)}")

if __name__ == "__main__":
    main()