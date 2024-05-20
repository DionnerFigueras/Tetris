#Game board

import pygame
from colors import Colors
class Grid:
    def __init__(self):
        self.num_rows = 20 #numero de filas de la matriz
        self.num_cols = 10 #numero de columnas de la matriz
        self.cell_size = 30 #Tamaño de cada cuadro en la matriz
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)] #creamos una matriz de 20 * 10
        self.colors = Colors.get_cell_colors()# inicializamos los colora a utilizar


    def gridd(self):
        return [cell for row in self.grid for cell in row]
        #return [row[:] for row in self.grid] 

    def get_state(self):
        return self.grid

    #Clase para dibujar la cuadricula (matriz)
    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end = " ")
            print() 
    
    # Define si un bloque se encuentra dentro la cuadricula
    def is_inside(self, row, column):
        if (row >= 0 and row < self.num_rows) and (column >= 0 and column < self.num_cols):
            return True
        return False

    # Verifica si una casilla esta vacia
    def is_empty(self, row, colum):
        if self.grid[row][colum] == 0:
            return True
        return False

    def grid_empty(self):
        return all(cell == 0 for row in self.grid for cell in row)

    # Verifica si una fila se encuentra llena
    def is_row_full(self, row):
        for colum in range(self.num_cols):
            if self.grid[row][colum] == 0:
                return False
        return True
    
    def empty_cell(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return column
        return -1
    
    #Elimina la fila llena
    def clear_row(self, row):
        for colum in range(self.num_cols):
            self.grid[row][colum] = 0

    #Mueve una serie de filas hacia abajo
    def move_row_down(self, row, num_row):
        for colum in range(self.num_cols):
            self.grid[row+num_row][colum] = self.grid[row][colum]
            self.grid[row][colum] = 0

    #Utiliza las funciones de is_row_full, clear_row y move_row_down
    def crear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1,0,-1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed +=1
            elif completed > 0:
                self.move_row_down(row,completed)
        return completed
    
    def cell_ocuped(self):
        for row in range(self.num_rows-1,0,1):
            if self.empty_cell() == -1:
                return True
        return False
    
    #Reinicia el juego
    def reset(self):
        for row in range(self.num_rows):
            for colum in range(self.num_cols):
                self.grid[row][colum] = 0

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size + 11, row*self.cell_size + 11, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)