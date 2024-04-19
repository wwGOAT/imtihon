def tub():
    for num in range(2, 10001):
        is_tub = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_tub = False
                break
        if is_tub:
            yield num


tub_son = list(tub())

print(tub_son)