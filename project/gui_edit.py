from tkinter import *

def get_input():
    p1_list = []
    p1 = entry_field.get()
    p1_list = p1_list.append(p1)
    return p1

def create_text_icon(a_word, root):
        icon0 = Text(root, height=1, width=1)
        icon0.grid(row=2, column=2)
        icon0.insert(INSERT, a_word[3])
        icon0.insert(END, "")

        icon1 = Text(root, height=1, width=1)
        icon1.grid(row=2, column=3)
        icon1.insert(INSERT, a_word[0])
        icon1.insert(END, "")

        icon2 = Text(root, height=1, width=1)
        icon2.grid(row=2, column=4)
        icon2.insert(INSERT, a_word[2])
        icon2.insert(END, "")

        icon3 = Text(root, height=1, width=1)
        icon3.grid(row=2, column=5)
        icon3.insert(INSERT, a_word[1])
        icon3.insert(END, "")


def check_score(answer, root):
    correct_list = ["blij", "bi", "bil"]
    if answer in correct_list:
        label = Text(root)
        label.insert(INSERT, "Correct! You get 5 points\nYou have .. points!")
        label.grid(row=6, column=7)
    else:
        label = Text(root)
        label.insert(INSERT, "Nope, try again!\nYou have .. points!")
        label.grid(row=6, column=7)


if __name__ == "__main__":
    
    root = Tk()
    root.geometry("700x400")
    
    entry_field = Entry(root)
    entry_field.grid(row=3, column=1)
    
    button1 = Button(root, command = check_score("bi", root))
    button1.grid(row=3, column=6)

    a = create_text_icon("blij", root)

    
    root.mainloop()

