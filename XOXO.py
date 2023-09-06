from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class TicTacToe(BoxLayout):
    def __init__(self, **kwargs):
        super(TicTacToe, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.grid = GridLayout(cols=3)
        self.board = ['' for _ in range(9)]
        self.current_player = "X"
        self.buttons = [Button(text="", on_press=self.make_move) for _ in range(9)]
        for button in self.buttons:
            self.grid.add_widget(button)
        self.add_widget(self.grid)
        self.status_label = Label(text="Player X's turn")
        self.add_widget(self.status_label)
        self.reset_button = Button(text="Reset", on_press=self.reset_game)
        self.add_widget(self.reset_button)

    def make_move(self, button):
        position = self.buttons.index(button)
        if self.board[position] == '':
            self.board[position] = self.current_player
            self.buttons[position].text = self.current_player
            if self.check_winner(self.current_player):
                self.status_label.text = f"Player {self.current_player} wins!"
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.text = f"Player {self.current_player}'s turn"
        else:
            self.status_label.text = "Invalid move!"

    def check_winner(self, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(all(self.board[i] == player for i in combination) for combination in winning_combinations)

    def reset_game(self, instance=None):
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button.text = ""
        self.current_player = "X"
        self.status_label.text = "Game reset. Player X's turn"

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()

if __name__ == "__main__":
    TicTacToeApp().run()
