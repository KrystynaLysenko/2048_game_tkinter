# Example file showing a basic pygame "game loop"
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2048 game")
        self.root.minsize(400, 400)

        self.root.grid()
        
        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)
        
        self.draw_squares()
        
        self.root.mainloop()
        
        
    def draw_squares(self):
        # self.game_frame = tk.Frame(self.root, bg="blue")
        # self.game_frame.grid(sticky="snew", row=0, column=0, columnspan=4, rowspan=4)
        
        #Squares
        for n in range(4):
            for y in range(4):
                label = tk.Label(self.root, text=2048, font=('TkDefaultFont', 15), fg='white', height=10, width=20, borderwidth=5, bg='#DA7297')
                label.grid(column=n, row=y, columnspan=1, rowspan=1, padx=5, pady=5)
                    
      

if __name__ == "__main__":
    app = App()