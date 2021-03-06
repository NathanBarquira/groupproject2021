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
        # self.master.geometry('800x600')
        self.master.configure(background='white')
        self.master.resizable(0, 0)

    def runUI(self):
        """ run the UI """
        self.master.mainloop()

    def create_map(self):
        """ creates the map for the game """

        # initialize variables for the game
        self.null_list = []
        self.x = 0
        self.y = 0
        image = tk.PhotoImage(file='map.png')

        for i in range(21):
            for j in range(21):
                self.map = tk.Button(self.master, width=4, height=2, bg='red')
                self.map.grid(row=i, column=j)

        self.map_pic = tk.Label(self.master, width=795, height=860)
        self.map_pic.image = image
        self.map_pic.configure(image=image)
        self.map_pic.grid(row=0, column=0, columnspan=100, rowspan=300)

        # self.map = tk.Label(self.master)
        # self.map.image = image
        # self.map.configure(image=image)
        # self.map.grid(column=0, row=0, columnspan=20, rowspan=20)

    def spawn_player(self):
        self.player = tk.Label(self.master, width=4, height=2, bg='black')
        player_image = tk.PhotoImage(file='panda.png')
        # self.player.image = player_image
        # self.player.configure(image=player_image)
        self.player.grid(row=self.x, column=self.y)

    def make_move(self):
        self.master.bind('<a>', self.made_move_a)
        self.master.bind('<w>', self.made_move_w)
        self.master.bind('<s>', self.made_move_s)
        self.master.bind('<d>', self.made_move_d)

    def made_move_d(self, event=None):
        if self.y >= 20:
            print('DEBUG: you hit a wall!')
            self.player.destroy()
            self.spawn_player()
        else:
            if (self.x, self.y + 1) == (self.rock_x, self.rock_y):
                print('DEBUG: you hit rock')
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
            if (self.x - 1, self.y) == (self.rock_x, self.rock_y):
                print('DEBUG: you hit rock')
                self.player.destroy()
                self.spawn_player()
            else:
                self.x -= 1
                self.player.destroy()
                self.spawn_player()

    def made_move_s(self, event=None):
        if self.x >= 20:
            print('DEBUG: you hit a wall!')
            self.player.destroy()
            self.spawn_player()
        else:
            if (self.x + 1, self.y) == (self.rock_x, self.rock_y):
                print('DEBUG: you hit rock')
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
            if (self.x, self.y - 1) == (self.rock_x, self.rock_y):
                print('DEBUG: you hit rock')
                self.player.destroy()
                self.spawn_player()
            else:
                self.y -= 1
                self.player.destroy()
                self.spawn_player()

    def random_terrain(self):
        self.rock_x = random.randint(0, 20)
        self.rock_y = random.randint(0, 20)
        self.null_list.append((self.rock_x, self.rock_y))
        self.rock = tk.Label(self.master, width=10, height=10)
        rock_image = tk.PhotoImage(file='rock.png')
        self.rock.image = rock_image
        self.rock.configure(image=rock_image)
        self.rock.grid(row=self.rock_x, column=self.rock_y)

    def check_null(self, movement='default', positive=False):
        """ checks if movement is to rock """
        if (self.x, self.y) == (self.rock_x, self.rock_y):
            print('DEBUG: you hit rock')
            if positive:
                movement -= 1
            else:
                movement += 1
            self.player.destroy()
            self.spawn_player()
            return


if __name__ == '__main__':
    game = Map()
