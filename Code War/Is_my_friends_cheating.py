# A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
# Within that sequence, he chooses two numbers, a and b.
# He says that the product of a and b should be equal to the sum of all numbers in the sequence,
# excluding a and b.
# Given a number n, could you tell me the numbers he excluded from the sequence?

def remov_nb(n):

    # Did not pass the test. It works but took to long
    res = []
    sum_of_n = sum(range(1, n + 1))

    for i in range(1, n):
        for j in range(i+1, n+1):
            if i*j == sum_of_n - (i+j):
                res.append((i, j))
                res.append((j, i))

    return res

# Passed


def remov_nb_2(n):
    result = []
    sequence_sum = n * (n + 1) // 2
    for x in range(1, n + 1):
        y = (sequence_sum - x) // (x + 1)
        if y <= n and x * y == (sequence_sum - x - y):
            result.append((x, y))
    return result


n = 5

print(remov_nb_2(n))
