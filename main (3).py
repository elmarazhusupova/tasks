def count_even(lst, c = 0) :
    if not lst:
        return c
    return count_even(lst[1:], c + 1 - lst[0] % 2)