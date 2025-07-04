def make_readable(seconds):
    hours = seconds // 3600
    seconds -= hours * 3600
    
    minutes = seconds // 60
    seconds -= minutes * 60
    
    if len(str(hours)) < 2:
        hours = f"0{hours}"
    
    if len(str(minutes)) < 2:
        minutes = f"0{minutes}"
    
    if len(str(seconds)) < 2:
        seconds = f"0{seconds}"
    
    return f"{hours}:{minutes}:{seconds}"
    
    