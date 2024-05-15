import tkinter as tk
from tkinter import ttk
import pyttsx3
import random

def convert_text_to_speech():
    text = text_entry.get()
    engine.say(text)
    engine.runAndWait()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)    # Speed of speech (words per minute )
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Create a function to generate a random color
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Create the main application window
root = tk.Tk()
root.title("Text to Speech Converter")

# Create a Canvas widget with a random gradient background
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, highlightthickness=0)
canvas.pack()

# Generate random colors for the gradient
color1 = random_color()
color2 = random_color()

# Draw gradient rectangles
for i in range(100):
    color = "#%02x%02x%02x" % (
        int(color1[1:3], 16) * i // 100 + int(color2[1:3], 16) * (100 - i) // 100,
        int(color1[3:5], 16) * i // 100 + int(color2[3:5], 16) * (100 - i) // 100,
        int(color1[5:], 16) * i // 100 + int(color2[5:], 16) * (100 - i) // 100
    )
    canvas.create_rectangle(i * (canvas_width / 100), 0, (i + 1) * (canvas_width / 100), canvas_height, fill=color, outline="")

# Create and pack the labels with original style
label1 = ttk.Label(root, text="W E L C O M E   T O   T E X T  T O  S P E E C H   C O N V E R S I O N", font=('Arial', 14, 'bold'))
label1.place(relx=0.5, rely=0.1, anchor="center")

label2 = ttk.Label(root, text="PLEASE ENTER YOUR TEXT BELOW:", font=('Arial', 12))
label2.place(relx=0.5, rely=0.3, anchor="center")

# Create and pack the text entry field with original style
text_entry = ttk.Entry(root, width=50, font=('Arial', 12))
text_entry.place(relx=0.5, rely=0.4, anchor="center")

# Create and pack the convert button with original style
convert_button = ttk.Button(root, text="Convert", command=convert_text_to_speech)
convert_button.place(relx=0.5, rely=0.5, anchor="center")

# Run the application
root.mainloop()
