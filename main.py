# Example file showing a basic pygame "game loop"
import tkinter as tk

import random


COLORS = {
    0: 'white',
    2: "#FFCC99",    # Light Apricot
    4: "#FFB6C1",    # Light Pink
    8: "#FFD700",    # Gold
    16: "#98FB98",   # Pale Green
    32: "#87CEEB",   # Sky Blue
    64: "#FFA07A",   # Light Salmon
    128: "#AFEEEE",  # Pale Turquoise
    256: "#F0E68C",  # Khaki
    512: "#DDA0DD",  # Plum
    1024: "#B0E0E6", # Powder Blue
    2048: "#FFE4E1",  # Misty Rose
}

NUMBERS = [ 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]


class App(tk.Tk):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2048 game")
        self.root.minsize(400, 400)
        self.root.resizable(False, False)

        self.root.grid()
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.create_new_board()
        self.board_full = True
        
        self.root.bind("<Up>", self.on_up_arrow)
        self.root.bind("<Down>", self.on_down_arrow)
        self.root.bind("<Left>", self.on_left_arrow)
        self.root.bind("<Right>", self.on_right_arrow)
        
        self.root.mainloop()
        
        
    def create_new_board(self):
        self.squares = [[],[],[],[]]
        #Creates empty squares
        for n in range(4):
            for y in range(4):
                text = 0
                square_label = tk.Label(self.root, text=text, font=('TkDefaultFont', 20, 'bold'), fg='#FDFFD2', height=5, width=10, borderwidth=5)
                square_label.configure(bg=COLORS[square_label.cget('text')])
                self.squares[n].append(square_label)
                square_label.grid(column=n, row=y, columnspan=1, rowspan=1, padx=5, pady=5)

        self.generate_rand_squares()

        
                
    def generate_rand_squares(self):
        generated_squares = 0
        
        while generated_squares < 1:
            
            randx, randy = (random.randint(0, 3), random.randint(0, 3))
            # print(randx, randy)
            
            if not self.check_full():
                if self.squares[randx][randy].cget('text') == 0:
                    self.squares[randx][randy].configure(text=2, bg=COLORS[2])
                    generated_squares += 1
      
            else:
                break
            

    
    def check_full(self):
        item_list = []
        for row_num in range(len(self.squares)):
            for item in self.squares[row_num]:
                item_list.append(int(item.cget('text')))
        if 0 in item_list:
            return False
        else:
            return True
        
    
    def make_move(self, direction):
        if direction == "Up":
            table = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                    [(1, 0), (1, 1), (1, 2), (1, 3)],
                    [(2, 0), (2, 1), (2, 2), (2, 3)],
                    [(3, 0), (3, 1), (3, 2), (3, 3)]]
            
        elif direction == 'Left':
            table = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                    [(0, 1), (1, 1), (2, 1), (3, 1)],
                    [(0, 2), (1, 2), (2, 2), (3, 2)],
                    [(0, 3), (1, 3), (2, 3), (3, 3)]]
            
        elif direction == 'Down':
            table = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                    [(1, 3), (1, 2), (1, 1), (1, 0)],
                    [(2, 3), (2, 2), (2, 1), (2, 0)],
                    [(3, 3), (3, 2), (3, 1), (3, 0)]]
            
        elif direction == 'Right':
            table = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                    [(3, 1), (2, 1), (1, 1), (0, 1)],
                    [(3, 2), (2, 2), (1, 2), (0, 2)],
                    [(3, 3), (2, 3), (1, 3), (0, 3)]]

        for column_coor in table:
            
            first_square_coor = column_coor[0]
            second_square_coor = column_coor[1]
            third_square_coor = column_coor[2]
            forth_square_coor = column_coor[3]
            
            first_square = self.squares[first_square_coor[0]][first_square_coor[1]]
            second_square = self.squares[second_square_coor[0]][second_square_coor[1]]
            third_square = self.squares[third_square_coor[0]][third_square_coor[1]]
            forth_square = self.squares[forth_square_coor[0]][forth_square_coor[1]]
            
            column = [first_square, second_square, third_square, forth_square]
            
            for n in range(len(column) - 1):
                if column[n].cget('text') == column[n + 1].cget('text'):
                    new_value = int(column[n].cget('text') * 2)
                    column[n].configure(text=new_value, bg=COLORS[new_value])
                    column[n + 1].configure(text=0, bg=COLORS[0])
                elif column[n].cget('text') == '0':
                    new_value = int(column[n + 1].cget('text'))
                    column[n].configure(text=new_value, bg=COLORS[new_value])
                    column[n + 1].configure(text=0, bg=COLORS[0])
                else:
                    pass

    
    def on_up_arrow(self, event):
        self.make_move('Up')
        self.generate_rand_squares()
        # print("Up arrow key pressed!")
        
        # for line in self.squares:
        #     print("\n")
        #     for square in line:
        #         print(square.cget('text'))
        
        
    def on_down_arrow(self, event):
        self.make_move('Down')
        self.generate_rand_squares()
        # print("Down arrow key pressed!")
    
    
    def on_right_arrow(self, event):
        self.make_move('Right')
        self.generate_rand_squares()
        # print("Right arrow key pressed!")
    
    
    def on_left_arrow(self, event):
        self.make_move('Left')
        self.generate_rand_squares()
        # print("Left arrow key pressed!")
            
        
            
        
                    
      

if __name__ == "__main__":
    app = App()