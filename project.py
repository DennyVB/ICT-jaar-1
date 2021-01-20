def in_a_row_n_east(ch, r_start, c_start, a, n):
    """ Checks if a character 'ch' appears n times in a row in east direction.
        With starting point 'r_start' and 'c_start'
    """

    
    rows = len(a)      
    cols = len(a[0])   
    
    if r_start >= rows:
        return False  


    if c_start > cols - n:
        return False
    
    for i in range(n):
        if a[r_start][c_start+i] != ch:
            return False
    
    return True



def in_a_row_n_south(ch, r_start, c_start, a, n):
    """ Checks if a character 'ch' appears n times in a row in south direction.
        With starting point 'r_start' and 'c_start'
    """

    
    rows = len(a)
    cols = len(a[0])
    


    if r_start > rows - n:
        return False
    
    if c_start >= cols:
        return False
    
    for i in range(n):
        if a[r_start+i][c_start] != ch:
            return False
    
    return True



def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """ Checks if a character 'ch' appears n times in a row in southeast direction.
        With starting point 'r_start' and 'c_start'
    """
    
    rows = len(a)
    cols = len(a[0])
   

    if r_start > rows - n:
        return False
    
    if c_start > cols - n:
        return False
    
    for i in range(n):
        if a[r_start+i][c_start+i] != ch:
            return False
    
    return True

def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """ Checks if a character 'ch' appears n times in a row in northeast direction.
        With starting point 'r_start' and 'c_start'
    """
    
    rows = len(a)
    cols = len(a[0])

    if r_start < n-1:
        return False
    
    if c_start > cols - n:
        return False

    for i in range(n):
        
        if a[r_start-i][c_start+i] != ch:
            return False
        
    return True




class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # de string om terug te geven
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # onderkant van het bord
        
        

        # hier moeten de nummers nog onder gezet worden
        s += '\n'
        for i in range(self.width):
            s += ' ' + str(i%10)
        return s       # het bord is compleet, geef het terug
    
    
    def add_move(self, col, ox):
        """Adds a move to the board at a given column and specified character ox O/X
        """

        for row in range(0, self.height):
            if self.data[row][col] != " ":
                self.data[row - 1][col] = ox
                return
        
        self.data[self.height - 1][col] = ox
    
    def del_move(self, col):
        """Deletes the last move in a specific column
        """
        for row in range(0, self.height):
            if self.data[row][col] != " ":
                self.data[row][col] = " "
                return

        
    def set_board(self, move_string):
        """ Accepts a string of columns and places
            alternating checkers in those columns,
            starting with 'X'.
            For example, call b.set_board('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.set_board('000000') to
            see them alternate in the left column.
            move_string must be a string of one-digit integers.
        """
        next_checker = 'X'   # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allows_move(self, col):
        """Checks if a move is allowed in the specific column
        """

        if col < 0 or col >= self.width :
            return False
        elif self.data[0][col] != " ":
            return False
        
        else:
            return True
    
    def is_full(self):
        """Checks if the board is full
        """
        for col in range(0, self.width):
            if self.allows_move(col) == True:
                return False
        
        return True
        
    def wins_for(self, ox):
        """Checks if the board is winning for the specific ox: O/X
        """
        # Controleren op horizontale overwinningen
        for row in range(0, self.height):
            for col in range(0, self.width):
                if in_a_row_n_east(ox, row, col, self.data, 4) == True:
                    return True
                elif in_a_row_n_south(ox, row, col, self.data, 4) == True:
                    return True
                elif in_a_row_n_northeast(ox, row, col, self.data, 4) == True:
                    return True
                elif in_a_row_n_southeast(ox, row, col, self.data, 4) == True:
                    return True
        
        return False

    def host_game(self):
        """Hosts a complete game of 'four in a row'
        """
        while True:
            print(self.__repr__())
            users_col = -1
            while not self.allows_move(users_col):
                users_col = int(input("Kies een kolom: "))
            
            self.add_move(users_col, 'X')
            if self.wins_for('X') == True:
                print(self.__repr__())
                print('X wint -- Gefeliciteerd!')
                break
            elif self.is_full() == True:
                print('Gelijkspel!!!')
                break

             

                


            
            print(self.__repr__())
            users_col = -1
            while not self.allows_move(users_col):
                users_col = int(input("Kies een kolom: "))
            
            self.add_move(users_col, 'O')
            if self.wins_for('O') == True:
                print(self.__repr__())
                print('O wint -- Gefeliciteerd!')
                break

            elif self.is_full() == True:
                print('Gelijkspel!!!')
                break

    def play_game(self, px, po, show_scores=False):
        """
        Plays a game of Connect Four between players px and po.
        If show_scores is True, the player's board evaluations are printed each turn.
        """
        ox = 'O'
        while True:
            # druk het bord af
            print(self)

            # controleer of het spel afgelopen is
            if self.wins_for(ox):
                print(f'{ox} heeft gewonnen!')
                break
            elif self.is_full():
                print('Gelijkspel!')
                break

            # verander de huidige speler
            if ox == 'O':
                ox = 'X'
                player = px
            else:
                ox = 'O'
                player = po

            if player == 'human':
                # laat de menselijke speler een kolom kiezen
                col = -1
                while not self.allows_move(col):
                    col = int(input('Kolom voor ' + ox + ': '))
            else:
                # de computerspeler berekent een zet
                if show_scores:
                    scores = player.scores_for(self)
                    print('Scores voor ', ox, ':', [int(sc) for sc in scores])
                    col = player.tiebreak_move(scores)
                else:
                    col = player.next_move(self)

            # voer de zet uit
            self.add_move(col, ox)   
                    
                

class Player:
    

    def __init__(self, ox, tbt, ply):
        """Constructs objects of type Player with the given ox(O/X), strategy and 
            the amount of moves looking ahead 'ply'
        """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Returns the string representation of the Player
        """

        s = "Player: ox = " + self.ox + ", "
        s += "tbt = " + self.tbt + ", "
        s += "ply = " + str(self.ply)
        return s

    def opp_ch(self):
        """Character opposite of self
        """
        if self.ox == 'X':
            return 'O'
        elif self.ox == 'O':
            return 'X'
    

    def score_board(self, b):
        """Gives the board a score if its winning or losing or equal
        """
        if b.wins_for(self.ox) == True:
            return 100.0
        elif b.wins_for(self.opp_ch()) == True:
            return 0.0
        else:
            return 50.0
        

    def tiebreak_move(self, scores):
        """Makes a move based on the chosen strategy and chooses between moves with    
            the highest score
        """
        
        import random
        
        maximum = max(scores)
        max_indices = []
        for i, x in enumerate(scores):
            if x == max(scores):
                max_indices += [i]
        
        if self.tbt == 'LEFT':
            return max_indices[0]
        elif self.tbt == 'RIGHT':
            return max_indices[-1]
        
        elif self.tbt == 'RANDOM':
            
        
            return max_indices[random.choice(range(len(max_indices)))]


    def scores_for(self, b):
        """Scores the board and gives every column a score to check for winning moves or best moves
        """
        
        scores = [50.0] * b.width
        
        op = Player(self.opp_ch(), self.tbt, (self.ply - 1) )
        for x in range(len(scores)):
            
            
            if b.allows_move(x) == False:
                scores[x] = -1.0
                
            elif b.wins_for(self.ox) == True:
                scores[x] = 100.0
                
            elif b.wins_for(self.opp_ch()) == True:
                scores[x] = 0.0
                
            elif self.ply == 0:
                scores[x] = 50.0
                
            else: 
                
                b.add_move(x, self.ox)
                
                
                if b.wins_for(self.ox) == True:
                    scores[x] = 100.0
                    b.del_move(x)
                elif b.wins_for(self.opp_ch()) == True:
                    scores[x] = 0.0
                    b.del_move(x)
                elif b.allows_move(x) == False:
                    scores[x] = -1.0
                    b.del_move(x)
                else:
                    scores[x] = 100 - max(op.scores_for(b))
                    b.del_move(x)
                    
        
        return scores

    def next_move(self, b):
        scores = self.scores_for(b)
        best_move = self.tiebreak_move(scores)

        return best_move    

    

