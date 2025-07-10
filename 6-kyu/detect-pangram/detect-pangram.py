def is_pangram(st):
    char_count = [0] * 26
    
    for char in st.lower():
        if "a" <= char <= "z":
            char_count[ord(char) - ord("a")] += 1     
    
    for count in char_count:
        if count == 0:
            return False
    
    return True