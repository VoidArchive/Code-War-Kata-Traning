# What is an anagram? Well, two words are anagrams of each other
# if they both contain the same letters. For example:


def anagrams(word, words):
    return [w for w in words if sorted(word) == sorted(w)]


# Using Lamda Funtion

def anagrams_is(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)
