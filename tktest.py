import tkinter as tk
import json
from main import getJsonNotation


moves = [
    "B",
    "B",
    "L",
    "L",
    "R",
    "R",
    "Z",
    "L",
    "L",
    "R",
    "R",
    "Zi",
    "U",
    "B",
    "Ui",
    "B",
    "B",
    "D",
    "Bi",
    "Di",
    "Z",
    "U",
    "B",
    "Ui",
    "B",
    "B",
    "D",
    "Bi",
    "Di",
    "Z",
    "Bi",
    "Ri",
    "B",
    "R",
    "Z",
    "B",
    "B",
    "Bi",
    "Ri",
    "B",
    "R",
    "Z",
    "Z",
    "Z",
    "B",
    "L",
    "Bi",
    "Li",
    "Bi",
    "Di",
    "B",
    "D",
    "Zi",
    "Zi",
    "B",
    "B",
    "B",
    "Bi",
    "Di",
    "B",
    "D",
    "B",
    "L",
    "Bi",
    "Li",
    "Z",
    "Bi",
    "Di",
    "B",
    "D",
    "B",
    "L",
    "Bi",
    "Li",
    "Z",
    "B",
    "B",
    "L",
    "Bi",
    "Li",
    "Bi",
    "Di",
    "B",
    "D",
    "Z",
    "B",
    "B",
    "L",
    "Bi",
    "Li",
    "Bi",
    "Di",
    "B",
    "D",
    "Z",
    "X",
    "X",
    "F",
    "D",
    "R",
    "F",
    "Ri",
    "Fi",
    "Di",
    "Xi",
    "Xi",
    "X",
    "X",
    "Zi",
    "Li",
    "Fi",
    "L",
    "D",
    "F",
    "Di",
    "Li",
    "F",
    "L",
    "F",
    "F",
    "Z",
    "Li",
    "Fi",
    "L",
    "D",
    "F",
    "Di",
    "Li",
    "F",
    "L",
    "F",
    "F",
    "Xi",
    "Xi",
    "X",
    "X",
    "F",
    "R",
    "F",
    "Ri",
    "F",
    "R",
    "F",
    "F",
    "Ri",
    "F",
    "F",
    "F",
    "F",
    "F",
    "Xi",
    "Xi",
    "X",
    "X",
    "R",
    "R",
    "F",
    "D",
    "Ui",
    "R",
    "R",
    "Di",
    "U",
    "F",
    "R",
    "R",
    "Z",
    "Z",
    "Z",
    "Z",
    "Z",
    "R",
    "R",
    "F",
    "D",
    "Ui",
    "R",
    "R",
    "Di",
    "U",
    "F",
    "R",
    "R",
    "Z",
    "Di",
    "Li",
    "Ri",
    "S",
    "Ri",
    "Ri",
    "S",
    "S",
    "Ri",
    "Fi",
    "Fi",
    "R",
    "Si",
    "Si",
    "Ri",
    "Ri",
    "Si",
    "R",
    "Fi",
    "Fi",
    "L",
    "D",
]


def moves_to_image():

    # Create a window 200x200
    window = tk.Tk()
    window.geometry("200x200")
    window.title("Rubik's Cube")

    # Create two partitions
    top_frame = tk.Frame(window)
    top_frame.pack()
    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side=tk.BOTTOM)

    # Add two buttons at the bottom
    button1 = tk.Button(bottom_frame, text="Previous Image", fg="red")
    button2 = tk.Button(bottom_frame, text="Next Image", fg="blue")
    button1.pack(side=tk.LEFT)
    button2.pack(side=tk.LEFT)

    global current_move
    current_move = 0
    global total_moves
    total_moves = len(moves)

    def associate_moves_with_images(current_moves):
        # Get the json file with all the notation
        data = getJsonNotation()

        # Get the current move as a number
        current_move_str = moves[current_moves]

        # Get the image associated with the move
        img = tk.PhotoImage(file=f"./images/{current_move_str}.png")

        # Update the image
        label.config(image=img)
        label.image = img

    def button_next():
        global current_move
        associate_moves_with_images(current_move)
        current_move += 1
        if current_move == total_moves:
            current_move = 0

    # Bind the buttons to the functions
    button2.config(command=button_next)

    imgFolder = "./images/"

    # Add an image to the top frame
    img = tk.PhotoImage(file=imgFolder + "L.png")
    label = tk.Label(top_frame, image=img)
    label.pack()

    # Add a label to the top frame with some text
    text = tk.Label(top_frame, text="This is a Rubik's Cube")
    text.pack()

    # Start the window
    window.mainloop()


if __name__ == "__main__":
    moves_to_image()
