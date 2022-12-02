def alphabet_war(fight):
    left_side = {"w": 4, "p": 3, "b": 2, "s": 1}
    right_side = {"m": 4, "q": 3, "d": 2, "z": 1}
    left_score = 0
    right_score = 0
    for i in fight:
        if i in left_side:
            left_score += left_side[i]
        elif i in right_side:
            right_score += right_side[i]
    if left_score > right_score:
        return "Left side wins!"
    elif left_score < right_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"