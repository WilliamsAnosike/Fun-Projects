#This is a game of Tic-Tac-Toe!

def new_game():
    user_input = input("Do you wish to start a new game?(Y/N)(exit to terminate): ")
    if user_input == "Y":   
        print("New game coming up!")
        new_board = TicTacToe()
        new_board.print_board()
        playing(new_board)
    else:
        print("Ending session...")

class TicTacToe():
    def __init__(self, ):
        super().__init__()
        self.status = 0
        self.board = {1: " ", 2: " ", 3: " ",
                      4: " ", 5: " ", 6: " ",
                      7: " ", 8: " ", 9: " "
                     }
    
    def print_board(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        
    def move(self, player, position):
            self.board[position] = player
    
    def check(self, count):
        if count >= 5:
            if (self.board[1] == self.board[2] == self.board[3]) and (self.board[1] != " "):
                self.print_board()
                print("GAME OVER!")
                print("Player", str(self.board[1]), "is the winner!")
                self.status = 1
            elif (self.board[4] == self.board[5] == self.board[6]) and (self.board[4] != " "):
                self.print_board()
                print("GAME OVER!")
                print("Player", str(self.board[4]), "is the winner!")
                self.status = 1
            elif (self.board[7] == self.board[8] == self.board[9]) and (self.board[7] != " "):
                self.print_board()
                print("GAME OVER!")
                print("Player", str(self.board[7]), "is the winner!")
                self.status = 1
            elif (self.board[1] == self.board[5] == self.board[9]) and (self.board[1] != " "):
                self.print_board()
                print("GAME OVER!")
                print("Player", str(self.board[1]), "is the winner!")
                self.status = 1
            elif (self.board[1] == self.board[4] == self.board[7]) and (self.board[1] != " "):
                self.print_board()
                print("GAME OVER!")
                print("Player", str(self.board[1]), "is the winner!")
                self.status = 1
            elif (self.board[2] == self.board[5] == self.board[8]) and (self.board[2] != " "):
                self.print_board()
                print("GAME OVER!")
                print("Player", str(self.board[2]), "is the winner!")  
                self.status = 1 
            elif (self.board[3] == self.board[6] == self.board[9]) and (self.board[3] != " "):
                self.print_board()
                print("GAME OVER!")
                print("Player", str(self.board[3]), "is the winner!")
                self.status = 1
            elif (self.board[3] == self.board[5] == self.board[7]) and (self.board[3] != " "):
                self.print_board()
                print("GAME OVER!")
                print("Player", str(self.board[3]), "is the winner!") 
                self.status = 1                                                                                        
        if count == 10:
            print("GAME OVER!")
            print("It's a tie")
        

def playing(board):
    count = 1
    player = 'X'
    
    while (count != 9) and (board.status == 0):
        next_move = int(input("Player {0} it is your turn! Where would you like to move?: ".format(player)))
        board.move(player, next_move)
        board.print_board()
        board.check(count)
        count += 1
        if count in [1,3,5,7,9]:
            player = 'X'
        else:
            player = 'O'
        
    
    print("GAME IS OVER!!")
        
new_game()