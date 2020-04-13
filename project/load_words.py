import sys
import json
import random


# This function read the word file and puts all words in a list.
def load_words():
    all_words = set('AI')
    fname = 'nederlands.txt'
    with open(fname) as f:
        all_words.update(f.read().splitlines())

    return all_words


# This function removes all punctuation.
def remove_punc(english_words):
    correct_list = [s.replace('"', '') for s in english_words]
    correct_list = [s.replace(':', '') for s in correct_list]

    return correct_list


# This function finds all words containing 7 characters in a list.
def seven_char_words(complete_list):
    word_list = []
    for i in complete_list:
        if len(i) == 7:
            word_list.append(i)

    return word_list


# This function finds all words containing only unique characters.
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


# This function picks a random word from a list.
def get_random_word(uniq_char_words):
    number = random.randint(1, len(uniq_char_words))
    random_word = uniq_char_words[number]

    return random_word


# This function picks a random character from a word.
def must_use_char_pick(random_word):
    must_use_char = random_word[random.randint(0, 6)]
    return must_use_char


# This function makes a list of words containing only the characters of
# a certain word.
def correct_answer_finder(complete_list, random_word, must_use_char):
    correct_answers = []
    for item in complete_list:
        checked_word = ""
        if len(item) > 3:
            if must_use_char in item:
                for char in item:
                    if char in random_word:
                        checked_word += char
        if len(checked_word) == len(item):
            correct_answers.append(item)
    return correct_answers


# This function checks if a word contains all 7 characters.
def pangram_check(answer, random_word):
    for char in random_word:
        if char not in answer:
            return False

    return True
