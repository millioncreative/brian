import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
import sudoku


def test_generate_full_board_size_and_values():
    board = sudoku.generate_full_board()
    assert len(board) == 9
    assert all(len(row) == 9 for row in board)
    for row in board:
        for val in row:
            assert 1 <= val <= 9


def test_remove_cells_difficulty_bounds():
    board = sudoku.generate_full_board()
    puzzle_easy = sudoku.remove_cells(board, 0)
    puzzle_hard = sudoku.remove_cells(board, 100)
    easy_clues = sum(val != 0 for row in puzzle_easy for val in row)
    hard_clues = sum(val != 0 for row in puzzle_hard for val in row)
    assert easy_clues == 81
    assert hard_clues == 17

