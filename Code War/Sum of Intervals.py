# Write a function called sumIntervals/sum_intervals() that accepts an array of intervals,
# and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.


def sum_of_intervals(intervals):
    sum = []
    for i, j in intervals:

        sum += range(i, j)
    return len(set(sum))


a = [
    [1, 4],
    [7, 10],
    [3, 5]
]

print(sum_of_intervals(a))
