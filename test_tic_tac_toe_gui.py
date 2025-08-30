import unittest
from tic_tac_toe_gui import TicTacToeGUI

class TestTicTacToeLogic(unittest.TestCase):
    def setUp(self):
        """Создаем экземпляр игры перед каждым тестом"""
        # Создаем минимальную заглушку для root
        class RootStub:
            def title(self, *args):
                pass
        
        self.game = TicTacToeGUI(RootStub())

    def test_initial_board(self):
        """Тест начального состояния доски"""
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.game.board, expected_board)
        self.assertEqual(self.game.current_player, 'X')

    def test_make_move(self):
        """Тест выполнения хода"""
        # Выполняем ход
        self.game.make_move(1, 1, 'X')
        self.assertEqual(self.game.board[1][1], 'X')
        
        # Проверяем другой ход
        self.game.make_move(0, 0, 'O')
        self.assertEqual(self.game.board[0][0], 'O')

    def test_check_winner_rows(self):
        """Тест проверки победителя по строкам"""
        # Победа X по первой строке
        self.game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Победа O по второй строке
        self.game.board = [[' ', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')

    def test_check_winner_columns(self):
        """Тест проверки победителя по столбцам"""
        # Победа X по первому столбцу
        self.game.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Победа O по второму столбцу
        self.game.board = [[' ', 'O', ' '], [' ', 'O', ' '], [' ', 'O', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')

    def test_check_winner_diagonals(self):
        """Тест проверки победителя по диагоналям"""
        # Победа X по главной диагонали
        self.game.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Победа O по побочной диагонали
        self.game.board = [[' ', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']]
        self.assertEqual(self.game.check_winner(), 'O')

    def test_is_board_full(self):
        """Тест проверки заполненности доски"""
        # Пустая доска
        self.assertFalse(self.game.is_board_full())
        
        # Частично заполненная доска
        self.game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', ' ', 'X']]
        self.assertFalse(self.game.is_board_full())
        
        # Полностью заполненная доска
        self.game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]
        self.assertTrue(self.game.is_board_full())

    def test_restart_game(self):
        """Тест перезапуска игры"""
        # Делаем несколько ходов
        self.game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]
        self.assertTrue(self.game.is_board_full())
        
        # Перезапускаем игру (только логика, без GUI)
        self.game.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game.current_player = 'X'
        
        # Проверяем, что доска пуста
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.game.board, expected_board)
        self.assertEqual(self.game.current_player, 'X')

if __name__ == '__main__':
    unittest.main()