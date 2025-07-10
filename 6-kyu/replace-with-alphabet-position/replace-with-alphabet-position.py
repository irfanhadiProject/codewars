def alphabet_position(text):
    numbers = []
    
    for char in text.lower():
        if "a" <= char <= "z":
            numbers.append(ord(char) - ord("a") + 1)
    
    return " ".join(str(num) for num in numbers)