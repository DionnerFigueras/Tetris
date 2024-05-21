class TetrisAI:
    def __init__(self, game):
        self.game = game
        
    def get_grid_state(self):
        return self.game.grid.get_state()

    def get_current_block(self):
        return self.game.current_block
    
    def evaluate_move(self, move):
        # Heuristic function to evaluate the move's potential score and risk of game over
        score = 0
        risk = 0

        # Calculate the potential score based on the move
        if move == "lock":
            score += self.game.grid.crear_full_rows() * 100
        elif move == "rotate":
            score += 10
        elif move == "move_down":
            score += 1

        # Calculate the risk of game over based on the move
        if move == "lock" and self.game.game_over:
            risk += 1000
        elif move == "move_down" and self.game.game_over:
            risk += 500

        return score - risk

    def choose_move(self):
        moves = ["lock", "rotate", "move_down", "move_left", "move_right"]
        best_move = None
        best_score = -1000

        for move in moves:
            score = self.evaluate_move(move)
            if score > best_score:
                best_move = move
                best_score = score

        return best_move

    def play(self):
        while not self.game.game_over:
            move = self.choose_move()
            if move == "lock":
                self.game.lock_block()
            elif move == "rotate":
                self.game.rotate()
            elif move == "move_down":
                self.game.mode_down()
            elif move == "move_left":
                self.game.move_left()
            elif move == "move_right":
                self.game.move_right()

""" 
Basándome en todo el código proporcionado me gustaría que me ayudarais a crear un automata que sea capaz de jugar al juego de forma totalmente autónoma.
import pygame
import random
from JuegoTetris import JuegoTetris
Based on all the code provided I would like you to help me to create an agent that is able to play the game in a fully autonomous way.

class TetrisAutomaton:
    def __init__(self, game):
        self.game = game
        self.best_move = None

    def get_best_move(self):
        # Simple heuristic to choose the best move
        # Try to place the block in the middle of the grid
        # and rotate it to fit the most
        best_score = -float('inf')
        best_move = None
        for rotation in range(4):
            for x in range(self.game.grid.num_rows):
                self.game.current_block.rotate(rotation)
                self.game.current_block.move(x, 0)
                if self.game.block_fits():
                    score = self.game.score
                    if score > best_score:
                        best_score = score
                        best_move = (rotation, x)
        return best_move

    def play(self):
        while not self.game.game_over:
            self.best_move = self.get_best_move()
            if self.best_move:
                rotation, x = self.best_move
                self.game.current_block.rotate(rotation)
                self.game.current_block.move(x, 0)
                self.game.mode_down()
                self.game.update_score(0, 1)
            else:
                self.game.game_over = True
            pygame.display.update()
            pygame.time.delay(100)

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 620))
    pygame.display.set_caption('Tetris Automaton')
    game = JuegoTetris()
    automaton = TetrisAutomaton(game)
    automaton.play()
    pygame.quit()


if __name__ == '__main__':
    main()
 """

