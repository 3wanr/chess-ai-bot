# Minimax, Alpha-Beta pruning, & move search logic

class gameState:
    def __init__(self):
        self.board = ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br",
                      "bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp",
                      "--", "--", "--", "--", "--", "--", "--", "--",
                      "--", "--", "--", "--", "--", "--", "--", "--",
                      "--", "--", "--", "--", "--", "--", "--", "--",
                      "--", "--", "--", "--", "--", "--", "--", "--",
                      "wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp",
                      "wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"
                      ]
        self.turn = 'white'
        self.selected_piece = None
        self.valid_moves = []
        self.move_log = []
        self.white_king_location = (7, 4)
        self.black_king_location = (0, 4)
        self.checkmate = False
        self.stalemate = False
        self.in_check = False
        self.pins = []
        self.checks = []

    def valid_queen_move(start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Check for valid queen move (diagonal or straight)
        if row_diff == col_diff or start_row == end_row or start_col == end_col:
            return True

        return False

    def valid_rook_move(start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check for valid rook move (straight)
        if start_row == end_row or start_col == end_col:
            return True

        return False

    def valid_bishop_move(start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Check for valid bishop move (diagonal)
        if row_diff == col_diff:
            return True

        return False

    def valid_knight_move(start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Check for valid knight move (L-shape)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return True

        return False

    def valid_king_move(start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Check for valid king move (one square in any direction)
        if row_diff <= 1 and col_diff <= 1:
            return True

        return False

    def valid_pawn_move(piece, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        direction = -1 if "white" in piece else 1  # White moves up, black moves down
        start_row_initial = 6 if "white" in piece else 1  # Initial row for pawns

        # Check for valid pawn move (one square forward)
        if start_col == end_col and end_row == start_row + direction:
            return True

        # Check for valid pawn move (two squares forward from initial position)
        if start_col == end_col and start_row == start_row_initial and end_row == start_row + 2 * direction:
            return True

        # Check for valid pawn capture (diagonal)
        if abs(end_col - start_col) == 1 and end_row == start_row + direction:
            return True

        return False

    def get_all_valid_moves(self):
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row * 8 + col]
                if piece != "--":
                    piece_moves = self.get_piece_valid_moves(piece, (row, col))
                    moves.extend(piece_moves)
        return moves

    
    
    def make_move(self, start_pos, end_pos):
        piece = self.board[start_pos[0] * 8 + start_pos[1]]
        self.board[end_pos[0] * 8 + end_pos[1]] = piece
        self.board[start_pos[0] * 8 + start_pos[1]] = "--"
        self.move_log.append((start_pos, end_pos, piece))
        self.turn = 'black' if self.turn == 'white' else 'white'

        # Update king's location if moved
        if piece == "wk":
            self.white_king_location = end_pos
        elif piece == "bk":
            self.black_king_location = end_pos

        

    

    