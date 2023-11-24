from tkinter import *
import pandas
import random
reps = 0
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn")
except FileNotFoundError:
    orginal_data = pandas.read_csv("data/french_words.csv")
    to_lear = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}
data= pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=old_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=new_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400, 263, image=old_image)

card_title = canvas.create_text(400, 150, text="",font=("Ariel", 40, "italic"))

card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(column=0, row=1)

yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=is_known)
yes_button.grid(column=1, row=1)

next_card()


window.mainloop()