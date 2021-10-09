from random import randint, choice

vowels = "aeiouyåä"


def random_vowel():
    return choice(vowels)


def random_consonant():
    return choice("bcdðfghjkĸlmnpqrsštvwxz")


def random_repeat(element):
    if randint(0, 1) == 0:
        return ""
    return random_repeat(element) + element()


def random_start():
    return (
        random_repeat(random_consonant)
        + random_vowel()
        + (random_vowel() if randint(0, 2) == 0 else "")
    )


def random_non_start():
    return random_consonant() + random_start()


def random_end():
    return random_repeat(random_non_start) + random_repeat(random_consonant)


def random_swap_pair():
    st1, st2 = random_start(), random_start()
    end1, end2 = random_end(), random_end()
    sp = " " + random_repeat(lambda: " ")
    return (st1 + end1 + sp + st2 + end2, st2 + end1 + sp + st1 + end2)


def random_swapped_sentence():
    if randint(0, 3) == 0:
        return random_swap_pair()
    if randint(0, 2) == 0:
        word = random_start() + random_end()
        return (word, word)
    s1, s2 = random_swapped_sentence()
    w1, w2 = random_swap_pair()
    sp = " " + random_repeat(lambda: " ")
    return (w1 + sp + s1, w2 + sp + s2)


def generate_swaps():
    for i in range(30):
        yield random_swapped_sentence()
