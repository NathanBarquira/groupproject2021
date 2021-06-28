import tkinter as tk

class Map:
    def __init__(self):
        self.board_setup()
        self.create_map()
        self.runUI()

    def board_setup(self):
        """ Creating the board """
        self.master = tk.Tk()
        self.master.title('Aim Trainer')
        self.master.geometry('+{}+{}'.format(700, 300))
        self.master.geometry('800x600')
        self.master.configure(background='white')
        self.master.resizable(0, 0)

    def runUI(self):
        """ run the UI """
        self.master.mainloop()

    def create_map(self):
        image = tk.PhotoImage(file='map.png')
        self.map = tk.Label(self.master)
        self.map.image = image
        self.map.configure(image=image)
        self.map.grid(column=0, row=0, columnspan=10, rowspan=10)

    def spawn_player(self):
        self.player = tk.Label(self.master, color='black')


if __name__ == '__main__':
    game = Map()
