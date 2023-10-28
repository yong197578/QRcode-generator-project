from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()


def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(300, 600, window=image_label)


canvas = Canvas(root, width=600, height=800)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="blue", font=("Arial", 60))
canvas.create_window(300, 75, window=app_label)

name_label = Label(root, text="Link name", fg="green", font=("Arial", 40))
link_label = Label(root, text="Link", fg="green", font=("Arial", 40))
canvas.create_window(300, 150, window=name_label)
canvas.create_window(300, 250, window=link_label)

name_entry = Entry(root, width=40, font=('Arial', 24))
link_entry = Entry(root,  width=40, font=('Arial', 24))
canvas.create_window(300, 200, window=name_entry)
canvas.create_window(300, 300, window=link_entry)

button = Button(text="Generate QR code", height=3, width=30, font=('Arial', 24), fg="red", command=generate)
canvas.create_window(300, 400, window=button)

root.mainloop()