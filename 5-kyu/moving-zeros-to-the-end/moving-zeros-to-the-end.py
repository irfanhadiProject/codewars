def move_zeros(lst):
    new_list = []
    for num in lst:
        if num != 0:
            new_list.append(num)
    
    for _ in range(len(lst) - len(new_list)):
        new_list.append(0)
    
    return new_list