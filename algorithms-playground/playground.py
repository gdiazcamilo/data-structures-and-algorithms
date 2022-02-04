
def firstUniqChar(string: str) -> int:
    unique_chars = {}
    repeating_chars = set()
    for idx, char in enumerate(string):
        if char in unique_chars:
            del unique_chars[char]
            repeating_chars.add(char)
        else:
            if char not in repeating_chars:
                unique_chars[char] = idx
    
    for char, idx in unique_chars.items():
        return idx
    
    return -1

print(firstUniqChar('a'))