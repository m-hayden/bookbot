def get_word_count(str):
    words = str.split()
    return len(words)

def get_char_count(str):
    text = str.lower()
    char_dict = {}
    
    #first determine if the character exist:
    for char in text:    
        #if it does add to the value:
        if char in char_dict:
            char_dict[char] += 1
        #else add the character as a key w/ value 1:
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(dict):
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            new_char_dict = {
                "char": char,
                "num": count
            }
            char_list.append(new_char_dict)
    char_list.sort(reverse=True, key=lambda num: num["num"])
    return char_list