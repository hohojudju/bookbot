def count_words(words):
    words_split = words.split()
    return len(words_split)

def count_characters(words):
    times = {}
    for word in words:
        word = word.lower()
        for character in word:
            if character not in times:
                times[character] = 1
            else:
                times[character] += 1

    return times

def get_num(item):
    return item["num"]

def count_sorted(characters):

    sorted = []

    for char in characters:
        dictio = {"char":char, "num":characters[char]}
        sorted.append(dictio)
    sorted.sort(reverse=True, key=get_num)
    return sorted
