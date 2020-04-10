from tkinter import *
from load_words import *

def get_input():
    p1_list = []
    p1 = entry_field.get()
    p1_list = p1_list.append(p1)
    check_score(p1, root)
    
def check_score(answer, root):
    correct_list = correct_answer_finder(complete_list, random_word, must_use_char)
    entry_field.delete(0, END)
    if answer.lower() in correct_list and answer.lower() not in answer_list:
        answer_list.append(answer)
        earned_points = len(answer) - 3
        if (pangram_check(answer, random_word) == True):
            earned_points += 7
        total_points = score_count(answer_list, random_word)
        label = Text(root, width='30')
        label.insert(INSERT, "Correct! You get {0} points\nYou have {1} points!\n".format(earned_points, total_points))
        label.grid(row=6, column=1, sticky='w')
        label.insert(INSERT, answer_list)

    elif answer.lower() in answer_list:
        total_points = score_count(answer_list, random_word)
        label = Text(root, width='30')
        label.insert(INSERT, "Oops! You already had that one!\nYou have {0} points!\n".format(total_points))
        label.grid(row=6, column=1, sticky='w')
        label.insert(INSERT, answer_list)

    else:
        total_points = score_count(answer_list, random_word)
        label = Text(root, width='30')
        label.insert(INSERT, "Nope, try again!\nYou have {0} points!\n".format(total_points))
        label.grid(row=6, column=1, sticky='w')
        label.insert(INSERT, answer_list)


def score_count(answer_list, pangram_status):
    total_points = 0
    for item in answer_list:
        total_points += len(item) - 3
        if (pangram_check(item, random_word) == True):
            total_points += 7
    return total_points


def create_text_icon(a_word, root, char_list):
        icon1 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=char_list[0])
        icon1.grid(row=1, column=1, sticky='w', padx=30)

        icon2 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=char_list[1])
        icon2.grid(row=1, column=1, sticky='w', padx=90)

        icon3 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=char_list[2])
        icon3.grid(row=2, column=1, sticky='w')

        icon4 = Button(root, height=1, width=1, font='Arial 30', bg='yellow', text=must_use_char)
        icon4.grid(row=2, column=1, sticky='w', padx=60)

        icon5 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=char_list[3])
        icon5.grid(row=2, column=1, sticky='w', padx=120)

        icon6 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=char_list[4])
        icon6.grid(row=3, column=1, sticky='w', padx=30)

        icon7 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=char_list[5])
        icon7.grid(row=3, column=1, sticky='w', padx=90)



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


if __name__ == "__main__":
    
    root = Tk()
    root.geometry("700x400")
    
    answer_list = []
    total_points = 0
    
    entry_field = Entry(root)
    entry_field.grid(row=4, column=1, sticky='w')
    entry_field.focus()
    
    button1 = Button(root, command = get_input, height=1, width=5, text='CHECK')
    button1.grid(row=4, column=2)
    
    english_words = load_words()
    complete_list = remove_punc(english_words)#use this list for all words
    seven_char_list = seven_char_words(complete_list)
    uniq_char_words = get_uniq(seven_char_list)
    random_word = get_random_word(uniq_char_words)#the word in the honeycomb
    must_use_char = must_use_char_pick(random_word)
    correct_answers = correct_answer_finder(complete_list, random_word, must_use_char)


    #print(correct_answers)
    #print(random_word)
    chars_list = index_word(random_word, must_use_char)
    a = create_text_icon(random_word, root, chars_list)


    root.mainloop()

