def spin_words(sentence):
    # Your code goes here
    formatted_words = []
    
    for word in sentence.split():
        if len(word) >= 5:
            formatted_words.append(word[::-1])
        else:
            formatted_words.append(word)
        
    
    formatted_sentence = " ".join(word for word in formatted_words)
    return formatted_sentence