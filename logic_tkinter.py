 #Sue Ji 33337876

##import point



class DiscState:
    '''
    Gamestate info:
    whether it is flippable and valid to be dropped,
    how many discs of each color on the board, when and who wins
    '''

    def __init__(self, turn:str,wonMode:str,board_row:int,board_col:int):
        self.turn=turn
        self._wonMode=wonMode
        self._row=board_row
        self._col=board_col
        self._none = 'No One'
        self._black = 'B'
        self._white = 'W'
        self._board=self.empty_board()
        self._black_discs=[]
        self._white_discs=[]
        


    def from_pixel(self,points:[list],w:int,h:int)->list:
        '''
        transver the clicked point coordinator from pixel to the tile row and col
        '''
        tile=[]

        for point in points:
            for tile_x in range(self._col):
    

                range1=tile_x/self._col
                range2=(tile_x+1)/self._col
                
                if point[0]/w > range1 and point[0]<range2:
                   

                    for tile_y in range(self._row):
                        range3=tile_y/self._row
                        range4=(tile_y+1)/self._row
                        
                        if point[1]/h > range3 and point[1]/h<range4:

                            tile.append([tile_x,tile_y])

   
            return tile
                


    def handle_click(self,point:list,color:str)->None:
        '''
        Whenever click on canvas, the click point coordinator will be appended
        to the self.discs list
        '''
        if color=='B':
            self._black_discs.append(point)
        else:
            self._white_discs.append(point)
        


    def handle_game(self,point:[list],w:int,h:int)->str:
        '''
        check whether either player has won and the valid move before drop the disc, switch
        the turn and update the board
        '''
        
        tile=self.from_pixel(point,w,h)
        if self.full_board():
            return self.winner()
        else:
            if self.empty_board_check():
                if self.check_all(tile[0],[tile[1]]):
                    self.flip_all(tile[0],tile[1])
                                
            else:
                return self.winner()
        
            
        
    def black_discs(self)->[list]:
        '''
        return all the black discs' pixel coordinators on the board, to be used in GUI later
        '''
        return self._black_discs
    

    def white_discs(self)->[list]:
        '''
        return all the white discs' pixel coordinators on the board, to be used in GUI later
        '''
        return self._white_discs



    def empty_board(self)->[[str]]:
        '''
        gievn the board row and col, create the two-dimensional board
        '''
        
        board=[]
        for r in range(self._row):
            board.append([])
            
            for c in range(self._col):
                
                board[-1].append(self._none)
               
        self._board=board
       
        return self._board

    

    def update_board(self)->None:
        '''
        given the exisiting discs on the board, update the 2-dimensional board 
        '''
       
        for disc in self._discs:
            if self.turn==self._black:

                self._board[disc[0]][disc[1]]=self._black
            else:
                self._board[disc[0]][disc[1]]=self._white                
                
                

    def total_black(self)->int:
        '''
        the number of black discs on the board currently
        '''
   
        black=0
       
        for row in range(len(self._board)):
            for tile in range(len(self._board[row])):
                if self._board[row][tile]==self._black:
                    black+=1
        return black

    
    def total_white(self)->int:
        '''
        the number of white discs on the board currently
        '''
        white=0
        for row in range(len(self._board)):
            for tile in range(len(self._board[row])):
                if self._board[row][tile]==self._white:
                    white+=1
        return white



    def opposite_turn(self)->str:
        '''
        return the turn that is opposite to the current turn
        '''
        if self.turn == self._black:
           
            return self._white

        else:
            return self._black

    

    def winner(self) -> str:
        '''
        Determines the winning player in the given game state, if any.
        If the black player has won, BLACK is returned; if the white player
        has won, WHITE is returned; if no player has won yet, NONE is
        returned.
        '''
        winner = self._none

        if self._wonMode=='>':
            if self.total_black()>self.total_white():
                winner=self._black
            elif self.total_white()>self.total_black(): 
                winner=self._white
            else:
                winner=self._none
        elif self._wonMode=='<':
            if self.total_black()>self.total_white():
                winner=self._black
            elif self.total_white()>self.total_black():
                winner=self._white
            else:
                winner=self._none
        
        return winner


    def full_board(self) -> bool:
        '''
        check if the board is full of discs
        '''
        full=True
        for rw in range(len(self._board)):
            for col in range(len(self._board[rw])):
                if self._board[rw][col]==self._none:
                    full=False
        return full

    
    def empty_board_check(self)->bool:
        '''
        check if there is no more valid move for current turn player
        when the board is not full yet
        '''
        valid_move=True

        bool_list=[]
        
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):

                if self._board[row][col]==self._none:
                
                    bool_list.append(self.check_all(row,col))

        if True in bool_list:
            valid_move=True
        else:
            valid_move=False
            
        return valid_move


    def flip_all(self,tiles:[list])->None:
        '''
        taken the tiles coordinators that have discs on the
        canvas, update the gameboard
        '''
        for tile in tiles:
            self._board[tile[0]][tile[1]]=self.turn


    def check_all(self,start_row:int,start_col:int)->bool:
        if self._board[start_row][start_col]==self._none:
        
            if self._down_right(start_row,start_col)!=[]or self._up_right(start_row,start_col)!=[]or \
               self._down_left(start_row,start_col)!=[]or self._up_left(start_row,start_col)!=[]or \
               self._down(start_row,start_col)!=[]or self._up(start_row,start_col)!=[]or\
               self._right(start_row,start_col)!=[]or self._left(start_row,start_col)!=[]:
                return True
            else:
                return False
        else:
            self.winner()
            return False



    '''try delta +/- 1 to make the 8 directions flip together in one function'''
   
        

    def _flip_all(self,start_row:int,start_col:int):  
        
        if self._down_right(start_row,start_col)!=[]:

            for tile in self._down_right(start_row,start_col):
                self._board[tile[0]][tile[1]]=self.turn
                
        if self._up_right(start_row,start_col)!=[]:
 
            for tile in self._up_right(start_row,start_col):
                self._board[tile[0]][tile[1]]=self.turn
        if self._down_left(start_row,start_col)!=[]:
         
            for tile in self._down_left(start_row,start_col):
                self._board[tile[0]][tile[1]]=self.turn
        if self._up_left(start_row,start_col)!=[]:
           
            for tile in self._up_left(start_row,start_col):
                self._board[tile[0]][tile[1]]=self.turn
        if self._down(start_row,start_col)!=[]:
            self._board[start_row][start_col]=self.turn
            for tile in self._down(start_row,start_col):
                self._board[tile[0]][tile[1]]=self.turn

        if self._right(start_row,start_col)!=[]:
            self._board[start_row][start_col]=self.turn
            for tile in self._right(start_row,start_col):
                self._board[tile[0]][tile[1]]=self.turn
        if self._up(start_row,start_col)!=[]:
            self._board[start_row][start_col]=self.turn
            for tile in self._up(start_row,start_col):
                self._board[tile[0]][tile[1]]=self.turn
        if self._left(start_row,start_col)!=[]:
            self._board[start_row][start_col]=self.turn
            for tile in self._left(start_row,start_col):
                self._board[tile[0]][tile[1]]=self.turn

   

    def _down_right(self,start_row:int,start_col:int)->list:
        '''
        find the flippable tiles in down-right direction from the input tile.
        no flippable tiles in this direction if the tile is such as in range
        (len(self.board),len(self.board)) or no self-color disc on the direction
        '''

        flippable=[]
        dist=1
        new_row=start_row+1*dist
        new_col=start_col+1*dist
    
        while new_row<len(self._board) and new_col<len(self._board[start_row]):
            try:
                if self._board[new_row][new_col]!=self.turn and\
                   self._board[new_row][new_col]!=self._none:
                    dist+=1
                    new_row=start_row+1*dist
                    new_col=start_col+1*dist
                    if new_row<len(self._board) and new_col<len(self._board[start_row]):
                        if self._board[new_row][new_col]==self.turn:
                            for x in range(dist+1):
                                within_row=new_row-1*x
                                within_col=new_col-1*x
                                if self._board[within_row][within_col]==self._none:
                
                                    if within_row==start_row and within_col==start_col:
                                        flippable.append((within_row,within_col))
                                        
                                    else:
                                        flippable=[]
                                if self._board[within_row][within_col]==self.opposite_turn():
                                    flippable.append((within_row,within_col))
            
                else:
                   
                    break
                                    
            except IndexError:

                flippable=[]
                break

        return flippable


    def _up_right(self,start_row:int,start_col:int)->list:
        '''
        find the flippable tiles in down-right direction from the input tile.
        no flippable tiles in this direction if the tile is such as in range
        (len(self.board),len(self.board)) or no self-color disc on the direction
        '''

        flippable=[]
        dist=1
        new_row=start_row-1*dist
        new_col=start_col+1*dist
        
        while 0<=new_row and new_col<len(self._board[start_row]):
            try:

                if self._board[new_row][new_col]!=self.turn and\
                   self._board[new_row][new_col]==self._none:
                    dist+=1
                    new_row=start_row-1*dist
                    new_col=start_col+1*dist
                    if 0<=new_row and new_col<len(self._board[start_row]):
                        if self._board[new_row][new_col]==self.turn:
                            for x in range(dist+1):
                                within_row=new_row+1*x
                                within_col=new_col-1*x
                                if self._board[within_row][within_col]==self._none:
                
                                    if within_row==start_row and within_col==start_col:
                                        flippable.append((within_row,within_col))
                                        
                                    else:
                                        flippable=[]
                                if self._board[within_row][within_col]==self.opposite_turn():
                                    flippable.append((within_row,within_col))

                else:
                    
                    break
                                    
            except IndexError:

                flippable=[]
                break

        return flippable


        

    def _down_left(self,start_row:int,start_col:int)->list:
        '''
        find the flippable tiles in down-right direction from the input tile.
        no flippable tiles in this direction if the tile is such as in range
        (len(self.board),len(self.board)) or no self-color disc on the direction
        '''

        flippable=[]
        dist=1
        new_row=start_row+1
        new_col=start_col-1
    
        while new_row<len(self._board) and 0<=new_col:
            try:
                if self._board[new_row][new_col]!=self.turn and\
                   self._board[new_row][new_col]!=self._none:
                    dist+=1
                    new_row=start_row+1*dist
                    new_col=start_col-1*dist
                    if new_row<len(self._board) and 0<=new_col:
                        if self._board[new_row][new_col]==self.turn:
                            for x in range(dist+1):
                                within_row=new_row-1*x
                                within_col=new_col+1*x
                                if self._board[within_row][within_col]==self._none:
                
                                    if within_row==start_row and within_col==start_col:
                                        flippable.append((within_row,within_col))
                                        
                                    else:
                                        flippable=[]
                                if self._board[within_row][within_col]==self.opposite_turn():
                                    flippable.append((within_row,within_col))

                                    
                else:
                    
                    break
                                    
            except IndexError:
                flippable=[]
                break
        return flippable
        

    def _up_left(self,start_row:int,start_col:int)->list:
        '''
        find the flippable tiles in down-right direction from the input tile.
        no flippable tiles in this direction if the tile is such as in range
        (len(self.board),len(self.board)) or no self-color disc on the direction
        '''

        flippable=[]
        dist=1
        new_row=start_row-1*dist
        new_col=start_col-1*dist
       
        while 0<=new_row and 0<=new_col:
            try:
                if self._board[new_row][new_col]!=self.turn and\
                   self._board[new_row][new_col]!=self._none:
                    dist+=1
                    new_row=start_row-1*dist
                    new_col=start_col-1*dist
                    if 0<=new_row and 0<=new_col:
                        if self._board[new_row][new_col]==self.turn:
                            for x in range(dist+1):
                                within_row=new_row+1*x
                                within_col=new_col+1*x
                                if self._board[within_row][within_col]==self._none:
                
                                    if within_row==start_row and within_col==start_col:
                                        flippable.append((within_row,within_col))
                                        
                                    else:
                                        flippable=[]
                                if self._board[within_row][within_col]==self.opposite_turn():
                                    flippable.append((within_row,within_col))

                                    
                else:
                    break
                                    
            except IndexError:
                flippable=[]
                break

        return flippable
 

        

    def _right(self,start_row:int,start_col:int)->list:
        '''
        find the flippable tiles in down-right direction from the input tile.
        no flippable tiles in this direction if the tile is such as in range
        (len(self.board),len(self.board)) or no self-color disc on the direction
        '''

        try:
            flippable=[]
            for col in range(start_col+1,len(self._board[start_row])):
                if self._board[start_row][col]==self.turn:
                    if col!=start_col+1:
                        for cl in range(start_col+1,col):
                            if self._board[start_row][cl]==self._none:
                                flippable=[]
                            if self._board[start_row][cl]==self.opposite_turn():
                                flippable.append((start_row,cl))
                    else:
                        flippable=[]
            return flippable
        except IndexError:
            flippable=[]
            pass
                                
    def _left(self,start_row:int,start_col:int)->list:
        '''
        find the flippable tiles in down-right direction from the input tile.
        no flippable tiles in this direction if the tile is such as in range
        (len(self.board),len(self.board)) or no self-color disc on the direction
        '''
        
        try:
            flippable=[]
            for col in range(0,start_col):
                if self._board[start_row][col]==self.turn:
                    if col!=start_col-1:
                        for cl in range(col,start_col):
                            if self._board[start_row][cl]==self._none:
                                flippable=[]
                            if self._board[start_row][cl]==self.opposite_turn():
                                flippable.append((start_row,cl))
                    else:
                        flippable=[]
            return flippable
        except IndexError:
            flippable=[]
            pass
                    
    def _up(self,start_row:int,start_col:int)->list:
        '''
        find the flippable tiles in down-right direction from the input tile.
        no flippable tiles in this direction if the tile is such as in range
        (len(self.board),len(self.board)) or no self-color disc on the direction
        '''

        try:
            flippable=[]
            for row in range(0,start_row):
                if self._board[row][start_col]==self.turn:
                    if row!=start_row-1:
                        for rw in range(row,start_row):
                            if self._board[rw][start_col]==self._none:
                                flippable=[]
                            if self._board[rw][start_col]==self.opposite_turn():
                                flippable.append((rw,start_col))
                    else:
                        flippable=[]
            return flippable
        except IndexError:
            flippable=[]
            pass
                
    def _down(self,start_row:int,start_col:int)->list:
        '''
        find the flippable tiles in down-right direction from the input tile.
        no flippable tiles in this direction if the tile is such as in range
        (len(self.board),len(self.board)) or no self-color disc on the direction
        '''

        try:
            flippable=[]
            for row in range(start_row+1,len(self._board)):
                if self._board[row][start_col]==self.turn:
                    if row!=start_row+1:
                        for rw in range(start_row,row):
                            if self._board[rw][start_col]==self._none:
                                flippable=[]
                            if self._board[rw][start_col]==self.opposite_turn():
                                flippable.append((rw,start_col))
                    else:
                        flippable=[]
            return flippable
        except IndexError:
            flippable=[]
            pass
            
        

