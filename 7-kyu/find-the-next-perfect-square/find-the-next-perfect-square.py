def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if sq % sq ** 0.5 != 0:
        return -1
    else:
        return (sq ** 0.5 + 1) ** 2
​