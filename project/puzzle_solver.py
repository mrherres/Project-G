from tkinter import *
from tkinter import messagebox
from load_words import *


# This function checks the answer and score for the user and updates the gui
# with the correct information.
def check_score(answer, root):
    correct_list = correct_answer_finder(complete_list, random_word,
                                         must_use_char)
    entry_field.delete(0, END)  # Delete first entry, otherwise raises error.
    if answer.lower() in answer_list:  # Check if answer was already given
        total_points = score_count(answer_list, random_word)
        label = Text(root, width='30', wrap=WORD)
        label.insert(INSERT, "Oops! You already had that one!\n"
                             "You have {0} points!\n"
                             .format(total_points))
        label.grid(row=6, column=1, sticky='w')
        label.insert(INSERT, "{0} words remaining.\n"
                             .format(len(correct_list) - len(answer_list)))
        label.insert(INSERT, answer_list)

    elif answer.lower() in correct_list:
        # Check if the user was correct
        answer_list.append(answer)
        earned_points = len(answer) - 3
        if (pangram_check(answer, random_word) is True):
            earned_points += 7
        total_points = score_count(answer_list, random_word)
        label = Text(root, width='30', wrap=WORD)
        label.insert(INSERT, "Correct! You get {0} points\nYou have {1} "
                             "points!\n"
                             .format(earned_points, total_points))
        label.grid(row=6, column=1, sticky='w')
        label.insert(INSERT, "{0} words remaining.\n"
                             .format(len(correct_list) - len(answer_list)))
        label.grid(row=6, column=1, sticky='w')
        label.insert(INSERT, answer_list)

    else:  # Reply for when the users answer was not correct
        total_points = score_count(answer_list, random_word)
        label = Text(root, width='30', wrap=WORD)
        label.insert(INSERT, "Nope, try again!\nYou have {0} points!\n"
                             .format(total_points))
        label.grid(row=6, column=1, sticky='w')
        label.insert(INSERT, "{0} words remaining.\n"
                             .format(len(correct_list) - len(answer_list)))
        label.insert(INSERT, answer_list)


# This function counts the score of the user by checking the length of the
# answers given
def score_count(answer_list, random_word):
    total_points = 0
    for item in answer_list:
        total_points += len(item) - 3
        if (pangram_check(item, random_word) is True):
            total_points += 7
    return total_points


# This fucntion creates the squares with letter which the user can choose from
def create_text_icon(a_word, root, char_list):
        icon1 = Button(root, height=1, width=1, font='Arial 30', bg='pink',
                       text=char_list[0])
        icon1.grid(row=1, column=1, sticky='w', padx=30)

        icon2 = Button(root, height=1, width=1, font='Arial 30', bg='pink',
                       text=char_list[1])
        icon2.grid(row=1, column=1, sticky='w', padx=90)

        icon3 = Button(root, height=1, width=1, font='Arial 30', bg='pink',
                       text=char_list[2])
        icon3.grid(row=2, column=1, sticky='w')
        # Icon4 creates the square with the letter that must be used
        icon4 = Button(root, height=1, width=1, font='Arial 30', bg='yellow',
                       text=must_use_char)
        icon4.grid(row=2, column=1, sticky='w', padx=60)

        icon5 = Button(root, height=1, width=1, font='Arial 30', bg='pink',
                       text=char_list[3])
        icon5.grid(row=2, column=1, sticky='w', padx=120)

        icon6 = Button(root, height=1, width=1, font='Arial 30', bg='pink',
                       text=char_list[4])
        icon6.grid(row=3, column=1, sticky='w', padx=30)

        icon7 = Button(root, height=1, width=1, font='Arial 30', bg='pink',
                       text=char_list[5])
        icon7.grid(row=3, column=1, sticky='w', padx=90)


# This function makes sure the index of the letters given to "create_text_icon"
# is random
def index_word(word, must_use_char):
    word = word.replace(must_use_char, "")
    char1 = word[random.randint(0, 5)]
    word = word.replace(char1, "")
    char2 = word[random.randint(0, 4)]
    word = word.replace(char2, "")
    char3 = word[random.randint(0, 3)]
    word = word.replace(char3, "")
    char4 = word[random.randint(0, 2)]
    word = word.replace(char4, "")
    char5 = word[random.randint(0, 1)]
    word = word.replace(char5, "")
    char6 = word
    char_list = [char1, char2, char3, char4, char5, char6]
    return char_list


# This is the base of the program, which calls all the necessary files
# and functions to run the game.
if __name__ == "__main__":

    root = Tk()
    root.geometry("700x400")  # Create the window for the game
    # This gives the user useful information on how to play the game

    answer_list = []
    total_points = 0

    entry_field = Entry(root)  # Creates the entry field for the user to type
# the answers
    entry_field.grid(row=4, column=1, sticky='w')
    entry_field.focus()

    dutch_words = load_words()  # This is the file which contains a lot of
# Dutch words, which the program uses to check answers
    complete_list = remove_punc(dutch_words)  # Use this list for all words
    seven_char_list = seven_char_words(complete_list)
    uniq_char_words = get_uniq(seven_char_list)  # This makes sure there are no
# duplicates in the collection of words
    random_word = get_random_word(uniq_char_words)  # The word used for
# the honeycomb
    must_use_char = must_use_char_pick(random_word)  # The character that must
# be used in every answer
    correct_answers = correct_answer_finder(complete_list, random_word,
                                            must_use_char)

    chars_list = index_word(random_word, must_use_char)  # Divides the word in
# characters to display in the gui
    icons = create_text_icon(random_word, root, chars_list)  # This makes sure
# the icons are created

    for item in correct_answers:   # enters all correct answers
        check_score(item, root)

    root.mainloop()  # Makes sure the program keeps on running
