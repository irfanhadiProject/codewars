def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    
    result = []
    max_length = 0
    max_length_index = 0
    
    for i in range(len(strarr) - k + 1):
        concat_str = "".join(strarr[i:i+k])
        result.append(concat_str)
    
    for res in result:
        if len(res) > max_length:
            max_length = len(res)
            max_length_index = result.index(res)
    
    return result[max_length_index]