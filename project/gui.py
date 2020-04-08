from tkinter import *

def get_input():
    p1_list = []
    p1 = entry_field.get()
    p1_list = p1_list.append(p1)
    check_score(p1, root)
    
def check_score(answer, root):
    correct_list = ["blij", "bi", "bil", "bijl"]
    entry_field.delete(0, END)
    if answer.lower() in correct_list and answer.lower() not in answer_list:
        answer_list.append(answer)
        score = 5 * len(answer_list)
        label = Text(root)
        label.insert(INSERT, "Correct! You get 5 points\nYou have {0} points!\n".format(score))
        label.grid(row=6, column=7)
        label.insert(INSERT, answer_list)

    elif answer.lower() in answer_list:
        score = 5 * len(answer_list)
        label = Text(root)
        label.insert(INSERT, "Oops! You already had that one!\nYou have {0} points!\n".format(score))
        label.grid(row=6, column=7)
        label.insert(INSERT, answer_list)

    else:
        score = 5 * len(answer_list)
        label = Text(root)
        label.insert(INSERT, "Nope, try again!\nYou have {0} points!\n".format(score))
        label.grid(row=6, column=7)
        label.insert(INSERT, answer_list)


def create_text_icon(a_word, root):
        icon1 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=a_word[4])
        icon1.grid(row=1, column=1, sticky='w', padx=30)

        icon2 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=a_word[2])
        icon2.grid(row=1, column=1, sticky='w', padx=90)

        icon3 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=a_word[3])
        icon3.grid(row=2, column=1, sticky='w')

        icon4 = Button(root, height=1, width=1, font='Arial 30', bg='yellow', text=a_word[1])
        icon4.grid(row=2, column=1, sticky='w', padx=60)

        icon5 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=a_word[6])
        icon5.grid(row=2, column=1, sticky='w', padx=120)

        icon6 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=a_word[0])
        icon6.grid(row=3, column=1, sticky='w', padx=30)

        icon7 = Button(root, height=1, width=1, font='Arial 30', bg='pink', text=a_word[5])
        icon7.grid(row=3, column=1, sticky='w', padx=90)


if __name__ == "__main__":
    
    root = Tk()
    root.geometry("700x400")
    
    answer_list = []
    
    entry_field = Entry(root)
    entry_field.grid(row=4, column=1)
    entry_field.focus()
    
    button1 = Button(root, command = get_input)
    button1.grid(row=4, column=6)

    a = create_text_icon("obscure", root)


    root.mainloop()

