""" import multiprocessing
import pygame
import sys
from functions import JuegoTetris
from colors import Colors
from Prueba import TetrisAI

class Implementation:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        self.screen = pygame.display.set_mode((500, 620))
        pygame.display.set_caption('Tetris en Pythno')

        # Create a JuegoTetris object
        self.game = JuegoTetris()

    def play(self):
        # Set up the game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle user input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.game.move_right()
                    elif event.key == pygame.K_DOWN:
                        self.game.mode_down()
                    elif event.key == pygame.K_SPACE:
                        self.game.rotate()

            # Update the game state
            self.game.mode_down()

            # Render the game screen
            self.screen.fill(Colors.dark_blue)
            self.game.draw(self.screen)
            pygame.display.update()

class ImplementationAI:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        self.screen = pygame.display.set_mode((500, 620))
        pygame.display.set_caption('Tetris en Pythno - IA Mode')

        # Create a JuegoTetris object and a TetrisAI object
        self.automata = JuegoTetris()
        self.ai = TetrisAI(self.automata)

    def play(self):
        # Set up the game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update the game state using the AI logic
            self.automata.play_autonomously()

            # Render the game screen
            self.screen.fill(Colors.dark_blue)
            self.automata.draw(self.screen)
            pygame.display.update()

def run_human_mode():
    impl = Implementation()
    impl.play()

def run_ai_mode():
    impl_ai = ImplementationAI()
    impl_ai.play()

if __name__ == '__main__':
    # Create two separate processes for human mode and AI mode
    p1 = multiprocessing.Process(target=run_human_mode)
    p2 = multiprocessing.Process(target=run_ai_mode)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join() """