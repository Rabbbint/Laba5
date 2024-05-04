import random

arr = random.sample(range(1, 1001), 10)

del_index = random.randint(0, 9)

randArr = arr[0:del_index] + arr[del_index+1:]
random.shuffle(randArr)


def findDel(arr, randArr):
    n = len(arr)
    return (arr[0] + arr[n-1])*n/2 - sum(randArr)


res = sum(arr) - sum(randArr)
print("Исходный набор чисел:", arr)
print("Перемешанный набор чисел:", randArr)
print("Удалённое число:", res)
