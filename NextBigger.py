def next_bigger(n):    
    s = list(str(n))
    i = len(s) - 1
    if n < 10 or i == 0:
        return - 1
    