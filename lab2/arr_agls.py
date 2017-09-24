#! Нахождение минимума в массиве
def arr_min(arr):
    minx = arr[0]
    for x in arr:
        if x < minx:
            minx = x
    return minx


array = [1, 2, 3]
print(arr_min(array))


#! Нахождение среднего арифметического в массиве
def arr_ave(arr):
    summ = 0
    n = 0
    for x in arr:
        summ += x
        n += 1
    if n != 0:
        return summ / n
    else:
        return "error"


print(arr_ave(array))