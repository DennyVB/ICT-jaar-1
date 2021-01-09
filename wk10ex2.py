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

        return s       # het bord is compleet, geef het terug
    
    
    def add_move(self, col, ox):

        for row in range(0, self.height):
            if self.data[row][col] != " ":
                self.data[row - 1][col] = ox
                return
        
        self.data[self.height - 1][col] = ox
    
    def del_move(self, col):
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

        if col < 0 or col >= self.width :
            return False
        elif self.data[0][col] != " ":
            return False
        
        else:
            return True
        
    def wins_for(self, ox):
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
