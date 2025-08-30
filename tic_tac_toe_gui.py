import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.resizable(False, False)
        
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()
        
    def create_widgets(self):
        # Создаем кнопки для игрового поля
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.root,
                    text=' ',
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button
                
        # Создаем кнопку для новой игры
        self.restart_button = tk.Button(
            self.root,
            text="Новая игра",
            font=('Arial', 12),
            command=self.restart_game
        )
        self.restart_button.grid(row=3, column=0, columnspan=3, pady=10)
        
    def on_button_click(self, row, col):
        # Проверяем, что клетка пуста и нет победителя
        if self.board[row][col] == ' ' and not self.check_winner() and not self.is_board_full():
            # Ход игрока
            self.make_move(row, col, 'X')
            
            # Проверяем победителя после хода игрока
            winner = self.check_winner()
            if winner:
                self.highlight_winner()
                messagebox.showinfo("Победа!", f"Игрок {winner} победил!")
                return
                
            # Проверяем ничью
            if self.is_board_full():
                messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
                return
                
            # Ход компьютера
            self.root.after(300, self.ai_move)  # Небольшая задержка для лучшего UX
            
    def make_move(self, row, col, player):
        self.board[row][col] = player
        self.buttons[row][col].config(text=player)
        
    def ai_move(self):
        # Простая стратегия ИИ:
        # 1. Попытаться выиграть
        # 2. Блокировать победу игрока
        # 3. Сделать случайный ход
        
        # Проверим, можем ли мы выиграть следующим ходом
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    if self.check_winner() == 'O':
                        self.board[i][j] = ' '  # Отменяем ход для проверки
                        self.make_move(i, j, 'O')
                        winner = self.check_winner()
                        if winner:
                            self.highlight_winner()
                            messagebox.showinfo("Победа!", f"Игрок {winner} победил!")
                            return
                        return
                    self.board[i][j] = ' '  # Отменяем ход
        
        # Проверим, нужно ли блокировать игрока
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'X'
                    if self.check_winner() == 'X':
                        self.board[i][j] = ' '  # Отменяем ход для проверки
                        self.make_move(i, j, 'O')
                        return
                    self.board[i][j] = ' '  # Отменяем ход
        
        # Если нет срочных ходов, выбираем случайную пустую клетку
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col, 'O')
            
            # Проверяем победителя после хода компьютера
            winner = self.check_winner()
            if winner:
                self.highlight_winner()
                messagebox.showinfo("Победа!", f"Игрок {winner} победил!")
                return
                
            # Проверяем ничью
            if self.is_board_full():
                messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
                
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
        
    def highlight_winner(self):
        # Подсветка выигрышной комбинации
        # Проверка строк
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                for j in range(3):
                    self.buttons[i][j].config(bg='lightgreen')
                return

        # Проверка столбцов
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != ' ':
                for i in range(3):
                    self.buttons[i][j].config(bg='lightgreen')
                return

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            for i in range(3):
                self.buttons[i][i].config(bg='lightgreen')
            return
            
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            for i in range(3):
                self.buttons[i][2-i].config(bg='lightgreen')
            return
            
    def restart_game(self):
        # Сброс игры
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', bg='SystemButtonFace')

def main():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()