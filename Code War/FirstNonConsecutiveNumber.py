

array = [1, 2, 3, 4, 6, 7, 8]


def fnc(arr):
    for x, y in enumerate(arr, arr[0]):
        if x != y:
            return y


fnc(array)
