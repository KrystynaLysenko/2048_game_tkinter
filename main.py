# Example file showing a basic pygame "game loop"
import tkinter as tk

import random


COLORS = {
    " " : 'white',
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
    'None': 'grey'
}

NUMBERS = [" ", 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]


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
        self.board_full = False
        
        self.root.bind("<Up>", self.on_up_arrow)
        
        self.root.mainloop()
        
        
    def create_new_board(self):
        self.squares = [[],[],[],[]]
        #Squares
        for n in range(4):
            for y in range(4):
                square_label = tk.Label(self.root, text=" ", font=('TkDefaultFont', 20, 'bold'), fg='#FDFFD2', height=5, width=10, borderwidth=5)
                square_label.configure(bg=COLORS[square_label.cget('text')])
                self.squares[n].append(square_label)
                square_label.grid(column=n, row=y, columnspan=1, rowspan=1, padx=5, pady=5)

        
                
    def update_board(self):
        generated_squares = 0
        while generated_squares < 2:
            
            randx, randy = (random.randint(0, 3), random.randint(0, 3))
            print(randx, randy)
            
            if self.squares[randx][randy].cget('text') == " ":
                self.squares[randx][randy].configure(text=2, bg=COLORS[2])
                generated_squares += 1
            
                
        
                
    
    def on_up_arrow(self, event):
        self.update_board()
        print("Up arrow key pressed!")
        
        for line in self.squares:
            print("\n")
            for square in line:
                print(square.cget('text'))
        
        
    def on_down_arrow(self, event):
        pass
    
    
    def on_right_arrow(self, event):
        pass
    
    
    def on_down_arrow(self, event):
        pass
            
        
            
        
                    
      

if __name__ == "__main__":
    app = App()