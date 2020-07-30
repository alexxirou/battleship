# -*- coding: utf-8 -*-
import tkinter as tk
import random
import battleship

battleship.MISS = 'MISS'
battleship.HIT = 'HIT'
battleship.DESTROYED = 'DESTROYED'




class Battleship(tk.Frame):
    def __init__(self, player_grid, opponent_grid):
        root = tk.Tk()
        super().__init__(root)
        root.protocol("WM_DELETE_WINDOW", root.destroy)
        self.pack()
        self.player_grid = player_grid
        self.opponent_grid = opponent_grid
        self.scale = 20
        self.strategy = random_shoot

        self.create_widgets()

    def create_widgets(self):
        self.canvas1 = tk.Canvas(self, width=self.player_grid.sizex * self.scale, height=self.player_grid.sizey * self.scale, bg='white')
        self.canvas1.pack()
        self.show_grid_player()

        self.canvasmiddle = tk.Canvas(self, width=self.scale, height=self.scale)
        self.canvasmiddle.pack()

        self.canvas2 = tk.Canvas(self, width=self.opponent_grid.sizex * self.scale, height=self.opponent_grid.sizey * self.scale, bg='white')
        self.canvas2.bind("<Button-1>", self.shoot)
        self.canvas2.pack()
        self.show_grid_opponent()

    def shoot(self, event):
        opp = battleship.BlindGrid(self.opponent_grid)
        b = battleship.BlindGrid(self.player_grid)
        pointx = event.x // self.scale
        pointy = event.y // self.scale
        shot_before = any((pointx,pointy) in s.positions for s in self.opponent_grid.ships)
        if len(opp.sunken_ships) < 5:
            res, ship = self.opponent_grid.shoot((pointx,pointy))
            """if the win condition has not be met the player will shoot."""
            if res == battleship.MISS and not shot_before:
                self.canvas2.create_oval(pointx * self.scale+1, pointy * self.scale+1, (pointx +1)* self.scale-1, (pointy +1) * self.scale-1, fill= 'blue')
            elif res != battleship.MISS:
                if res == battleship.HIT:
                    print(res)
                self.canvas2.create_oval(pointx * self.scale+1, pointy * self.scale+1, (pointx +1)* self.scale-1, (pointy +1) * self.scale-1, fill= 'red')
            if ship is not None:
                print(ship.name, res+"!!!" )
                self.show_sunk(ship)
            self.let_opponent_shoot()

        if len(opp.sunken_ships) >= 5 and len(b.sunken_ships) < 5 :
            print("Game over! You win!")
            """Win condition if all of the opponent's ships are in the list and not all of the player's ships are not on the lose list. """





    def let_opponent_shoot(self):
        opp = battleship.BlindGrid(self.opponent_grid)
        b = battleship.BlindGrid(self.player_grid)
        x, y = self.strategy(b)
        shot = (x, y)
        if len(b.sunken_ships) >= 5 and len(opp.sunken_ships) < 5:
            print("Game over. You lost...")
            """Lose condition."""
            return
        while shot in b.misses.union(b.hits) and len(b.sunken_ships) < 5 and len(opp.sunken_ships) < 5:
                #print(shot)

                x, y = self.strategy(b)
                shot =(x,y)
                """if the shot generated is in the list of the previous hits/misses, and the game win or lose condition is not met, a new shot will be generated."""
        res, ship = self.player_grid.shoot((x,y))
        if res == battleship.MISS:
            self.canvas1.create_oval(x * self.scale+1, y * self.scale+1, (x +1)* self.scale-1, (y +1) * self.scale-1, fill= 'blue')
            #print(b.misses)
            """Adds previous shot to list"""

        else:
            self.canvas1.create_oval(x * self.scale+1, y * self.scale+1, (x +1)* self.scale-1, (y +1) * self.scale-1, fill= 'yellow')

            #print(b.hits)
        return

        """Breaks possible unwanted loops."""


    def show_sunk(self, ship):
        for x, y in ship.positions:
            self.canvas2.create_rectangle(x * self.scale, y * self.scale, (x + 1) * self.scale -1, (y + 1) * self.scale -1, fill= 'red', outline='#D3D3D3')

    def show_alive(self):
        for rect in self.alive:
            self.canvas.delete(rect)
        points = self.board.points
        self.alive = {self.canvas.create_rectangle(point.x * self.scale, point.y * self.scale,
                                                   (point.x + 1) * self.scale -1,
                                                   (point.y + 1) * self.scale -1,
                                                   fill= 'black', outline='#D3D3D3')
                                            for point in points}
    def show_grid_player(self):
        for i in range(1, self.player_grid.sizex):
            self.canvas1.create_line(i * self.scale, 0, i * self.scale, self.player_grid.sizey * self.scale, fill = '#D3D3D3')
        for j in range(1, self.player_grid.sizey):
            self.canvas1.create_line(0, j * self.scale, self.player_grid.sizex * self.scale, j * self.scale, fill = '#D3D3D3')
        for ship in self.player_grid.ships:
            for x, y in ship.positions:
                self.canvas1.create_rectangle(x * self.scale, y * self.scale,
                                                   (x + 1) * self.scale -1,
                                                   (y + 1) * self.scale -1,
                                                   fill= 'red', outline='#D3D3D3')

    def show_grid_opponent(self):
        for i in range(1, self.opponent_grid.sizex):
            self.canvas2.create_line(i * self.scale, 0, i * self.scale, self.opponent_grid.sizey * self.scale, fill = '#D3D3D3')
        for j in range(1, self.opponent_grid.sizey):
            self.canvas2.create_line(0, j * self.scale, self.opponent_grid.sizex * self.scale, j * self.scale, fill = '#D3D3D3')


def random_shoot(blind_grid):
    sunkname = []
    b = battleship.BlindGrid(battleship.g)
    res =0
    for ship in b.sunken_ships:
        sunkname.append(ship.name)
    print(sunkname)
    for tuple in b.hits:
        if ("Carrier", "Battleship") not in sunkname and (tuple[0], tuple[1]) in b.hits and (tuple[0] + 1, tuple[1]) in b.hits  and (tuple[0] + 2, tuple[1]) not in b.misses.union(b.hits) and (tuple[0] + 2 <= 10):
            res = int(tuple[0] + 2), int(tuple[1])
            return res
            #print(res)
        elif ("Carrier", "Battleship") not in sunkname and (tuple[0], tuple[1]) in b.hits and (tuple[0] - 1, tuple[1]) in b.hits and (tuple[0] - 2, tuple[1]) not in b.misses.union(b.hits) and (tuple[0] - 2 >= 0):
            res = int(tuple[0] - 2), int(tuple[1])
            #print(res)
        elif ("Carrier", "Battleship") not in sunkname and (tuple[0], tuple[1]) in b.hits and (tuple[0], tuple[1] + 1) in b.hits and (tuple[0], tuple[1] + 2) not in b.misses.union(b.hits) and (tuple[1] + 2 <= 10):
            res = int(tuple[0]), int(tuple[1] + 2)
            return res
            #print(res)
        elif ("Carrier", "Battleship") not in sunkname and (tuple[0], tuple[1]) in b.hits and (tuple[0], tuple[1] - 1) in b.hits and (tuple[0], tuple[1] - 2) not in b.misses.union(b.hits) and (tuple[1] - 2 >= 0):
            res = int(tuple[0]), int(tuple[1] - 2)
            return res
            #print(res)

        elif (tuple[0], tuple[1]) in b.hits and (tuple[0] + 1, tuple[1]) not in b.misses.union(b.hits) and (tuple[0] + 1 in range(0, 10)):
            res = int(tuple[0] + 1), int(tuple[1])
            return res
                #print(res)
        elif (tuple[0], tuple[1]) in b.hits and (tuple[0] - 1, tuple[1]) not in b.misses.union(b.hits) and (tuple[0] -1 in range(0, 10)):
            res = int(tuple[0] - 1), int(tuple[1])
            return res
            #print(res)
        elif (tuple[0], tuple[1]) in b.hits and (tuple[0], tuple[1] + 1) not in b.misses.union(b.hits) and (tuple[1] + 1 in range(0, 10)):
            res = int(tuple[0]), int(tuple[1] + 1)
            return res
             #print(res)
        elif (tuple[0], tuple[1]) in b.hits and (tuple[0], tuple[1] - 1) not in b.misses.union(b.hits) and (tuple[1] - 1 in range(0, 10)):
            res = int(tuple[0]), int(tuple[1] - 1)
            return res
            #print(res)
        """Conditions for AI to shoot around a previous "hit" before shooting at random. """
    res1= random.choice([i for i in range(0, blind_grid.sizex)]), random.choice([i for i in range(0, blind_grid.sizey)])
    return res1
    """Generates random coordinates to be used for shots by AI."""

Battleship(battleship.g, battleship.g2).mainloop()