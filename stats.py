def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lowercase = text.lower()
    cases = {}
    for case in lowercase:
        if case not in cases:
            cases[case] = 0
        if case in cases:
            cases[case] += 1
    return cases

def sort_on(dict):
    return dict["num"]

def sort_num_characters(num_characters):
    sortedlist =[]
    for char in num_characters:
        sortedlist.append({"char":char,"num":num_characters[char]})
    sortedlist.sort(reverse=True, key=sort_on)
    return sortedlist