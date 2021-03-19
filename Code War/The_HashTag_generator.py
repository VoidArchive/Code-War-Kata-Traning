# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    a = s.title()
    if len(a) > 140:
        return False
    elif a == '':
        return False
    else:
        return "#"+''.join(a.split())


print(generate_hashtag('Bye hi i am programmer'))

# Best solution


def generate_hashtag2(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output
