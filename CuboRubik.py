def cube(n):
    pass
    res = ''
    for i in range(1, n * 2 + 1):
        row = ''
        if i <= n:
            row += '/\\' * i + '_\\' * n
            dist = n - i
        else:
            row += '\\/' * (n * 2 - i + 1) + '_/' * n
            dist = i - n - 1
        if 2 * n - i:
            row += '\n'
        res += dist * ' ' + row