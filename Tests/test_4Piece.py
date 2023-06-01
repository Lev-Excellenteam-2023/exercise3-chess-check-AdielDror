from unittest.mock import patch
from unittest import mock

from Piece import Knight, Rook, Bishop, Queen, Pawn, King
from chess_engine import game_state
from enums import Player


# Unit_test
def test_get_valid_peaceful_moves_1():
    game_state_1 = mock.Mock()

    white_knight = mock.Mock(spec=Knight)
    white_knight.get_valid_peaceful_moves.return_value = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6),
                                                          (5, 5), (5, 3)]

    game_state_1.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), white_knight, (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    moves = white_knight.get_valid_peaceful_moves(game_state_1)

    assert moves == [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6),
                     (5, 5), (5, 3)]


def test_get_valid_peaceful_moves_2():
    game_state_2 = mock.Mock()

    white_knight = mock.Mock(spec=Knight)
    white_knight.get_valid_peaceful_moves.return_value = [(1, 2), (2, 1)]

    game_state_2.board = [[white_knight, (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    moves = white_knight.get_valid_peaceful_moves(game_state_2)

    assert moves == [(1, 2), (2, 1)]


def test_get_valid_peaceful_moves_3():
    game_state_3 = mock.Mock()

    white_knight = mock.Mock(spec=Knight)
    white_knight.get_valid_peaceful_moves.return_value = [(5, 2), (5, 4), (6, 1), (6, 5)]

    game_state_3.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), white_knight, (), (), (), ()]]

    moves = white_knight.get_valid_peaceful_moves(game_state_3)

    assert moves == [(5, 2), (5, 4), (6, 1), (6, 5)]


def test_get_valid_piece_takes_1():
    game_state_1 = mock.Mock()

    white_knight = mock.Mock(spec=Knight)
    white_knight.get_valid_piece_takes.return_value = []

    game_state_1.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), white_knight, (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    assert white_knight.get_valid_piece_takes(game_state_1) == []


def test_get_valid_piece_takes_2():
    game_state_2 = mock.Mock()

    white_knight = mock.Mock(spec=Knight)
    white_bishop = mock.Mock(spec=Bishop)
    white_pawn_1 = mock.Mock(spec=Pawn)
    white_pawn_2 = mock.Mock(spec=Pawn)

    white_knight.get_valid_piece_takes.return_value = [(1, 4), (4, 3)]

    game_state_2.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), white_bishop, (), (), ()],
                          [(), (), white_knight, (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), white_pawn_1, (), white_pawn_2, (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    assert white_knight.get_valid_piece_takes(game_state_2) == [(1, 4), (4, 3)]


def test_get_valid_piece_takes_3():
    game_state_3 = mock.Mock()

    black_knight = mock.Mock(spec=Knight)
    black_queen = mock.Mock(spec=Queen)
    white_king = mock.Mock(spec=King)
    white_pawn_1 = mock.Mock(spec=Pawn)
    white_pawn_2 = mock.Mock(spec=Pawn)
    white_pawn_3 = mock.Mock(spec=Pawn)

    black_knight.get_valid_piece_takes.return_value = [(1, 2), (3, 2), (4, 1)]

    game_state_3.board = [[(), black_queen, (), (), (), (), (), ()],
                          [(), (), white_pawn_1, (), (), (), ()],
                          [black_knight, (), (), (), (), (), (), ()],
                          [(), white_pawn_3, white_king, (), (), (), (), ()],
                          [(), white_pawn_2, (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()]]

    assert black_knight.get_valid_piece_takes(game_state_3) == [(1, 2), (3, 2), (4, 1)]


# Integration_test
def test_get_valid_piece_moves():
    game_state_1 = mock.Mock()

    black_knight = mock.Mock(spec=Knight)
    black_bishop = mock.Mock(spec=Bishop)
    white_knight = mock.Mock(spec=Knight)
    white_pawn_1 = mock.Mock(spec=Pawn)
    white_pawn_2 = mock.Mock(spec=Pawn)

    black_knight.get_valid_piece_moves.return_value = [(3, 2), (4, 5), (6, 1), (6, 5), (7, 4), (4, 1),
                                                       (7, 2)]

    game_state_1.board = [[(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), (), (), black_bishop, (), (), ()],
                          [(), white_pawn_1, (), white_pawn_2, (), (), (), ()],
                          [(), (), (), black_knight, (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), white_knight, (), (), (), (), ()]]

    assert black_knight.get_valid_piece_moves(game_state_1) == [(3, 2), (4, 5), (6, 1), (6, 5), (7, 4), (4, 1),
                                                                (7, 2)]


def test_evaluate_board():
    game_state_2 = mock.Mock()
    chess_ai_1 = mock.Mock()

    black_knight = mock.Mock(spec=Knight)
    black_bishop = mock.Mock(spec=Bishop)
    black_rook = mock.Mock(spec=Rook)
    black_queen = mock.Mock(spec=Queen)
    white_knight = mock.Mock(spec=Knight)
    white_king = mock.Mock(spec=King)
    white_pawn_1 = mock.Mock(spec=Pawn)
    white_pawn_2 = mock.Mock(spec=Pawn)

    chess_ai_1.evaluate_board.return_value = -820

    game_state_2.board = [[black_rook, (), (), (), black_queen, (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [white_king, (), (), (), (), (), (), ()],
                          [(), (), (), (), black_bishop, (), (), ()],
                          [(), white_pawn_1, (), white_pawn_2, (), (), (), ()],
                          [(), (), (), black_knight, (), (), (), ()],
                          [(), (), (), (), (), (), (), ()],
                          [(), (), white_knight, (), (), (), (), ()]]

    assert chess_ai_1.evaluate_board(game_state_2, "white") == -820


# System_test
def initialize_game_state():
    game_state_1 = game_state()

    # Initialize the empty board
    game_state_1.board = [[Player.EMPTY] * 8 for _ in range(8)]

    # Initialize White pieces
    game_state_1.board[0][0] = Rook('r', 0, 0, Player.PLAYER_1)
    game_state_1.board[0][7] = Rook('r', 0, 7, Player.PLAYER_1)
    game_state_1.board[0][1] = Knight('n', 0, 1, Player.PLAYER_1)
    game_state_1.board[0][6] = Knight('n', 0, 6, Player.PLAYER_1)
    game_state_1.board[0][2] = Bishop('b', 0, 2, Player.PLAYER_1)
    game_state_1.board[0][5] = Bishop('b', 0, 5, Player.PLAYER_1)
    game_state_1.board[0][4] = Queen('q', 0, 4, Player.PLAYER_1)
    game_state_1.board[0][3] = King('k', 0, 3, Player.PLAYER_1)
    for col in range(8):
        game_state_1.board[1][col] = Pawn('p', 1, col, Player.PLAYER_1)

    # Initialize Black pieces
    game_state_1.board[7][0] = Rook('r', 7, 0, Player.PLAYER_2)
    game_state_1.board[7][7] = Rook('r', 7, 7, Player.PLAYER_2)
    game_state_1.board[7][1] = Knight('n', 7, 1, Player.PLAYER_2)
    game_state_1.board[7][6] = Knight('n', 7, 6, Player.PLAYER_2)
    game_state_1.board[7][2] = Bishop('b', 7, 2, Player.PLAYER_2)
    game_state_1.board[7][5] = Bishop('b', 7, 5, Player.PLAYER_2)
    game_state_1.board[7][4] = Queen('q', 7, 4, Player.PLAYER_2)
    game_state_1.board[7][3] = King('k', 7, 3, Player.PLAYER_2)
    for col in range(8):
        game_state_1.board[6][col] = Pawn('p', 6, col, Player.PLAYER_2)

    return game_state_1


def test():
    with patch('chess_engine.game_state') as mock_game_state:
        instance = mock_game_state.return_value
        instance.move_piece.side_effect = [
            None,  # Mock move_piece for the first call
            None,  # Mock move_piece for the second call
            None,  # Mock move_piece for the third call
            None  # Mock move_piece for the fourth call
        ]
    game_state_1 = initialize_game_state()

    game_state_1.move_piece((1, 2), (2, 2), False)
    game_state_1.move_piece((6, 3), (4, 3), False)
    game_state_1.move_piece((1, 1), (3, 1), False)
    game_state_1.move_piece((7, 4), (3, 0), False)
    assert game_state_1.checkmate_stalemate_checker() == 0
