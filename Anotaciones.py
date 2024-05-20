import multiprocessing
import pygame, sys
from functions import JuegoTetris
from colors import Colors

class Implementation:

    def run_game():
        implementation = Implementation()
        implementation.play()

    if __name__ == '__main__':
        # Create two separate processes
        process1 = multiprocessing.Process(target=run_game)
        process2 = multiprocessing.Process(target=run_game)

        # Start both processes
        process1.start()
        process2.start()

        # Wait for both processes to finish
        process1.join()
        process2.join()