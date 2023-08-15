from enum import Enum
from AI import best_move

class PlayerType(Enum):
    AI = 'AI'
    HUMAN = 'HUMAN'

def get_player_type(s):
    if s == 'HUMAN':
        return PlayerType.HUMAN
    elif s == 'AI':
        return PlayerType.AI
    else:
        print('Invalid, try again!')
        quit()

class Player:
    def __init__(self,player_type):
        self.ptype = get_player_type(player_type)

    def play(self, board):
        if self.ptype == PlayerType.HUMAN:
            return map(int,input('Enter row and column respectively: ').split())
        if self.ptype == PlayerType.AI:
            s1 = best_move[board]
            i = 0
            while i<9:
                if s1[i]!=board[i]:
                    break
                i+=1
            return (i//3,i%3)

class TicTacToe:
    def __init__(self,player1,player2):
        self.board = '+'*9
        self.player1 = player1
        self.player2 = player2
        self.turn = 1
        self.game_ended = 0
        self.display_board()

    def display_board(self):
        print('Current board : \n')
        print(' '.join(list(self.board[:3])))
        print(' '.join(list(self.board[3:6])))
        print(' '.join(list(self.board[6:])))
        print()

    def check_game_ended(self):
        x = self.board
        rows = [x[:3],x[3:6],x[6:]]
        cols = [x[::3],x[1::3],x[2::3]]
        diags = [x[::4],x[6::-2][:3]]
        check = rows+cols+diags
        if 'XXX' in check:
            self.game_ended = 1
        elif 'OOO' in check:
            self.game_ended = 2
        elif not x.count('+'):
            self.game_ended = 3
        return self.game_ended

    def play_turn(self):
        if self.turn==1:
            print('Player1 is playing now!')
            r,c = self.player1.play(self.board)
            i = 3*r+c
            self.board = self.board[:i]+'X'+self.board[i+1:]
            self.display_board()
            if self.check_game_ended():
                print('Match tied!' if self.game_ended == 3 else 'Player1 won!')
            else:
                self.turn=2
        if self.turn==2:
            print('Player2 is playing now!')
            r,c = self.player2.play(self.board)
            i = 3*r+c
            self.board = self.board[:i]+'O'+self.board[i+1:]
            self.display_board()
            if self.check_game_ended():
                print('Match tied!' if self.game_ended == 3 else 'Player2 won!')
            else:
                self.turn=1
    
    def play_game(self):
        while not self.game_ended:
            self.play_turn()


print('Welcome to Tictactoe!')
p1 = Player(input('Select player1 (HUMAN or AI) : ').upper())
p2 = Player(input('Select player2 (HUMAN or AI) : ').upper())
game = TicTacToe(p1,p2)
game.play_game()


