"""The maximum sum subarray problem consists in finding
the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and
the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum.
Note that the empty list or array is also a valid sublist/subarray."""


def max_sequence(arr):
    sum_arr = []
    for j, e in enumerate(arr):
        sum_arr.append(e)
        for i in range(j + 1, len(arr)):
            e += arr[i]
            sum_arr.append(e)
    if all(i < 0 for i in arr) or not sum_arr:
        return 0
    else:
        max_sum = max(sum_arr)
        return max_sum


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sequence(a))
