# Minimax, Alpha-Beta pruning, & move search logic

import chess
import random

board = chess.Board()


def side_name(color):
    return "White" if color == chess.WHITE else "Black"


def random_bot_move(board_state):
    legal_moves = list(board_state.legal_moves)
    if not legal_moves:
        return None
    random.shuffle(legal_moves)
    return legal_moves[0]


def get_game_status(board_state):
    if board_state.is_checkmate():
        winner = side_name(not board_state.turn)
        loser = side_name(board_state.turn)
        return {
            "game_over": True,
            "type": "checkmate",
            "message": f"Checkmate! {winner} wins by defeating {loser}.",
        }

    if board_state.is_stalemate():
        return {
            "game_over": True,
            "type": "stalemate",
            "message": "Stalemate! It's a draw.",
        }

    if board_state.is_insufficient_material():
        return {
            "game_over": True,
            "type": "draw",
            "message": "Draw due to insufficient material.",
        }

    if board_state.can_claim_threefold_repetition():
        return {
            "game_over": True,
            "type": "draw",
            "message": "Draw by threefold repetition.",
        }

    if board_state.can_claim_fifty_moves():
        return {
            "game_over": True,
            "type": "draw",
            "message": "Draw by the fifty-move rule.",
        }

    if board_state.is_check():
        return {
            "game_over": False,
            "type": "check",
            "message": f"{side_name(board_state.turn)} is in check.",
        }

    return {
        "game_over": False,
        "type": "normal",
        "message": "Game continues.",
    }


def play_game():
    global board
    board = chess.Board()
    print(board)

    while not board.is_game_over():
        current_player = side_name(board.turn)

        # Get user input for the move
        move_uci = input(f"{current_player}'s move (UCI, e.g. e2e4): ")
        move = chess.Move.from_uci(move_uci)

        # Check if the move is legal
        if move not in board.legal_moves:
            print("Illegal move. Try again.")
            continue

        # Push the move to the board and display the updated board
        board.push(move)
        print(f"{current_player} plays: {move}")
        print(board)

        # Check the game status after the player's move
        status = get_game_status(board)
        print(status["message"])
        if status["game_over"]:
            break

        # Bot's turn
        bot_move = random_bot_move(board)
        if bot_move is None:
            print("No legal moves available for the bot.")
            break

        board.push(bot_move)
        print(f"Bot plays: {bot_move}")
        print(board)

        status = get_game_status(board)
        print(status["message"])
        if status["game_over"]:
            break

    print("Game over.")

