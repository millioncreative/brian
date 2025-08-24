import random
import time

BASE = 3
SIDE = BASE * BASE

def pattern(r, c):
    return (BASE * (r % BASE) + r // BASE + c) % SIDE

def shuffle(s):
    return random.sample(s, len(s))

def generate_full_board():
    r_base = range(BASE)
    rows = [g * BASE + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * BASE + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, SIDE + 1))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]

def remove_cells(board, difficulty):
    puzzle = [row[:] for row in board]
    total_cells = SIDE * SIDE
    min_clues = 17
    max_remove = total_cells - min_clues
    remove_count = int(max_remove * (difficulty / 100))
    positions = [(r, c) for r in range(SIDE) for c in range(SIDE)]
    random.shuffle(positions)
    for i in range(remove_count):
        r, c = positions[i]
        puzzle[r][c] = 0
    return puzzle

def print_board(board):
    for r in range(SIDE):
        row = " ".join(str(num) if num != 0 else '.' for num in board[r])
        print(row)

def play(difficulty=50):
    board = generate_full_board()
    puzzle = remove_cells(board, difficulty)
    start = time.time()
    while True:
        print_board(puzzle)
        if puzzle == board:
            end = time.time()
            print(f"Solved in {end - start:.2f} seconds")
            break
        inp = input("Enter row col value (e.g., 1 3 5) or q to quit: ")
        if inp.lower().startswith('q'):
            print("Quit the game")
            break
        try:
            r, c, v = map(int, inp.split())
            if board[r-1][c-1] == v:
                puzzle[r-1][c-1] = v
            else:
                print("Incorrect value")
        except Exception:
            print("Invalid input")

if __name__ == "__main__":
    try:
        difficulty = int(input("Enter difficulty (0-100): "))
    except Exception:
        difficulty = 50
    play(difficulty)
