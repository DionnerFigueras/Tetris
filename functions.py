#Game functions

import copy
from grid import Grid
from blocks import *
import random

class JuegoTetris:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock() ,TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.best_move = None
        self.prev_block = None
        self.prev_grid = None


    #Actualizar el score
    def update_score(self, lines_creared, move_down_point):

        if lines_creared == 1:
            self.score += 100
        elif lines_creared == 2:
            self.score += 300
        elif lines_creared >= 3:
            self.score += 500
        self.score += move_down_point

# Generar los bloques de forma aleatoria
    def get_random_block(self):
        if len(self.blocks) == 0:
           self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock() ,TBlock(), ZBlock()]

        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block    
    
# Movimientos de los bloques

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1) 
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def mode_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

# Bloques un loque cuando llegue al final 
    def lock_block(self):
        tiles = self.current_block.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.colum] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_creared = self.grid.crear_full_rows()
        self.update_score(rows_creared, 0)
        if self.block_fits() == False:
            self.game_over = True

#Reiniciar el juego
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock() ,TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

#Colisiones
    def block_fits(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.colum) == 0: 
                return False
        return True
    
 # Rota el bloque   
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False:
            self.current_block.undo_rotation()

# Establece el limite de la pantalla 
    def block_inside(self):
        tiles = self.current_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.colum) == False:
                return False
        return True
 
#    FUNCIONES DEL AUTOMATA    
    
    #Guarda es estado actual del juego
    def save_state(self):
        self.prev_block = self.current_block
        self.prev_grid = copy.deepcopy(self.grid.grid)
    
    #Restaura el juego utilizando la funcion save_state
    def restore_state(self):
        self.current_block = self.prev_block
        self.grid.grid = copy.deepcopy(self.prev_grid)
    
    #Evaluta el movimiento    
    def evaluate_state(self, grid):
        filled_cells = sum(sum(row) for row in grid.grid)
        holes = sum(1 for row in grid.grid for cell in row if cell == 0 and any(grid.grid[i][j] != 0 for i in range(row.index(cell), len(grid.grid)) for j in range(len(row))))
        height = max(max(row.index(cell) for cell in row if cell != 0) for row in grid.grid)
        return -filled_cells - holes * 2 - height * 3
    
    #posibles movimientos
    def moves(self, direction):
        if direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()
        elif direction == 'down':
            self.mode_down()
        elif direction == 'rotate':
            self.rotate()
#Automata 
def play_autonomously(self):
    while not self.game_over:
        if not self.grid.is_empty():
            best_move = None
            best_score = float('-inf')
            for move in [self.move_left(), self.move_right(), self.rotate(), self.mode_down()]:
                self.save_state()
                score = self.evaluate_state(self.grid)
                if score > best_score:
                    best_move = move
                    best_score = score
                self.restore_state()
            if best_move:
                best_move()
            else:
                self.mode_down()
            self.update_score(0, 1)
        else:
            self.mode_down()
            self.update_score(0, 1)
            
#   FIN DE LAS FUNCIONES DEL AUTOMATA


# Dibujar el juego en pantalla
    def draw(self, screen):
        self.grid.draw(screen)

        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
            
