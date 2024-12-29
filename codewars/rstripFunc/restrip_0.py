def no_boring_zeros(n):
    if n == 0:
        return 0
    else:
        num1 = str(n)
        num1 = num1.rstrip("0")
        return int(num1)
