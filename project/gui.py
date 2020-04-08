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
        icon0 = Text(root, height=1, width=1, font='Arial 30', bg='pink')
        icon0.grid(row=1, column=1, sticky='w', padx=15)
        icon0.insert(INSERT, a_word[3])
        icon0.insert(END, "")

        icon1 = Text(root, height=1, width=1, font='Arial 30', bg='pink')
        icon1.grid(row=1, column=1, sticky='w', padx=45)
        icon1.insert(INSERT, a_word[0])
        icon1.insert(END, "")

        icon2 = Text(root, height=1, width=1, font='Arial 30', bg='pink')
        icon2.grid(row=2, column=1, sticky='w')
        icon2.insert(INSERT, a_word[2])
        icon2.insert(END, "")

        icon3 = Text(root, height=1, width=1, font='Arial 30', bg='pink')
        icon3.grid(row=2, column=1, sticky='w', padx=30)
        icon3.insert(INSERT, a_word[1])
        icon3.insert(END, "")

        icon4 = Text(root, height=1, width=1, font='Arial 30', bg='pink')
        icon4.grid(row=2, column=1, sticky='w', padx=60)
        icon4.insert(INSERT, a_word[4])
        icon4.insert(END, "")

        icon5 = Text(root, height=1, width=1, font='Arial 30', bg='pink')
        icon5.grid(row=3, column=1, sticky='w', padx=15)
        icon5.insert(INSERT, a_word[6])
        icon5.insert(END, "")

        icon6 = Text(root, height=1, width=1, font='Arial 30', bg='pink')
        icon6.grid(row=3, column=1, sticky='w', padx=45)
        icon6.insert(INSERT, a_word[5])
        icon6.insert(END, "")


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

