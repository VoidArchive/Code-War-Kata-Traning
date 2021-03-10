# In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer


def square_digits(num):
    # split the number in string
    numbers = list(str(num))
    for number in numbers:
        print(int(number)**2, end="")

def alt_sqd(num):
    return ''.join(str(int(i)**2) for i in str(num))


print(square_digits(9119))
print(alt_sqd(9119))