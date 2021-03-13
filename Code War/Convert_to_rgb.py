
# The rgb function is incomplete. Complete it so that passing
# in RGB decimal values will result in a hexadecimal representation
# being returned. Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.


def rgb(r, g, b):
    def round(x):
        return min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


# How??
def rgb_is(r, g, b):
    def round(x): return min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
