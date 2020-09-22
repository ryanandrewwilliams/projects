import random

class game:
    def __init__(self):
        self.board = [None]*9
        self.current_player = 'x'

    def print_board(self):
        length = len(self.board) / 3
        length = int(length)
        for i in range(length):
            print(self.board[3*i:length+(i*3)])


    def pick_space(self, row_index, col_index, player):
        t = (row_index * 3) + col_index
        if self.is_valid_move(row_index, col_index) == True:
            self.board[t] = player
            return True
        else:
            print('Not a Valid Move')
            return False


    def is_valid_move(self, row_index, col_index):
        t = (row_index * 3) + col_index
        if t <= 8 and self.board[t] == None:
            return True
        else:
            return False


    def get_move(self, player):
        print('Select Row')
        row_index = int(input())
        print('Select Column')
        col_index = int(input())
        if self.pick_space(row_index, col_index, player) == False:
            return self.get_move(player)
        else:
            result = self.winner(row_index,col_index,'x')
            game_over = self.is_game_over(row_index, col_index, 'x')
            if result == 'x':
                print('PLAYER VICTORY')
        return game_over


    def get_ai_move(self):
        possible_moves = self.open_spots()
        index = random.randint(0, len(possible_moves)-1)
        selected_move = possible_moves[index]
        row_index = selected_move[0]
        col_index = selected_move[1]
        self.pick_space(row_index, col_index, 'o')
        result = self.winner(row_index, col_index, 'o')
        game_over = self.is_game_over(row_index, col_index, 'o')
        if result == 'o':
            print('AI VICTORY')
        return game_over

    def is_game_over(self,row_index, col_index, player):
        possible_moves = self.open_spots()
        result = self.winner(row_index, col_index, player)
        if len(possible_moves) < 1 and result != player:
            print('GAME OVER! CATS GAME')
            return 1
        elif result == player:
            print('GAME OVER')
            return 1
        else:
            return 0


    def open_spots(self):
        available = []
        for i in range(9):
            if self.board[i] == None:
                row_index = int(i / 3)
                col_index = i % 3
                available.append([row_index,col_index])
        return available


    def winner(self, row_index,col_index,player):
        win = True
        for i in range(3):
            t = (row_index * 3) + i
            win = (win and self.board[t] == player)
        if win:
            return player
        win = True
        for i in range(3):
            t = (i * 3) + col_index
            win = (win and self.board[t] == player)
        if win:
            return player
        win = True
        for i in range(3):
            t = (i * 3) + i
            win = (win and self.board[t] == player)
        if win:
            return player
        win = True
        for i in range(3):
            t = 6 - (2 * i)
            win = (win and self.board[t] == player)
        if win:
            return player

    def play_game(self, player):
        self.print_board()
        game_over = 0
        while game_over == 0:
            game_over = self.get_move(player)
            if game_over == 0:
                game_over = self.get_ai_move()
            self.print_board()








g = game()
g.print_board()
#g.play_game('x')
"""
g.get_move('x')
g.open_spots()
g.get_ai_move()
g.get_move('x')
g.open_spots()
g.get_ai_move()
g.get_move('x')
g.open_spots()
g.get_ai_move()
"""


