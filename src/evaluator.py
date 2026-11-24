# Material counts, PSTs, & static evaluation heuristics

import chess
import numpy as np

def construct_X(board):
    x_vector = [0] * 64 * 12  # 64 squares, 12 piece types (6 for each color)

    for square in range(64):
        piece = board.piece_at(square)
        if piece is not None:
            piece_type = piece.piece_type - 1  # piece_type is 1-6, we want 0-5
            color_offset = 0 if piece.color == chess.WHITE else 6
            index = square * 12 + piece_type + color_offset
            x_vector[index] = 1

    return np.array(x_vector)
 
def construct_features(board, eval_entry):
    """
    Construct a feature vector for a given board position and evaluation entry.
    Features include material counts, piece-square tables (PSTs), and static evaluation heuristics.
    """
    features = []

    # Piece-square tables (PSTs)
    pst_features = get_pst_features(board)
    features.extend(pst_features)


    return np.array(features)

def get_pst_features(board):
    