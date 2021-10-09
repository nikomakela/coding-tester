from random import randint


def deepsize(ls):
    if not isinstance(ls, list):
        return 1
    return sum(deepsize(e) for e in ls)


def add_tag_at(tree, place, tag):
    localplace, left, prev = 0, place, place
    while left > 0 and localplace < len(tree):
        prev = left
        left -= deepsize(tree[localplace])
        localplace += 1
    pre, post = tree[:localplace], tree[localplace:]
    if left == 0:
        if randint(0, 1) == 0 and len(post) > 0 and isinstance(post[0], list):
            return pre + [add_tag_at(post[0], 0, tag)] + post[1:]
        return pre + [[tag] if randint(0, 1) == 0 else tag] + post
    pre, point = pre[:-1], pre[-1]
    if not isinstance(point, list):
        return pre + [point, tag] + post
    return pre + [add_tag_at(point, prev, tag)] + post


def generate_flatten():
    result, inp = [], []
    for tag in range(30):
        yield (inp, result)
        place = randint(0, len(inp))
        inp = inp[:place] + [tag] + inp[place:]
        result = add_tag_at(result, place, tag)
