def unique_in_order(sequence):
    unique = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i -1]:
            unique.append(sequence[i])
            
    return unique