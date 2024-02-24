from sudoku import *

import time
import multiprocessing

def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    start = time.time()
    solve(grid)
    end = time.time()
    print(f"{filename}: {end-start}")


if __name__ == "__main__":
    spisok = ["hard_puzzles/hardpuzzle"+str(i)+".txt" for i in range(1,96)]
    for filename in spisok:
        p = multiprocessing.Process(target=run_solve, args=(filename,))
        p.start()
