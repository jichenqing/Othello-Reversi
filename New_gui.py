#Sue Ji 33337876


import tkinter

import logic_tkinter

##import point



DEFAULT_FONT = ('Helvetica 14 bold')



class StartDialog:

    def __init__(self, root):

        self._root_window = root

        self._dialog_window = tkinter.Toplevel()

        

        title_label=tkinter.Label(

            master = self._dialog_window, text = 'Gameboard Setup',

            font = DEFAULT_FONT)


        
        title_label.grid(row = 0, column = 0,columnspan = 1,
                         sticky = tkinter.W+tkinter.N)




        done_button = tkinter.Button(

            master = self._dialog_window, text = 'Done', font = DEFAULT_FONT,

            command = self._on_ok_clicked)



        done_button.grid(row =0, column = 0, padx = 10, pady = 10, \
                          sticky = tkinter.E + tkinter.S)





        row_label=tkinter.Label(

            master = self._dialog_window, text = 'Number of Rows (4-16 even):',

            font = DEFAULT_FONT)

        row_label.grid( row = 1, column = 0, padx = 10, pady = 10,

            sticky = tkinter.W)
        



        self._row_var=tkinter.StringVar()
        self._row_var.set('4')


        row_options=tkinter.OptionMenu(self._dialog_window,
                                             self._row_var,'4',
                                             '6','8','10','12','14','16')
        row_options.grid(row = 1, column = 1, padx = 10, pady = 1,

            sticky = tkinter.W + tkinter.E)

      
        
        col_label=tkinter.Label(

            master = self._dialog_window, text = 'Number of Columns (4-16 even):',

            font = DEFAULT_FONT)

        col_label.grid(

            row = 2, column = 0, padx = 10, pady = 10,

            sticky = tkinter.W)
        

        self._col_var=tkinter.StringVar()
        self._col_var.set('4')

        col_options=tkinter.OptionMenu(self._dialog_window,self._col_var,'4',
                                             '6','8','10','12','14','16')

        col_options.grid(row = 2, column = 1, padx = 10, pady = 1,

            sticky = tkinter.W + tkinter.E)

       
       

        start_turn_label=tkinter.Label(

            master = self._dialog_window, text = '(Black or White) play first:',

            font = DEFAULT_FONT)

        start_turn_label.grid( row = 3, column = 0, padx = 10, pady = 10,

            sticky = tkinter.W)

        self._turn_var=tkinter.StringVar()
        self._turn_var.set('B')

        start_turn_options=tkinter.OptionMenu( self._dialog_window,
                                    self._turn_var,'B','W')
        
        start_turn_options.grid(row = 3, column = 1, padx = 10, pady = 1,

            sticky = tkinter.W + tkinter.E)
        

        

        win_mode_label=tkinter.Label(

            master = self._dialog_window, text = 'discs ">" or "<" to win:',

            font = DEFAULT_FONT)

        win_mode_label.grid(row = 4, column = 0, padx = 10, pady = 10,

            sticky = tkinter.W)


        self._win_var=tkinter.StringVar()
        self._win_var.set('>')

        win_mode_options=tkinter.OptionMenu(
        self._dialog_window, self._win_var,'<','>')

        win_mode_options.grid(row = 4, column = 1, padx = 10, pady = 1,

            sticky = tkinter.W + tkinter.E)

        

        self._dialog_window.columnconfigure(1, weight = 1)

        


        self._ok_clicked = False
        self._board_row=0
        self._board_col=0
        self._start_turn=''
        self._win_mode=''
        



    def show(self)->None:
        '''
        makes the dialog show up
        '''

        self._dialog_window.grab_set()

        self._dialog_window.wait_window()



    def was_ok_clicked(self) -> bool:
        
        '''
        MAKE THE VALUE A METHOD FOR LATER USE
        '''

        return self._ok_clicked



    def get_row(self) -> str:
        '''
        MAKE THE VALUE A METHOD FOR LATER USE
        '''

        return self._board_row



    def get_col(self) -> str:
        '''
        MAKE THE VALUE A METHOD FOR LATER USE
        '''

        return self._board_col

    

    def start_turn(self)->str:
        '''
        MAKE THE VALUE A METHOD FOR LATER USE
        '''
        
        return self._start_turn

    

    def win_mode(self)->str:
        '''
        MAKE THE VALUE A METHOD FOR LATER USE
        '''


        return self._win_mode



    def _on_ok_clicked(self)->None:
        '''
        STORE THE VARIABLES: input board col, borad row number, first
        player and win < or > FOR GUI
        '''
        
        self._ok_clicked = True


        self._board_row=int(self._row_var.get())

        self._board_col=int(self._col_var.get())

        self._start_turn=self._turn_var.get()

        self._win_mode=self._win_var.get()


        self._dialog_window.destroy()

        

####################################################################################################################



class OthelloApplication:

    


    def __init__(self):


        self._board_setup=False

        self._black_done_was_clicked=False

        self._white_done_was_clicked=False

        self._gamestart=False

        
        self._row=0
        self._col=0
        self._turn='B'
        self._win_mode=''
        self._first_turn=' '


        self._state=logic_tkinter.DiscState(self._turn,self._win_mode,
                                            self._row,self._col)



        self._root_window=tkinter.Tk()

        self._root_window.title('Full Othello Game')





        self.label_frame=tkinter.Frame(master = self._root_window)



        self.label_frame.grid(

            row =0, column = 0, padx =  10, pady = 10,

            sticky = tkinter.W + tkinter.S+tkinter.N+tkinter.E)
        
        
        self._score_board = tkinter.StringVar()

        self._score_board.set('B: {}     W: {}'.format(0,0))

        score_label=tkinter.Label(
            master = self.label_frame, textvariable = self._score_board,
            font = DEFAULT_FONT)
        score_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)



        self._turn_text = tkinter.StringVar()

        self._turn_text.set('turn: {}'.format(self._turn))

        turn_label=tkinter.Label(
            master = self.label_frame, textvariable = self._turn_text,
            font = DEFAULT_FONT)
        turn_label.grid(
            row = 0, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E)



        self._center_text = tkinter.StringVar()

        self._center_text.set('Welcome to Othello Full Game!')

        turn_label=tkinter.Label(
            master = self.label_frame, textvariable = self._center_text,
            font = DEFAULT_FONT)
        turn_label.grid(
            row = 0, column = 1, padx = 100, pady = 10,sticky = tkinter.E)

        


        

        self._canvas=tkinter.Canvas(master=self._root_window,

                                     width=500,height=500,

                                     background='green')

        self._canvas.grid(

            row = 2, column = 0, padx = 30, pady = 30,

            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)





        


        button_frame = tkinter.Frame(master = self._root_window)



        button_frame.grid(

            row =3, column = 0, padx = 10, pady = 10,

            sticky = tkinter.W + tkinter.S)


        
        setup_button=tkinter.Button(master = button_frame, text = 'setup gameboard',
                                          font = DEFAULT_FONT,
                                    command = self._on_setup_click)

        setup_button.grid(row = 0, column = 0, padx =5, pady = 0,
                                sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)




        black_done_button=tkinter.Button(master = button_frame, text =
                                          'Done with initial Black',
                                          font = DEFAULT_FONT,
                                         command = self._white_initial)

        black_done_button.grid(row = 0, column = 1, padx =5, pady = 0,
                                sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

 

        
        white_done_button=tkinter.Button(master = button_frame, text =
                                          'Start Game(Done with initial White)',
                                          font = DEFAULT_FONT,
                                         command = self._start_game)

        white_done_button.grid(row = 0, column = 2, padx =5, pady = 0,
                                sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)



        close_button=tkinter.Button(master=button_frame,text='Close',font=DEFAULT_FONT,
                                    command =self._root_window.destroy)
        close_button.grid(row = 0, column = 3, padx =5, pady = 0,
                                sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)


        
        
        
        self._canvas.bind('<Configure>', self._on_canvas_resized)                
        self._canvas.bind('<Button-1>', self._on_button_down)
        





        self._root_window.rowconfigure(0, weight = 0)

        self._root_window.rowconfigure(1, weight = 1)

        self._root_window.rowconfigure(2, weight = 1)

        self._root_window.rowconfigure(3, weight = 0)
        
        self._root_window.columnconfigure(0, weight = 1)





    def _on_setup_click(self)->None:

        '''
        MAKES THE StartDialog WINDOW POP UP WHEN CLICK 'START GAME' 
        '''
        
        options=StartDialog(self._root_window)
        options.show()

        if options.was_ok_clicked():
            
            self._row=options.get_row()

            self._col=options.get_col()

            self._first_turn=options.start_turn()
            
            self._win_mode=options.win_mode()

            self._state=logic_tkinter.DiscState(self._turn,self._win_mode,
                                                self._row,self._col)

            self._draw_board()

        
            self._board_setup = True

            

    def _black_initial(self)->None:
        '''
        place the initial black discs before place the white initials and starts the game
        '''

        if self._board_setup:
            
            self._turn='B'
            self._state.turn=self._turn


        
            

    def _white_initial(self)->None:
        '''
        place the initial white discs before game starts
        '''
        if self._black_done_was_clicked:
            self._turn='W'
            self._state.turn=self._turn
            self._turn_text.set('turn: {}'.format(self._turn))
            
           


    def _start_game(self)->None:
        '''
        starts and continues the game until the game is over
        '''
        if self._white_done_was_clicked:
            self._turn=self._first_turn
            self._state.turn=self._turn
            self._turn_text.set('turn: {}'.format(self._turn))
            self._gamestart=True


    def _game_loop(self,event_x:int,event_y:int)->None:
        '''
        loop the game, as draw disc one at each time and update the board,
        until one of the players wins the game or the game ends itself
        '''
        h = self._canvas.winfo_height()
        w = self._canvas.winfo_width()
        
        if self._board_setup==False or self._black_done_was_clicked==False or \
               self._white_done_was_clicked==False:

                self._center_text.set('Please place the initial discs\
                for both sides first')
                
                
        else:
            if self._state.full_board()==True or \
               self._state.empty_board_check()==False:
                self._center_text.set('Game Over!\n{} has won!'.\
                                   format(self._state.winner()))
                
                self._close()
       
            else:
                self._turn_text.set('turn: {}'.format(self._turn))
                game=self._state.handle_game([[event_x,event_y]],w,h)
                if game=='B' or game=='W' or game=="No One":
                    self._center_text.set('Game Over!\n{} has won!'.format(self._state.winner()))
                  
                    self._close()
                else:
                    try:
                        self._draw_disc([event_x,event_y],self._turn)
                        self._state.handle_click([event_x,event_y],self._turn)
                        self._score_count()
                        self._turn=self._state.opposite_turn()
                        self._state.turn=self._turn
                    except:
                        self._close()
                

            
          
    def _on_button_down(self,event:tkinter.Event)->None:
        '''
        track where the player wants to place the disc on canvas,
        draw all discs
        '''
       

        if self._board_setup:
            self._click_down(event.x,event.y)
            self._black_done_was_clicked=True
            self._click_down(event.x,event.y)
            self._white_done_was_clicked=True
            
            
        while self._gamestart:
            self._game_loop(event.x,event.y)
            

           
    def _close(self)->None:
        '''
        close the entire program
        '''

        while True:
            response=input('If you would like to close the window now, please input "CLOSE".\n')
            if response.upper()=="CLOSE":
                self._root_window.destroy()
                quit()
            else:
                self._root_window.wait_window()

    
    


    def _click_down(self,event_x:int,event_y:int)->None:
        '''
        place the initial discs and update the initial gameboard
        '''

        h = self._canvas.winfo_height()
        w = self._canvas.winfo_width()


        self._state.handle_click([event_x,event_y],self._turn)
        
        if self._turn=='B':
            tiles=self._state.from_pixel(self._state.black_discs(),w,h)
        else:
            tiles=self._state.from_pixel(self._state.white_discs(),w,h)

        self._state.flip_all(tiles)
        
        for disc in self._state.black_discs():
            self._draw_disc(disc,'B')
        for disc in self._state.white_discs():
            self._draw_disc(disc,'W')

        self._score_count()




    def _score_count(self)->None:
        '''
        Display the while discs and black discs on the board
        '''
        self._score_board.set('B: {}     W: {}'.format(self._state.total_black(),
                                                    self._state.total_white()))
                            




    def run(self) -> None:
        '''
        START THE GAME BY LOOPING THE EVENT
        '''

        self._root_window.mainloop()

        



    def _on_canvas_resized(self,event:tkinter.Event) -> None:
        '''
        RESIZE THE BOARD WHEN WINDOW SIZE CHANGE

        '''
        self._draw_board()
        self._draw_discs()

        



    def _draw_disc(self,point:list,color:str)->None:
        '''
        draw and place the disc
        '''
          
        h = self._canvas.winfo_height()
        w = self._canvas.winfo_width()


        for tile_x in range(self._col):
            left_end=int(w/self._col*tile_x)
            right_end=int(w/self._col*(tile_x+1))
            for tile_y in range(self._row):
                up_end=int(h/self._row*tile_y)
                bottom_end=int(h/self._row*(tile_y+1))
               
                if point[0] in range(left_end,right_end) and\
                   point[1] in range(up_end,bottom_end):
                    if color=='B':

                        self._canvas.create_oval(left_end,up_end,
                                             right_end,bottom_end,fill='Black')
                    else:
                        self._canvas.create_oval(left_end,up_end,
                                             right_end,bottom_end,fill='white')
    

        
    def _draw_board(self)->None:
        '''
        DRAW THE RESIZABLE BOARD
        '''


        lines_x=[]
        
        
        self._canvas.delete(tkinter.ALL)
        
        h = self._canvas.winfo_height()

        w = self._canvas.winfo_width()

        for col_line in range(self._col):
            line_x =  w / self._col * col_line

            self._canvas.create_line(line_x,0,line_x,h,fill='Black')

        for row_line in range(self._row):
            line_y = h / self._row * row_line

            self._canvas.create_line(0,line_y,w,line_y,fill='Black')
            

        self._score_count()
        
        



    def _draw_discs(self)->None:
        '''
        make all the discs on the board bigger or smaller when resizing canvas
        '''

##        self._canvas.delete(tkinter.ALL)
        
        for disc in self._state.black_discs():
            self._draw_disc(disc,'B')

        for disc in self._state.white_discs():
            self._draw_disc(disc,'W')
                                                    
     

            

if __name__=='__main__':


    OthelloApplication().run()

