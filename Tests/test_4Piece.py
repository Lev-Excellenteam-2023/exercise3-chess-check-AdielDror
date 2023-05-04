from Piece import Knight, Rook, Bishop, Queen, Pawn, King
from ai_engine import chess_ai
from chess_engine import game_state
from enums import Player


# Unit_test
def test_get_valid_peaceful_moves_1():
    game_state_1 = game_state()
    white_knight_1 = Knight('n', 3, 4, Player.PLAYER_1)
    game_state_1.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), white_knight_1, (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    assert white_knight_1.get_valid_peaceful_moves(game_state_1) == [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6),
                                                                     (5, 5), (5, 3)]


def test_get_valid_peaceful_moves_2():
    game_state_1 = game_state()
    white_knight_1 = Knight('n', 0, 0, Player.PLAYER_1)
    game_state_1.board = [[white_knight_1, (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    assert white_knight_1.get_valid_peaceful_moves(game_state_1) == [(1, 2), (2, 1)]


def test_get_valid_peaceful_moves_3():
    game_state_1 = game_state()
    white_knight_1 = Knight('n', 7, 3, Player.PLAYER_1)
    game_state_1.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), white_knight_1, (), (), (), ()]]

    assert white_knight_1.get_valid_peaceful_moves(game_state_1) == [(5, 2), (5, 4), (6, 1), (6, 5)]


def test_get_valid_piece_takes_1():
    game_state_1 = game_state()
    white_knight_1 = Knight('n', 3, 4, Player.PLAYER_1)
    game_state_1.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), white_knight_1, (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    assert white_knight_1.get_valid_piece_takes(game_state_1) == []


def test_get_valid_piece_takes_2():
    game_state_1 = game_state()
    white_knight_1 = Knight('n', 2, 2, Player.PLAYER_1)
    white_pawn_1 = Pawn('p', 4, 1, Player.PLAYER_1)
    white_pawn_2 = Pawn('p', 4, 3, Player.PLAYER_2)
    white_bishop = Bishop('b', 1, 4, Player.PLAYER_2)
    game_state_1.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), white_bishop, (), (), ()],
                          [(), (), white_knight_1, (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), white_pawn_1, (), white_pawn_2, (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    assert white_knight_1.get_valid_piece_takes(game_state_1) == [(1, 4), (4, 3)]


def test_get_valid_piece_takes_3():
    game_state_1 = game_state()
    black_knight_1 = Knight('n', 2, 0, Player.PLAYER_2)
    black_queen = Queen('q', 0, 1, Player.PLAYER_2)
    white_king = King('k', 3, 2, Player.PLAYER_1)
    white_pawn_1 = Pawn('p', 1, 2, Player.PLAYER_1)
    white_pawn_2 = Pawn('p', 4, 1, Player.PLAYER_1)
    white_pawn_3 = Pawn('p', 3, 1, Player.PLAYER_1)
    game_state_1.board = [[(), black_queen, (), (), (), (), (), ()],
                          [(), (), white_pawn_1, (), (), (), ()],
                          [black_knight_1, (), (), (), (), (), (), ()],
                          [(), white_pawn_3, white_king, (), (), (), (), ()],
                          [(), white_pawn_2, (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    assert black_knight_1.get_valid_piece_takes(game_state_1) == [(1, 2), (3, 2), (4, 1)]


# Integration_test
def test_get_valid_piece_moves():
    game_state_1 = game_state()
    black_knight_1 = Knight('n', 5, 3, Player.PLAYER_2)
    white_pawn_1 = Pawn('p', 4, 1, Player.PLAYER_1)
    white_pawn_2 = Pawn('p', 4, 3, Player.PLAYER_2)
    black_bishop = Bishop('b', 3, 4, Player.PLAYER_2)
    white_knight_1 = Knight('n', 7, 2, Player.PLAYER_1)
    game_state_1.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), black_bishop, (), (), ()],
                          [(), white_pawn_1, (), white_pawn_2, (), (), (), ()],
                          [(), (), (), black_knight_1, (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), white_knight_1, (), (), (), (), ()]]

    assert black_knight_1.get_valid_piece_moves(game_state_1) == [(3, 2), (4, 5), (6, 1), (6, 5), (7, 4), (4, 1),
                                                                  (7, 2)]


def test_evaluate_board():
    game_state_1 = game_state()
    chess_ai_1 = chess_ai()
    black_knight_1 = Knight('n', 5, 3, Player.PLAYER_2)
    white_pawn_1 = Pawn('p', 4, 1, Player.PLAYER_1)
    white_pawn_2 = Pawn('p', 4, 3, Player.PLAYER_2)
    black_bishop = Bishop('b', 3, 4, Player.PLAYER_2)
    white_knight_1 = Knight('n', 7, 2, Player.PLAYER_1)
    black_rook_1 = Rook('r', 0, 0, Player.PLAYER_2)
    black_queen = Queen('q', 0, 4, Player.PLAYER_2)
    white_king = King('k', 2, 0, Player.PLAYER_1)
    game_state_1.board = [[black_rook_1, (), (), (), black_queen, (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [white_king, (), (), (), (), (), (), ()],
                          [(), (), (), (), black_bishop, (), (), ()],
                          [(), white_pawn_1, (), white_pawn_2, (), (), (), ()],
                          [(), (), (), black_knight_1, (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), white_knight_1, (), (), (), (), ()]]

    assert chess_ai_1.evaluate_board(game_state_1, "white") == -820


# System_test
def test():
    game_state_1 = game_state()

    # Initialize White pieces
    white_rook_1 = Rook('r', 0, 0, Player.PLAYER_1)
    white_rook_2 = Rook('r', 0, 7, Player.PLAYER_1)
    white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
    white_knight_2 = Knight('n', 0, 6, Player.PLAYER_1)
    white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
    white_bishop_2 = Bishop('b', 0, 5, Player.PLAYER_1)
    white_queen = Queen('q', 0, 4, Player.PLAYER_1)
    white_king = King('k', 0, 3, Player.PLAYER_1)
    white_pawn_1 = Pawn('p', 1, 0, Player.PLAYER_1)
    white_pawn_2 = Pawn('p', 1, 1, Player.PLAYER_1)
    white_pawn_3 = Pawn('p', 1, 2, Player.PLAYER_1)
    white_pawn_4 = Pawn('p', 1, 3, Player.PLAYER_1)
    white_pawn_5 = Pawn('p', 1, 4, Player.PLAYER_1)
    white_pawn_6 = Pawn('p', 1, 5, Player.PLAYER_1)
    white_pawn_7 = Pawn('p', 1, 6, Player.PLAYER_1)
    white_pawn_8 = Pawn('p', 1, 7, Player.PLAYER_1)

    # Initialize Black Pieces
    black_rook_1 = Rook('r', 7, 0, Player.PLAYER_2)
    black_rook_2 = Rook('r', 7, 7, Player.PLAYER_2)
    black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
    black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
    black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
    black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
    black_queen = Queen('q', 7, 4, Player.PLAYER_2)
    black_king = King('k', 7, 3, Player.PLAYER_2)
    black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
    black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
    black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)
    black_pawn_4 = Pawn('p', 6, 3, Player.PLAYER_2)
    black_pawn_5 = Pawn('p', 6, 4, Player.PLAYER_2)
    black_pawn_6 = Pawn('p', 6, 5, Player.PLAYER_2)
    black_pawn_7 = Pawn('p', 6, 6, Player.PLAYER_2)
    black_pawn_8 = Pawn('p', 6, 7, Player.PLAYER_2)

    game_state_1.board = [
        [white_rook_1, white_knight_1, white_bishop_1, white_king, white_queen, white_bishop_2, white_knight_2,
         white_rook_2],
        [white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7,
         white_pawn_8],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4, black_pawn_5, black_pawn_6, black_pawn_7,
         black_pawn_8],
        [black_rook_1, black_knight_1, black_bishop_1, black_king, black_queen, black_bishop_2, black_knight_2,
         black_rook_2]
    ]

    game_state_1.move_piece((1, 2), (2, 2), False)
    game_state_1.move_piece((6, 3), (4, 3), False)
    game_state_1.move_piece((1, 1), (3, 1), False)
    game_state_1.move_piece((7, 4), (3, 0), False)
    assert game_state_1.checkmate_stalemate_checker() == 0
