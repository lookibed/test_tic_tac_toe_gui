import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_initial_board(self):
        """Тест начального состояния доски"""
        game = TicTacToe()
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.board, expected_board)
        self.assertEqual(game.current_player, 'X')

    def test_make_move(self):
        """Тест выполнения хода"""
        game = TicTacToe()
        # Успешный ход
        result = game.make_move(1, 1)
        self.assertTrue(result)
        self.assertEqual(game.board[1][1], 'X')
        
        # Попытка сделать ход в занятую клетку
        result = game.make_move(1, 1)
        self.assertFalse(result)
        
        # Переключение игрока и новый ход
        game.switch_player()
        result = game.make_move(0, 0)
        self.assertTrue(result)
        self.assertEqual(game.board[0][0], 'O')

    def test_check_winner_rows(self):
        """Тест проверки победителя по строкам"""
        game = TicTacToe()
        # Победа X по первой строке
        game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.check_winner(), 'X')
        
        # Победа O по второй строке
        game.board = [[' ', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']]
        self.assertEqual(game.check_winner(), 'O')

    def test_check_winner_columns(self):
        """Тест проверки победителя по столбцам"""
        game = TicTacToe()
        # Победа X по первому столбцу
        game.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertEqual(game.check_winner(), 'X')
        
        # Победа O по второму столбцу
        game.board = [[' ', 'O', ' '], [' ', 'O', ' '], [' ', 'O', ' ']]
        self.assertEqual(game.check_winner(), 'O')

    def test_check_winner_diagonals(self):
        """Тест проверки победителя по диагоналям"""
        game = TicTacToe()
        # Победа X по главной диагонали
        game.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertEqual(game.check_winner(), 'X')
        
        # Победа O по побочной диагонали
        game.board = [[' ', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']]
        self.assertEqual(game.check_winner(), 'O')

    def test_is_board_full(self):
        """Тест проверки заполненности доски"""
        game = TicTacToe()
        # Пустая доска
        self.assertFalse(game.is_board_full())
        
        # Частично заполненная доска
        game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', ' ', 'X']]
        self.assertFalse(game.is_board_full())
        
        # Полностью заполненная доска
        game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]
        self.assertTrue(game.is_board_full())

    def test_get_empty_cells(self):
        """Тест получения пустых клеток"""
        game = TicTacToe()
        # Пустая доска
        empty_cells = game.get_empty_cells()
        self.assertEqual(len(empty_cells), 9)
        
        # Доска с одним ходом
        game.board = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        empty_cells = game.get_empty_cells()
        self.assertEqual(len(empty_cells), 8)
        self.assertNotIn((0, 0), empty_cells)

    def test_switch_player(self):
        """Тест переключения игроков"""
        game = TicTacToe()
        self.assertEqual(game.current_player, 'X')
        game.switch_player()
        self.assertEqual(game.current_player, 'O')
        game.switch_player()
        self.assertEqual(game.current_player, 'X')

if __name__ == '__main__':
    unittest.main()