# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *
# for example, a tower of 3 floors looks like below

# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]

def tower_builder(n_floors):
    tower = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        tower.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)

    return tower

# internet solution


def tower_builder_is(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


print(tower_builder(3))
