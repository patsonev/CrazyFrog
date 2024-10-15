from tkinter import *
from PIL import Image, ImageTk
import random
import time
from threading import Thread

root = Tk()
root.resizable(0, 0)
root.title("CrazyFrog")
root.geometry("680x550")

buttons_frame = Frame(root, bg="white", padx=5, width=640, height=485)
buttons_frame.grid(row=0, column=0, padx=20, pady=5, sticky="nsew")

frog_image = Image.open("C:/Users/PC/Desktop/SmartFarmRobotix/CrazyFrog/frog_img.png")
frog_image = frog_image.resize((130, 130))
frog_image = ImageTk.PhotoImage(frog_image)

global to_show
to_show = -1

global points_counter
points_counter = 0

global best
best = 0

def button_clicked():
    global clicked
    clicked = clicked
    clicked = True
    
def frog_btns():
    global to_show
    to_show = to_show

    global points_counter
    points_counter = points_counter

    to_show *= -1

    while to_show > 0:
        global clicked
        clicked = False

        random_btn_num = random.randint(0, 8)

        for btn_num in range(0, 9):
            if btn_num == random_btn_num:
                btn = Button(
                    buttons_frame, 
                    image=frog_image,
                    text = "", 
                    bd = 0,
                    pady=3, 
                    command=button_clicked
                    )
                btn.grid(row=int(btn_num / 3), column=int(btn_num % 3), padx=15, pady=15)

            else:
                btn = Button(
                    buttons_frame, 
                    text = "", 
                    width = 25,
                    height=8,
                    bd = 0,
                    pady=3
                    )
                btn.grid(row=int(btn_num / 3), column=int(btn_num % 3), padx=15, pady=15)

        time.sleep(1 - (0.2 * points_counter / 50))

        if clicked:
            points_counter += 1
        else:
            points_counter -= 1

        points_lbl["text"] = f"Points: {points_counter}"

        global best
        if points_counter > best:
            best = points_counter

        best_lbl["text"] = f"Best result: {best}"

        widgets = buttons_frame.grid_slaves()
        for w in widgets:
            w.destroy()

        if points_counter < 0:
            Label(
                buttons_frame, 
                bg="white",
                text="Game Over", 
                font=("Helvetica", 50)
            ).grid(row=0, column=0, padx=140, pady=203)
            
            break

    if to_show < 0:
        widgets = buttons_frame.grid_slaves()
        for w in widgets:
            w.destroy()

        points_counter = 0
        
        points_lbl["text"]=f"Points: {points_counter}"

home_frame = Frame(root, padx=5)
home_frame.grid(row=1, column=0, padx=30, pady=0, sticky="nsew")

points_lbl = Label(
    home_frame, 
    text="Points: 0", 
    font=("Helvetica", 12)
    )
points_lbl.grid(row=0, column=0, padx=(10, 0))

start_btn = Button(
        home_frame, 
        text = "Start / Stop", 
        width = 20,
        height=2,
        bd = 1,
        font=("Helvetica", 10),
        pady=3, 
        command=lambda: Thread(target=frog_btns).start()
    )
start_btn.grid(row=0, column=1, padx=(140, 100))

best_lbl = Label(
    home_frame, 
    text="Best result: 0", 
    font=("Helvetica", 12)
    )
best_lbl.grid(row=0, column=2, padx=0)

root.mainloop()