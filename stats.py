# Count words in supplied text
def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

# Create dictionary of character counts
def count_chars(text):
    chars = {}
    for char in text.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sorter(dict):
    return dict["count"]

# Create sorted list of character count dictionaries
def sort_chars(dict):
    l = []
    for item in dict:
        if item.isalpha():
            l.append({"char": item, "count": dict[item]})
    l.sort(key=sorter, reverse=True)
    return l