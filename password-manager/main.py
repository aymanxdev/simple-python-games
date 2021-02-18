from tkinter import *
from PIL import Image, ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


logo_img = PhotoImage(file="logo.gif")
canvas = Canvas(width= 200, height=200)
canvas.create_image(100,103, image= logo_img)
canvas.grid(column=1, row=0)

# --------------- website Label --------------- #
website_label = Label(text="Website: ")
website_label.grid(column= 0, row=1)
website_input = Entry(width=36)
website_input.grid(column= 1, row=1, columnspan=2)
# --------------- Email/Username Label --------------- #
username_label = Label(text="Email/Username: ")
username_label.grid(column= 0, row=2)
username_input = Entry(width=36)
username_input.grid(column= 1, row=2, columnspan=2)
# --------------- Password Label --------------- #
password_label = Label(text="Password: ")
password_label.grid(column= 0, row=3)
password_input = Entry(width=21)
password_input.grid(column= 1, row=3)
# --------------- Generate Button --------------- #
generate_button = Button(text="Generate Password")
generate_button.grid(column= 2, row=3)
# --------------- Add Button --------------- #
add_button = Button(text="Add", width=36)
add_button.grid(column= 1, row= 4, columnspan=2)







# img = Image.open("logo.png")
# logo_img = ImageTk.PhotoImage(img)
window.mainloop()