import re
​
def count_smileys(arr):
    pattern = re.compile(r'^[:;][-~]?[)D]$')
    return sum(1 for face in arr if pattern.match(face))