# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b))
# that checks whether the two arrays have the "same" elements, with the
# same multiplicities. "Same" means, here,
# that the elements in b are the elements in a squared, regardless of the order.


def comp(array1, array2):
    if array1 and array2:
        return sorted([x*x for x in array1]) == sorted(array2)
    return array1 == array2 == []

# Easy solution using try except


def comp_is(array1, array2):

    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [
      121, 14641, 20736, 361, 25921, 361, 20736, 361]))
