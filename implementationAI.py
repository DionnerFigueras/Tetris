import pygame, sys
from functions import JuegoTetris
from colors import Colors
from functionsAI import TetrisAI

class ImplementationAI:
  def __init__(self):
    #Inicializamos pygames
    pygame.init()
    #Fuenta para las letras
    self.title_font = pygame.font.Font(None, 40)
    self.score_surface = self.title_font.render("Score", True, Colors.white)
    self.next_surface = self.title_font.render("Next", True, Colors.white)
    self.game_over_surface = self.title_font.render("Game Over", True, Colors.white)

    self.score_rect = pygame.Rect(320, 55, 170, 60)
    self.next_rect = pygame.Rect(320, 215, 170, 180)

    #Definimos el alto y ancho de la pantalla
    self.screen = pygame.display.set_mode((500, 620))

    #Definimos un titulo para el juego
    pygame.display.set_caption('Tetris en Pythno - IA Mode')

    #Reloj del juego
    self.clock = pygame.time.Clock()

    self.automata = JuegoTetris()
    self.ai = TetrisAI(self.automata)

  def play(self):
    #Evento de movimiento de descenso de los bloques
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 200)


    #Este ciclo se encargara de ejecutar el juego hasta que termine
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

          
        if self.automata.score >= 5000:
          self.automata.game_over = True
      
        if event.type == GAME_UPDATE and self.automata.game_over == False:
          self.ai.play()

    # Actualizamos la ventana cada que ocurra un cambio

      score_value_surface = self.title_font.render(str(self.automata.score), True, Colors.white)

      self.screen.fill(Colors.dark_blue)
      self.screen.blit(self.score_surface, (365,20,50,50))
      pygame.draw.rect(self.screen, Colors.light_blue, self.score_rect, 0, 10)
      self.screen.blit(score_value_surface, score_value_surface.get_rect(centerx = self.score_rect.centerx, centery = self.score_rect.centery))
      self.screen.blit(self.next_surface, (375,180,50,50))
      pygame.draw.rect(self.screen, Colors.light_blue, self.next_rect, 0, 10)
      
      if self.automata.game_over == True:
        self.screen.blit(self.game_over_surface, (320,450,50,50))
      self.automata.draw(self.screen)

    #Mostramos la pantalla de juego
      pygame.display.update()
      self.clock.tick(60)

  