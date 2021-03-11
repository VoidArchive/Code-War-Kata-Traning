# In this kata you are required to, given a string, replace every
# letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    new_string = ""
    text = text.lower()
    index = 0
    while index < len(text):
        item = text[index]
        if ord(item) > ord("z") or ord(item) < ord("a"):
            index += 1
            continue
        new_string += str(ord(item)-ord("a") + 1) + " "
        index += 1

    return new_string[:-1]
# Internet Solution


def alphabet_position_iS(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


print(alphabet_position("Hello"))
