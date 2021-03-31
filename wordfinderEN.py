import tkinter as tk
from tkinter import Button, Entry, ttk

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

e = Entry(root)
e.pack()
e.insert(0, "Regex:")

def myDelete():
    myLabel.destroy()


def myClick():


    import re
    global input, myLabel
    def get_wlyst():
        ww=open('wlystEN')
        ww=[w.strip() for w in ww]
        ww.append('nonstop')
        ww.append('autopech')
        ww.append('topprioriteit')
        return ww


    ww=get_wlyst()
    ding = str(e.get())
    
    zoekwoord=ding.lower()
    rx=re.compile("^"+zoekwoord+"$")

    xx=filter(rx.search,ww)
    input = '\n'.join(xx)
    myLabel = ttk.Label(scrollable_frame, text=input)
    myLabel.pack()

    










myButton = Button(root, text='Run', command=myClick, width=10, borderwidth= 2.5)
myButton.pack()

deleteButton = Button(root, text='clear', command=myDelete, width= 10, borderwidth=2.5)
deleteButton.pack(pady=10)



    

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()