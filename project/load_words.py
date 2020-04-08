import sys
import json
import random

def load_words():
    with open(sys.argv[1]) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
    
def remove_punc(english_words):
    correct_list = [s.replace('"', '') for s in english_words]
    correct_list = [s.replace(':', '') for s in correct_list]
    
    return correct_list
  
    
def seven_char_words(complete_list):
    word_list = []
    for i in complete_list:
        if len(i) ==  7:
            word_list.append(i)
        
    return word_list


def get_uniq(seven_char_list):
    uniq_list = []
    for i in seven_char_list:
        char_list = []
        for char in i:
            if char not in char_list:
                char_list.append(char)
        if len(char_list) == 7:
            uniq_list.append(i)
            
    return(uniq_list)


def get_random_word(uniq_char_words):
    number = random.randint(1, len(uniq_char_words))
    random_word = uniq_char_words[number]
    
    return random_word


if __name__ == "__main__":
    english_words = load_words()
    complete_list = remove_punc(english_words)#use this list for all words
    seven_char_list = seven_char_words(complete_list)
    uniq_char_words = get_uniq(seven_char_list)
    random_word = get_random_word(uniq_char_words)#the word in the honeycomb
    
    print(random_word)
