import tkinter as tk
import json
from main import getJsonNotation


moves_notations = [
    "Back clockwise",
    "Back clockwise",
    "Left clockwise",
    "Left clockwise",
    "Right clockwise",
    "Right clockwise",
    "Rotate the cube on F face",
    "Left clockwise",
    "Left clockwise",
    "Right clockwise",
    "Right clockwise",
    "Rotate the cube on B face",
    "Up clockwise",
    "Back clockwise",
    "Up counterclockwise",
    "Back clockwise",
    "Back clockwise",
    "Down clockwise",
    "Back counterclockwise",
    "Down counterclockwise",
    "Rotate the cube on F face",
    "Up clockwise",
    "Back clockwise",
    "Up counterclockwise",
    "Back clockwise",
    "Back clockwise",
    "Down clockwise",
    "Back counterclockwise",
    "Down counterclockwise",
    "Rotate the cube on F face",
    "Back counterclockwise",
    "Right counterclockwise",
    "Back clockwise",
    "Right clockwise",
    "Rotate the cube on F face",
    "Back clockwise",
    "Back clockwise",
    "Back counterclockwise",
    "Right counterclockwise",
    "Back clockwise",
    "Right clockwise",
    "Rotate the cube on F face",
    "Rotate the cube on F face",
    "Rotate the cube on F face",
    "Back clockwise",
    "Left clockwise",
    "Back counterclockwise",
    "Left counterclockwise",
    "Back counterclockwise",
    "Down counterclockwise",
    "Back clockwise",
    "Down clockwise",
    "Rotate the cube on B face",
    "Rotate the cube on B face",
    "Back clockwise",
    "Back clockwise",
    "Back clockwise",
    "Back counterclockwise",
    "Down counterclockwise",
    "Back clockwise",
    "Down clockwise",
    "Back clockwise",
    "Left clockwise",
    "Back counterclockwise",
    "Left counterclockwise",
    "Rotate the cube on F face",
    "Back counterclockwise",
    "Down counterclockwise",
    "Back clockwise",
    "Down clockwise",
    "Back clockwise",
    "Left clockwise",
    "Back counterclockwise",
    "Left counterclockwise",
    "Rotate the cube on F face",
    "Back clockwise",
    "Back clockwise",
    "Left clockwise",
    "Back counterclockwise",
    "Left counterclockwise",
    "Back counterclockwise",
    "Down counterclockwise",
    "Back clockwise",
    "Down clockwise",
    "Rotate the cube on F face",
    "Back clockwise",
    "Back clockwise",
    "Left clockwise",
    "Back counterclockwise",
    "Left counterclockwise",
    "Back counterclockwise",
    "Down counterclockwise",
    "Back clockwise",
    "Down clockwise",
    "Rotate the cube on F face",
    "Rotate the cube on R face",
    "Rotate the cube on R face",
    "Front clockwise",
    "Down clockwise",
    "Right clockwise",
    "Front clockwise",
    "Right counterclockwise",
    "Front counterclockwise",
    "Down counterclockwise",
    "Rotate the cube on L face",
    "Rotate the cube on L face",
    "Rotate the cube on R face",
    "Rotate the cube on R face",
    "Rotate the cube on B face",
    "Left counterclockwise",
    "Front counterclockwise",
    "Left clockwise",
    "Down clockwise",
    "Front clockwise",
    "Down counterclockwise",
    "Left counterclockwise",
    "Front clockwise",
    "Left clockwise",
    "Front clockwise",
    "Front clockwise",
    "Rotate the cube on F face",
    "Left counterclockwise",
    "Front counterclockwise",
    "Left clockwise",
    "Down clockwise",
    "Front clockwise",
    "Down counterclockwise",
    "Left counterclockwise",
    "Front clockwise",
    "Left clockwise",
    "Front clockwise",
    "Front clockwise",
    "Rotate the cube on L face",
    "Rotate the cube on L face",
    "Rotate the cube on R face",
    "Rotate the cube on R face",
    "Front clockwise",
    "Right clockwise",
    "Front clockwise",
    "Right counterclockwise",
    "Front clockwise",
    "Right clockwise",
    "Front clockwise",
    "Front clockwise",
    "Right counterclockwise",
    "Front clockwise",
    "Front clockwise",
    "Front clockwise",
    "Front clockwise",
    "Front clockwise",
    "Rotate the cube on L face",
    "Rotate the cube on L face",
    "Rotate the cube on R face",
    "Rotate the cube on R face",
    "Right clockwise",
    "Right clockwise",
    "Front clockwise",
    "Down clockwise",
    "Up counterclockwise",
    "Right clockwise",
    "Right clockwise",
    "Down counterclockwise",
    "Up clockwise",
    "Front clockwise",
    "Right clockwise",
    "Right clockwise",
    "Rotate the cube on F face",
    "Rotate the cube on F face",
    "Rotate the cube on F face",
    "Rotate the cube on F face",
    "Rotate the cube on F face",
    "Right clockwise",
    "Right clockwise",
    "Front clockwise",
    "Down clockwise",
    "Up counterclockwise",
    "Right clockwise",
    "Right clockwise",
    "Down counterclockwise",
    "Up clockwise",
    "Front clockwise",
    "Right clockwise",
    "Right clockwise",
    "Rotate the cube on F face",
    "Down counterclockwise",
    "Left counterclockwise",
    "Right counterclockwise",
    "Standing, the layer between F and B, turn direction as F",
    "Right counterclockwise",
    "Right counterclockwise",
    "Standing, the layer between F and B, turn direction as F",
    "Standing, the layer between F and B, turn direction as F",
    "Right counterclockwise",
    "Front counterclockwise",
    "Front counterclockwise",
    "Right clockwise",
    "Standing, the layer between F and B, turn direction as B",
    "Standing, the layer between F and B, turn direction as B",
    "Right counterclockwise",
    "Right counterclockwise",
    "Standing, the layer between F and B, turn direction as B",
    "Right clockwise",
    "Front counterclockwise",
    "Front counterclockwise",
    "Left clockwise",
    "Down clockwise",
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

    # Button one function
    def associate_moves_with_images():
        # Get the json file with all the notation
        data = getJsonNotation()

        moves_size = len(moves_notations)
        print(moves_size)

    # Bind the buttons to the functions
    button1.config(command=associate_moves_with_images)

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
