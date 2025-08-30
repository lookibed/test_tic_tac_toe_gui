import random
import sys

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        print("\n   0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i}  {' | '.join(row)}")
            if i < 2:
                print("  -----------")

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        # Проверка строк
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Проверка столбцов
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_empty_cells(self):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    empty_cells.append((i, j))
        return empty_cells

    def ai_move(self):
        # Простая стратегия ИИ:
        # 1. Попытаться выиграть
        # 2. Блокировать победу игрока
        # 3. Сделать случайный ход

        # Проверим, можем ли мы выиграть следующим ходом
        for i, j in self.get_empty_cells():
            self.board[i][j] = 'O'
            if self.check_winner() == 'O':
                self.board[i][j] = ' '  # Отменяем ход для проверки
                return (i, j)
            self.board[i][j] = ' '  # Отменяем ход

        # Проверим, нужно ли блокировать игрока
        for i, j in self.get_empty_cells():
            self.board[i][j] = 'X'
            if self.check_winner() == 'X':
                self.board[i][j] = ' '  # Отменяем ход для проверки
                return (i, j)
            self.board[i][j] = ' '  # Отменяем ход

        # Если нет срочных ходов, выбираем случайную пустую клетку
        if self.get_empty_cells():
            return random.choice(self.get_empty_cells())
        return None

    def play(self):
        print("Dobro pozhalovat v Krestiki-noliki!")
        print("Vvedite koordinaty v formate 'stroka stolbec' (naprimer: '1 2')")
        
        while True:
            self.print_board()
            
            if self.current_player == 'X':
                try:
                    move = input(f"Igrok {self.current_player}, vvedite vash khod (stroka stolbec): ").split()
                    if len(move) != 2:
                        print("Nekorrektnyy vvod. Pozhaluysta, vvedite dve koordinaty.")
                        continue
                        
                    row, col = map(int, move)
                    
                    if row < 0 or row > 2 or col < 0 or col > 2:
                        print("Koordinaty dolzhny byt ot 0 do 2.")
                        continue
                        
                    if not self.make_move(row, col):
                        print("Eta kletka uzhe zanyata. Poprobuite druguyu.")
                        continue
                        
                except ValueError:
                    print("Nekorrektnyy vvod. Pozhaluysta, vvedite chisla.")
                    continue
                except (EOFError, KeyboardInterrupt):
                    print("\nIgra prervana.")
                    return
            else:
                print("Khod kompyutera...")
                move = self.ai_move()
                if move:
                    self.make_move(move[0], move[1])
            
            winner = self.check_winner()
            if winner:
                self.print_board()
                if winner == 'X':
                    print("Pozdravlyaem! Vy pobedili!")
                else:
                    print("Kompyuter pobedil!")
                break
                
            if self.is_board_full():
                self.print_board()
                print("Nichya!")
                break
                
            self.switch_player()

def main():
    game = TicTacToe()
    game.play()
    
    while True:
        try:
            play_again = input("Khotite sygrat eshche raz? (da/net): ").lower()
            if play_again in ['da', 'yes', 'y', 'дa']:
                game = TicTacToe()
                game.play()
            elif play_again in ['net', 'no', 'n', 'нет']:
                print("Spasibo za igru!")
                break
            else:
                print("Pozhaluysta, vvedite 'da' ili 'net'.")
        except (EOFError, KeyboardInterrupt):
            print("\nSpasibo za igru!")
            break

if __name__ == "__main__":
    main()