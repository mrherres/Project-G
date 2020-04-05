from tkinter import *

def get_input():
    p1_list = []
    p1 = entry_field.get()
    p1_list = p1_list.append(p1)
    print(p1)

if __name__ == "__main__":
    
    root = Tk()
    root.geometry("350x200")
    
    entry_field = Entry(root)
    entry_field.grid(row=0, column=1)
    
    button1 = Button(root, command = get_input)
    button1.grid(row=1, column=2)
    
    root.mainloop()

