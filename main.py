import tkinter as tk
import threading
import random


class Map:
    def __init__(self):
        self.board_setup()
        self.create_map()
        self.spawn_player()
        self.random_terrain()
        self.make_move()
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
        self.x = 10
        self.y = 10
        image = tk.PhotoImage(file='map.png')
        self.map = tk.Label(self.master)
        self.map.image = image
        self.map.configure(image=image)
        self.map.grid(column=0, row=0, columnspan=20, rowspan=20)

    def spawn_player(self):
        self.player = tk.Label(self.master, width=50, height=50)
        player_image = tk.PhotoImage(file='panda.png')
        self.player.image = player_image
        self.player.configure(image=player_image)
        self.player.grid(row=self.x, column=self.y)

    def make_move(self):
        self.master.bind('<a>', self.made_move_a)
        self.master.bind('<w>', self.made_move_w)
        self.master.bind('<s>', self.made_move_s)
        self.master.bind('<d>', self.made_move_d)

    def made_move_d(self, event=None):
        if self.y >= 19:
            print('DEBUG: you hit a wall!')
            self.player.destroy()
            self.spawn_player()
        else:
            self.y += 1
            self.player.destroy()
            self.spawn_player()

    def made_move_w(self, event=None):
        if self.x <= 0:
            print('DEBUG: you hit a wall!')
            self.player.destroy()
            self.spawn_player()
        else:
            self.x -= 1
            self.player.destroy()
            self.spawn_player()

    def made_move_s(self, event=None):
        if self.x >= 19:
            print('DEBUG: you hit a wall!')
            self.player.destroy()
            self.spawn_player()
        else:
            self.x += 1
            self.player.destroy()
            self.spawn_player()

    def made_move_a(self, event=None):
        if self.y <= 0:
            print('DEBUG: you hit a wall!')
            self.player.destroy()
            self.spawn_player()
        else:
            self.y -= 1
            self.player.destroy()
            self.spawn_player()

    def random_terrain(self):
        rock_x = random.randint(0, 20)
        rock_y = random.randint(0, 20)
        self.rock = tk.Label(self.master, width=50, height=50)
        rock_image = tk.PhotoImage(file='rock.png')
        self.rock.image = rock_image
        self.rock.configure(image=rock_image)
        self.rock.grid(row=rock_x, column=rock_y)


if __name__ == '__main__':
    game = Map()
