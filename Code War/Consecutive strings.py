# You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string
# consisting of k consecutive strings taken in the array.

def longest_consec(strarr, k):

    x = len(strarr)
    longest = index = 0
    if x == 0 or k > x or k <= 0:
        return ""
    for i in range(x - k + 1):
        length = sum([len(s) for s in strarr[i: i + k]])
        if length > longest:
            longest = length
            index = i
    return ''.join(strarr[index: index + k])

    # Internet best solution


def longest_consec_is(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s

    return result
