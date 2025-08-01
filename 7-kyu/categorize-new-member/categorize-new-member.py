def open_or_senior(data):
    result = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result