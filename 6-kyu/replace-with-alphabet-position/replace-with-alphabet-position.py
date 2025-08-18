def alphabet_position(text):
    new_text = "".join(text.split()).lower()
    result = " ".join(str(ord(letter) - ord('a') + 1) for letter in new_text if "a" <= letter <="z")
    
    return result