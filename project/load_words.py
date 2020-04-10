import sys
import json
import random

def load_words():
    with open('words_dictionary.json', 'r') as word_file:
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

def correct_answer_finder(complete_list, random_word):
    correct_answers = []
    must_use_char = random_word[random.randint(1, len(random_word))]
    for item in complete_list:
        checked_word = ""
        if len(item) < 8:
            if must_use_char in item:
                for char in item:
                    if char in random_word:
                        checked_word += char
        if len(checked_word) == len(item):
            correct_answers.append(item)
    return correct_answers


#if __name__ == "__main__":
    #english_words = load_words()
    #complete_list = remove_punc(english_words)#use this list for all words
    #seven_char_list = seven_char_words(complete_list)
    #uniq_char_words = get_uniq(seven_char_list)
    #random_word = get_random_word(uniq_char_words)#the word in the honeycomb
    #correct_answers = correct_answer_finder(complete_list, random_word)


    #print(correct_answers)
    #print(random_word)
