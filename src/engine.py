# Minimax, Alpha-Beta pruning, & move search logic

import chess
import random

board = chess.Board()

turn_color = "White" if board.turn == chess.WHITE else "Black"

print(board)

def randomBotMove(board):
    legal_moves = list(board.legal_moves)

    random.shuffle(legal_moves)  # Shuffle the moves to add randomness

    return legal_moves[0] if legal_moves else None

while not board.is_game_over():
    move = chess.Move.from_uci(input(f"{turn_color}'s move (in UCI format): "))
    if move in board.legal_moves:
        board.push(move)
        print(board)
    else:
        print("Illegal move. Try again.")

    board.push(randomBotMove(board))
    print(board)


