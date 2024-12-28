def pattern(n):
    if n <= 1:
        return ""
    elif n % 2 != 0:
        n -= 1
    table = []
    for num in range(2, n + 1, 2):
        return table.append(str(num)*num)
    return "\n".join(table)
