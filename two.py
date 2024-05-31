from random import randint

def rand_list(arr):
    n = randint(0, len(arr) - 1)
    deleted_num = arr.pop(n)
    return deleted_num

if __name__ == '__main__':
    a = [randint(0, 1001) for _ in range(10)]
    a.sort()
    deleted_num = rand_list(a)
    print(f'Начальный массив: {a} \nУдаленное число: {deleted_num}')
