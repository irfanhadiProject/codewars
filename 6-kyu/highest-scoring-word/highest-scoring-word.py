def high(x):
    words = x.split()
    
    high_score = 0
    high_word = ""
    
    for word in words:
        score = 0
        for letter in word:
            score += ord(letter) - ord('a') + 1
        if high_score < score:
            high_score = score
            high_word = word
    
    return high_word
    
    