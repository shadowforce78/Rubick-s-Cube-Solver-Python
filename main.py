from rubik import solve
from rubik.cube import Cube
from rubik.solve import Solver
import time
from rubik.optimize import optimize_moves

def get_cube():
    # Schema = OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR
    # Schema 2 = BGBGBGBGBOROWYWRORYWYRORYWYOROWYWOROWYWRORYWYGBGBGBGBG (cross every face)
    # O = Orange, Y = Yellow, W = White, G = Green, B = Blue, R = Red
    #
        #     OOO
        #     OOO
        #     OOO
        # YYY WWW GGG BBB
        # YYY WWW GGG BBB
        # YYY WWW GGG BBB
        #     RRR
        #     RRR
        #     RRR
    print("Enter the colors for the cube in the following order:")
    print(Cube("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"))
    print("O = Orange, Y = Yellow, W = White, G = Green, B = Blue, R = Red")
    colors = input("Enter the colors: ")
    cube_to_solve = Cube(colors)
    print("Here is the cube you entered:")
    print(cube_to_solve)

    return cube_to_solve

def solve_cube(cube_string):
    successes = 0
    failures = 0

    avg_opt_moves = 0.0
    avg_moves = 0.0
    avg_time = 0.0
    while True:
        C = cube_string 
        solver = Solver(C)

        start = time.time()
        solver.solve()
        duration = time.time() - start

        if C.is_solved():
            opt_moves = optimize_moves(solver.moves)
            successes += 1
            avg_moves = (avg_moves * (successes - 1) + len(solver.moves)) / float(successes)
            avg_time = (avg_time * (successes - 1) + duration) / float(successes)
            avg_opt_moves = (avg_opt_moves * (successes - 1) + len(opt_moves)) / float(successes)
        else:
            failures += 1
            print(f"Failed ({successes + failures}): {C.flat_str()}")

        total = successes + failures
        if total == 1 or total % 100 == 0:
            pass_percentage = 100 * successes / total
            print(f"{total}: {successes} successes ({pass_percentage:0.3f}% passing)"
                  f" avg_moves={avg_moves:0.3f} avg_opt_moves={avg_opt_moves:0.3f}"
                  f" avg_time={avg_time:0.3f}s")

        print("Do you want to get the moves (y/n)?")
        response = input()
        get_moves = solver.moves
        if response == "y":
            print(get_moves)
        print("Do you want to continue (y/n)?")
        response = input()
        if response == "n":
            break
    

def main():
    cube_string = get_cube()
    solve_cube(cube_string)

if __name__ == "__main__":
    solve.DEBUG = False
    main()