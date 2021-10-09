def generate_fibo():
    a, b = 1, 0
    for i in range(30):
        yield (i + 1, a)
        a, b = a + b, a
