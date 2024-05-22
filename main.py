from rubik.cube import Cube
from rubik.solve import Solver
from rubik.optimize import optimize_moves
import tkinter as tk
import json


def get_json_notation():
    with open("cube_notation.json") as file:
        data = json.load(file)
    return data


def get_cube():
    print("Enter the colors for the cube in the following order:")
    print("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
    print("O = Orange, Y = Yellow, W = White, G = Green, B = Blue, R = Red")
    colors = input("Enter the colors: ").strip()
    cube_to_solve = Cube(colors)
    print("Here is the cube you entered:")
    print(cube_to_solve)
    return cube_to_solve


def get_moves(solver):
    optimized_moves = optimize_moves(solver.moves)
    return optimized_moves


def solve_cube(cube_string):
    solver = Solver(cube_string)
    solver.solve()
    solved_moves = optimize_moves(solver.moves)

    print("Do you want to get the moves (y/n)?")
    response = input().strip().lower()
    if response == "y":
        moves_notation = moves_to_notation(solved_moves)
        print(moves_notation)
        
    print("Do you want to display the moves in an image (y/n)?")
    response = input().strip().lower()
    if response == "y":
        moves_to_image(solved_moves)


def moves_to_notation(moves):
    data = get_json_notation()
    notation = ""
    for move in moves:
        notation += data[move] + "\n"
    return notation


def moves_to_image(moves):
    window = tk.Tk()
    window.geometry("400x400")
    window.title("Rubik's Cube")

    top_frame = tk.Frame(window)
    top_frame.pack()
    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side=tk.BOTTOM)

    label_moves = tk.Label(bottom_frame, text="0 / 0")
    label_moves.pack()

    button_prev = tk.Button(bottom_frame, text="Previous Image", fg="red")
    button_next = tk.Button(bottom_frame, text="Next Image", fg="blue")
    button_prev.pack(side=tk.LEFT)
    button_next.pack(side=tk.LEFT)

    current_move = 0
    total_moves = len(moves)

    def associate_moves_with_images(current_move_index):
        data = get_json_notation()
        current_move_str = moves[current_move_index]
        img_path = f"./images/{current_move_str}.png"
        img = tk.PhotoImage(file=img_path)
        label.config(image=img)
        label.image = img
        text.config(text=data[current_move_str])
        label_moves.config(text=f"{current_move_index + 1} / {total_moves}")

    def button_next_command():
        nonlocal current_move
        current_move += 1
        if current_move == total_moves:
            current_move = 0
        associate_moves_with_images(current_move)

    def button_prev_command():
        nonlocal current_move
        current_move -= 1
        if current_move < 0:
            current_move = total_moves - 1
        associate_moves_with_images(current_move)

    button_prev.config(command=button_prev_command)
    button_next.config(command=button_next_command)

    initial_img = tk.PhotoImage(file="./images/rubik.png")
    initial_img = initial_img.subsample(2)
    label = tk.Label(top_frame, image=initial_img)
    label.pack()

    text = tk.Label(top_frame, text="This is a Rubik's Cube")
    text.pack()

    associate_moves_with_images(current_move)
    window.mainloop()


def main():
    cube = get_cube()
    solve_cube(cube)


if __name__ == "__main__":
    main()
