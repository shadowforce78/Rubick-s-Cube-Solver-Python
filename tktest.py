import tkinter as tk
from main import get_json_notation
import cv2
import numpy as np


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

    # Add a label current_moves / total_moves
    label_moves = tk.Label(bottom_frame, text="0 / 0")
    label_moves.pack()

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
        data = get_json_notation()

        # Get the current move as a number
        current_move_str = moves[current_moves]

        # Get the image associated with the move
        img = tk.PhotoImage(file=f"./images/{current_move_str}.png")

        # Update the image
        label.config(image=img)
        label.image = img

        # Update the text
        text.config(text=data[current_move_str])

    def button_next():
        global current_move
        associate_moves_with_images(current_move)
        current_move += 1
        if current_move == total_moves:
            current_move = 0

        label_moves.config(text=f"{current_move} / {total_moves}")
        img = tk.PhotoImage(file=f"./images/{moves[current_move]}.png")

    def button_previous():
        global current_move
        associate_moves_with_images(current_move)
        current_move -= 1
        if current_move == -1:
            current_move = total_moves - 1

        label_moves.config(text=f"{current_move} / {total_moves}")
        img = tk.PhotoImage(file=f"./images/{moves[current_move]}.png")

    # Bind the buttons to the functions
    button1.config(command=button_previous)
    button2.config(command=button_next)

    # Add an image to the top frame, rezise it to 100x100
    img = tk.PhotoImage(file=f"./images/rubik.png")
    img = img.subsample(2)  # Resize the image to 100x100
    label = tk.Label(top_frame, image=img)
    label.pack()

    # Add a label to the top frame with some text
    text = tk.Label(top_frame, text="This is a Rubik's Cube")
    text.pack()

    # Start the window
    window.mainloop()


def detect_rubiks_face_from_camera():
    cap = cv2.VideoCapture(2)

    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la caméra.")
        return

    def get_dominant_color(patch):
        data = np.float32(patch).reshape((-1, 3))
        _, labels, centers = cv2.kmeans(
            data,
            1,
            None,
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
            10,
            cv2.KMEANS_RANDOM_CENTERS,
        )
        return centers[0].astype(int)

    def get_rubiks_color(bgr):
        hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]
        h, s, v = hsv

        if s < 50:
            return "white" if v > 200 else "gray"
        if v < 50:
            return "black"

        if h < 10 or h >= 160:
            return "red"
        elif 10 <= h < 25:
            return "orange"
        elif 25 <= h < 35:
            return "yellow"
        elif 35 <= h < 85:
            return "green"
        elif 85 <= h < 125:
            return "blue"
        else:
            return "red"

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Erreur: Impossible de lire une image de la caméra.")
            break

        # Définir un carré au centre de l'image
        height, width, _ = frame.shape
        square_size = min(width, height) // 3
        x_start = width // 2 - square_size // 2
        y_start = height // 2 - square_size // 2

        # Extraire la région d'intérêt (ROI)
        roi = frame[y_start : y_start + square_size, x_start : x_start + square_size]

        # Diviser la ROI en une grille 3x3
        cell_size = square_size // 3
        colors = []

        for i in range(3):
            row_colors = []
            for j in range(3):
                cell = roi[
                    i * cell_size : (i + 1) * cell_size,
                    j * cell_size : (j + 1) * cell_size,
                ]
                dominant_color = get_dominant_color(cell)
                rubiks_color = get_rubiks_color(dominant_color)
                row_colors.append(rubiks_color)
                # Dessiner les cases sur l'image
                cv2.rectangle(
                    frame,
                    (x_start + j * cell_size, y_start + i * cell_size),
                    (x_start + (j + 1) * cell_size, y_start + (i + 1) * cell_size),
                    (0, 255, 0),
                    2,
                )
            colors.append(row_colors)

        # Afficher les couleurs détectées dans la console
        print("\n".join([" ".join(row) for row in colors]))

        # Afficher l'image avec les cases détectées
        cv2.imshow("Rubik's Cube Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_rubiks_face_from_camera()
