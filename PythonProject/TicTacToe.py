import tkinter as tk

from tkinter import messagebox


class TicTacToe:

    def __init__(self, master):

        self.master = master

        self.master.title("Tic Tac Toe")

        self.board = [' ' for _ in range(9)]  # 3x3 board

        self.current_player = 'X'  # Player starts as 'X'

        self.buttons = [None] * 9

        self.create_buttons()

    def create_buttons(self):

        for i in range(9):
            self.buttons[i] = tk.Button(self.master, text=' ', font='Arial 20', width=5, height=2,

                                        command=lambda i=i: self.player_move(i))

            self.buttons[i].grid(row=i // 3, column=i % 3)

    def player_move(self, index):

        if self.board[index] == ' ':

            self.board[index] = self.current_player

            self.buttons[index].config(text=self.current_player)

            if self.check_winner(self.current_player):

                messagebox.showinfo("Juego terminado", f"¡El jugador {self.current_player} gana!")

                self.reset_game()

            elif ' ' not in self.board:

                messagebox.showinfo("Juego terminado", "¡Es un empate!")

                self.reset_game()

            else:

                self.current_player = 'O'  # Cambia al jugador O

                self.computer_move()

    def computer_move(self):

        index = self.find_best_move()

        if index is not None:

            self.board[index] = 'O'

            self.buttons[index].config(text='O')

            if self.check_winner('O'):

                messagebox.showinfo("Juego terminado", "¡La computadora gana!")

                self.reset_game()

            elif ' ' not in self.board:

                messagebox.showinfo("Juego terminado", "¡Es un empate!")

                self.reset_game()

            else:

                self.current_player = 'X'  # Cambia al jugador X

    def find_best_move(self):

        # Algoritmo simple para encontrar el mejor movimiento

        for i in range(9):

            if self.board[i] == ' ':

                self.board[i] = 'O'

                if self.check_winner('O'):
                    return i

                self.board[i] = ' '  # Deshacer movimiento

        for i in range(9):

            if self.board[i] == ' ':

                self.board[i] = 'X'

                if self.check_winner('X'):
                    self.board[i] = ' '  # Deshacer movimiento

                    return i

                self.board[i] = ' '  # Deshacer movimiento

        # Movimiento en el centro si está disponible

        if self.board[4] == ' ':
            return 4

        # Movimiento en las esquinas

        for i in [0, 2, 6, 8]:

            if self.board[i] == ' ':
                return i

        # Movimiento en los lados

        for i in [1, 3, 5, 7]:

            if self.board[i] == ' ':
                return i

        return None

    def check_winner(self, player):

        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),

                                (0, 3, 6), (1, 4, 7), (2, 5, 8),

                                (0, 4, 8), (2, 4, 6)]

        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)

    def reset_game(self):

        self.board = [' ' for _ in range(9)]

        self.current_player = 'X'

        for button in self.buttons:
            button.config(text=' ')


if __name__ == "__main__":
    root = tk.Tk()

    game = TicTacToe(root)

    root.mainloop()