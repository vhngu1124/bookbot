def get_num_words(text_list):
    list_length = len(text_list.split())
    return list_length

def count_letters(text_list):
    
    letter_dictionary = {
        "a": 0
    }

    for letter in text_list:
        if letter.lower() in letter_dictionary:
            letter_dictionary[letter.lower()] += 1
        else:
            letter_dictionary[letter.lower()] = 1
    
    return letter_dictionary

def sort_on(items):
    return items["count"]

def dictionary_to_list(dictionary):
    result = []
    for letter in dictionary:
        a = {'letter': letter, 'count': dictionary[letter]}
        result.append(a)
    result.sort(reverse=True, key=sort_on)
    
    return result

