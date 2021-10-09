from random import randint, choice


def random_numbers(n):
    return [randint(1, 99) for _ in range(randint(0, n))]


def extend_toplevel_zero(tree, mind, maxd):
    return ([0] + tree + [0], 1, 1 if maxd is None else maxd)


def extend_toplevel_nonzero(tree, mind, maxd):
    return (random_numbers(3) + tree + random_numbers(3), mind, maxd)


def embed_toplevel(tree, mind, maxd):
    return (
        [tree],
        None if mind is None else mind + 1,
        None if maxd is None else maxd + 1,
    )


def embed_toplevel_imbalance(tree, mind, maxd):
    return (
        [tree] + random_numbers(3) + [[tree]],
        None if mind is None else mind + 1,
        None if maxd is None else maxd + 2,
    )


def generate_zero_trees():
    tree, mindepth, maxdepth = [], None, None
    tree_trans = [
        extend_toplevel_zero,
        extend_toplevel_nonzero,
        embed_toplevel,
        embed_toplevel_imbalance,
    ]
    for i in range(30):
        tree, mindepth, maxdepth = choice(tree_trans)(tree, mindepth, maxdepth)
        yield (tree, [mindepth, maxdepth])
