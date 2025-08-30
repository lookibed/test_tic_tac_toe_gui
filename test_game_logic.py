import unittest

# Импортируем только логику игры без GUI компонентов
def check_winner(board):
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

class TestGameLogic(unittest.TestCase):
    def test_check_winner_rows(self):
        """Тест проверки победителя по строкам"""
        # Победа X по первой строке
        board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(check_winner(board), 'X')
        
        # Победа O по второй строке
        board = [[' ', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']]
        self.assertEqual(check_winner(board), 'O')

    def test_check_winner_columns(self):
        """Тест проверки победителя по столбцам"""
        # Победа X по первому столбцу
        board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertEqual(check_winner(board), 'X')
        
        # Победа O по второму столбцу
        board = [[' ', 'O', ' '], [' ', 'O', ' '], [' ', 'O', ' ']]
        self.assertEqual(check_winner(board), 'O')

    def test_check_winner_diagonals(self):
        """Тест проверки победителя по диагоналям"""
        # Победа X по главной диагонали
        board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertEqual(check_winner(board), 'X')
        
        # Победа O по побочной диагонали
        board = [[' ', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']]
        self.assertEqual(check_winner(board), 'O')

    def test_is_board_full(self):
        """Тест проверки заполненности доски"""
        # Пустая доска
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertFalse(is_board_full(board))
        
        # Частично заполненная доска
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', ' ', 'X']]
        self.assertFalse(is_board_full(board))
        
        # Полностью заполненная доска
        board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]
        self.assertTrue(is_board_full(board))

if __name__ == '__main__':
    unittest.main()