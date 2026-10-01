import tkinter as tk
from mss import mss
from PIL import Image, ImageTk


def capture_screen():
    with mss() as screen:
        screenshot = screen.grab(screen.monitors[1])

    image = Image.frombytes(
        "RGB",
        screenshot.size,
        screenshot.bgra,
        "raw",
        "BGRX"
    )

    # Resize the screenshot to fit the preview
    image.thumbnail((700, 450))

    photo = ImageTk.PhotoImage(image)

    preview_label.config(image=photo)
    preview_label.image = photo

    status_label.config(text="Screen captured successfully")


app = tk.Tk()
app.title("Screen Assistant")
app.geometry("800x650")

title = tk.Label(
    app,
    text="Screen Assistant",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

assist_button = tk.Button(
    app,
    text="Assist",
    font=("Arial", 14),
    command=capture_screen,
    width=15
)
assist_button.pack(pady=10)

status_label = tk.Label(
    app,
    text="Waiting...",
    font=("Arial", 11)
)
status_label.pack(pady=5)

preview_label = tk.Label(app)
preview_label.pack(pady=15)

app.mainloop()