import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox
from threading import Thread

class RubiksCubeScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Rubik's Cube Scanner")

        self.cap = cv2.VideoCapture(2)
        if not self.cap.isOpened():
            messagebox.showerror("Erreur", "Impossible d'ouvrir la caméra.")
            self.root.quit()

        self.frame = None
        self.face_colors = []
        self.face_index = 1

        self.label = tk.Label(root, text="Scannez la face 1 du Rubik's Cube", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.capture_button = tk.Button(root, text="Capturer la face", command=self.capture_face)
        self.capture_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Face suivante", command=self.next_face, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.result_button = tk.Button(root, text="Voir les couleurs scannées", command=self.show_results, state=tk.DISABLED)
        self.result_button.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.video_thread = Thread(target=self.update_frame)
        self.video_thread.start()

    def get_dominant_color(self, patch):
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

    def get_rubiks_color(self, bgr):
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

    def capture_face(self):
        if self.frame is not None:
            height, width, _ = self.frame.shape
            square_size = min(width, height) // 3
            x_start = width // 2 - square_size // 2
            y_start = height // 2 - square_size // 2

            roi = self.frame[y_start:y_start + square_size, x_start:x_start + square_size]

            cell_size = square_size // 3
            face_colors = []

            for i in range(3):
                row_colors = []
                for j in range(3):
                    cell = roi[i * cell_size:(i + 1) * cell_size, j * cell_size:(j + 1) * cell_size]
                    dominant_color = self.get_dominant_color(cell)
                    rubiks_color = self.get_rubiks_color(dominant_color)
                    row_colors.append(rubiks_color)
                face_colors.append(row_colors)

            self.face_colors.append(face_colors)

            self.next_button.config(state=tk.NORMAL)
            self.result_button.config(state=tk.NORMAL if self.face_index == 6 else tk.DISABLED)
            self.label.config(text=f"Face {self.face_index} scannée. Passez à la face suivante.")

            self.face_index += 1

    def next_face(self):
        self.label.config(text=f"Scannez la face {self.face_index} du Rubik's Cube")
        self.next_button.config(state=tk.DISABLED)

    def show_results(self):
        result_text = ""
        for i, face in enumerate(self.face_colors):
            result_text += f"Face {i + 1}:\n"
            result_text += "\n".join([" ".join(row) for row in face]) + "\n\n"
        messagebox.showinfo("Couleurs scannées", result_text)

    def on_closing(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.root.quit()

    def update_frame(self):
        while True:
            ret, self.frame = self.cap.read()
            if ret:
                cv2.imshow("Rubik's Cube Face Detection", self.frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

root = tk.Tk()
app = RubiksCubeScanner(root)
root.mainloop()
