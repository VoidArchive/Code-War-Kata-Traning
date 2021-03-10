
# Usually when you buy something, you're asked whether your credit card number, phone number or
# answer to your most secret question is still correct. However, since someone could look over
#  your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.


# return masked string
def maskify(cc):
    code = ''
    if len(cc) > 4:
        code += "#" * (len(cc)-4) + cc[-4:]
    else:
        return cc
    return code

# List Compression


def maskify_lc(cc):
    return '#'*(len(cc)-4) + cc[-4:]
