# In a certain kingdom, strange mathematics is taught at school.
# Its main difference from ordinary mathematics is that the
# numbers in it are not ordered in ascending order,
# but lexicographically, as in a dictionary
# (first by the first digit, then, if the first digit is equal, by the second, and so on).
# In addition, we do not consider an infinite set of natural numbers, but only the first n numbers.

# So, for example, if n = 11, then the numbers in strange mathematics are ordered as follows:

# 1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9.

# Help your students to learn this science: write a function that receives two integer numbers: n (total amount of numbers in strange mathematics) and k (number from sequence) and returns the location of a given number k in the order defined in strange mathematics.

# For example, if n = 11 and k = 2, the function should return 4 as the answer.

# Input: 1 <= n <= 100 000 , 1 <= k <= n.

# Output: position of the number k in sequence of the first n natural numbers
# in lexicographic order. Numbering starts with 1.
# lexorder = [1, 10, 11,12,13,14,15, 2, 3, 4, 5, 6, 7, 8, 9]

# for i, v in enumerate(lexorder):
#     if v == 2:
#         print(i+1)

# Works But It takes to looooooong
"""Test Results:
Fixed Tests
Fixed Tests Cases (3 of 3 Assertions)
Completed in 0.09ms"""


def strange_math(n, k):
    str_lexorder = []

    for i in range(1, n+1):
        str_lexorder.append(str(i))
        str_lexorder.sort()
    int_lexorder = [int(j) for j in str_lexorder]
    for a, b in enumerate(int_lexorder):
        if b == k:
            return a+1

# i am an idiot


def strange_math2(n, k):
    return sorted(range(n+1), key=str).index(k)


print(strange_math2(15, 15))
