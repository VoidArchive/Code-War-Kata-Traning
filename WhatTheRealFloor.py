def get_real_floor(n):
    if n < 0:
        return n
    else:
        return n if n < 13 else n - 2


print(get_real_floor(15))
