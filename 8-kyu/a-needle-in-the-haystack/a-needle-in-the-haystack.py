def find_needle(haystack):
    # your code here
    if "needle" in haystack:
        index = haystack.index("needle")
        return f"found the needle at position {index}"