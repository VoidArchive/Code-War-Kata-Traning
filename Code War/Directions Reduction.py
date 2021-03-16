"""Write a function dirReduc which will take an array of strings
and returns an array of strings with the needless directions
removed(W < ->E or S < ->N side by side)."""


def dirReduc(arr):
    direction = {"NORTH": "SOUTH", "SOUTH": "NORTH",
                 "EAST": "WEST", "WEST": "EAST"}
    real_direction = []
    for i in arr:
        if real_direction and direction[i] == real_direction[-1]:
            real_direction.pop()
        else:
            real_direction.append(i)

    return real_direction


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print(dirReduc(a))
