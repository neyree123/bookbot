def get_word_count( text ):
    return len(text.split())

def get_character_counts( text ):
    char_counts = {}

    lowercase = text.lower()
    for char in lowercase:
        if(char in char_counts):
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    return char_counts

def sort_on(items):
    return items["num"]

def get_sorted_list( chars ):
    ls = []
    for key in chars:
        ls.append({"name": key, "num": chars[key]})

    ls.sort(reverse=True, key=sort_on)

    return ls
