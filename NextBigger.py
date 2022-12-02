def next_bigger(n):    
    s = list(str(n))
    i = len(s) - 1
    if n < 10 or i == 0:
        return - 1
    while i >= 1 and s[i-1] >= s[i]:
        i -= 1
    if i == 0:
        return -1      
    temp, pos = len(s) - 1, s[i-1]
    