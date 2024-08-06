from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer")
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    #countdown(WORK_MIN*60) #get hold of number of seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    min_count = math.floor(count / 60) #number of minutes
    sec_count = count % 60 #number of seconds

    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW) #bg == background color



canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png") #reads the file to find the image
canvas.create_image(100, 112, image=tomato) #tells image where to go - x, y values
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font= (FONT_NAME, 35, "bold")) #must specify xy coordinates
canvas.grid(column=1, row=1) #displays image



title = Label(text="Timer")
title.grid(column=1, row=0)
title.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal")) #fg(foreground) changes text color

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)



reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=3)

checkmark = Label(bg=YELLOW, fg=PINK, font=(FONT_NAME, 40))
checkmark.grid(column=1, row=4)



#with tkinter, you often have to slightly change the coordinates to prevent edge of image being chopped off
window.mainloop()