import pygame, sys, random
from pygame.locals import *
from win_checker import win_checker
pygame.init()

class Feld:
    def __init__(self, position):
        self.x_koordinate = 100+(position-1)%3*100+20
        print("X-Koordinate: "+str(self.x_koordinate))
        self.y_koordinate = 100 + (position-1)//3*100+20
        print("Y-Koordinate: "+str(self.y_koordinate))
        self.rect = pygame.Rect(self.x_koordinate - 20, self.y_koordinate - 20, 100, 100)
    geklickt = False
    spieler_der_klickte = None
    def klicken(self, spieler):
        if self.geklickt == True:
            return False
        if spieler == 0: # blau ist 0, rot ist 1
            pygame.draw.line(screen, BLAU, (self.x_koordinate, self.y_koordinate), (self.x_koordinate+60, self.y_koordinate+60), 3)
            pygame.draw.line(screen, BLAU, (self.x_koordinate, self.y_koordinate+60), (self.x_koordinate+60, self.y_koordinate), 3)
        else:
            center = (self.x_koordinate + 30, self.y_koordinate + 30)
            pygame.draw.circle(screen, ROT, center, 40, 3)
        self.geklickt = True
        self.spieler_der_klickte = spieler
        return True

def checken(mausposition):
    global an_der_reihe, geklickte_felder
    for i in range(1,10):
        if feld[i].rect.collidepoint(mausposition):
            if not feld[i].geklickt:
                feld[i].klicken(an_der_reihe)
                if an_der_reihe == 0: # blau
                    an_der_reihe = 1
                    spieler_rot()
                else:
                    an_der_reihe = 0
                    spieler_blau()
                geklickte_felder.append(feld[i].spieler_der_klickte)
                print(geklickte_felder)
                # gucken, ob wer gewonnen hat
                if len(geklickte_felder) >= 5:
                    win_checker(feld,"rot")
                    win_checker(feld,"blau")
                

def spieler_blau():
    pygame.draw.rect(screen, WEISS, (50, 50, 420, 50))
    font = pygame.font.SysFont(None,45)
    text = font.render('Spieler Blau ist an der Reihe.', False, BLAU)
    screen.blit(text,(50,50))

def spieler_rot():
    pygame.draw.rect(screen, WEISS, (50, 50, 440, 50))
    font = pygame.font.SysFont(None,45)
    text = font.render('Spieler Rot ist an der Reihe.', False, ROT)
    screen.blit(text,(50,50))
    
# Colours
BACKGROUND = (255, 255, 255)
BLAU = (61, 225, 237)
ROT = (237, 93, 61)
BLACK = (0, 0, 0)
WEISS = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Zecke, Reißzwecke, Zeh')
logo = pygame.image.load('mittwochsfrosch.jpg')
pygame.display.set_icon(logo)

rechteck_feld_mitte = pygame.Rect(200, 200, 100, 100)
screen.fill(BACKGROUND)
pygame.draw.line(screen, BLACK, (100, 100), (100, 400), 3)
pygame.draw.line(screen, BLACK, (100, 100), (400, 100), 3)
pygame.draw.line(screen, BLACK, (400, 100), (400, 400), 3)
pygame.draw.line(screen, BLACK, (100, 400), (400, 400), 3)
pygame.draw.line(screen, BLACK, (100, 200), (400, 200), 3)
pygame.draw.line(screen, BLACK, (100, 300), (400, 300), 3)
pygame.draw.line(screen, BLACK, (200, 100), (200, 400), 3)
pygame.draw.line(screen, BLACK, (300, 100), (300, 400), 3)

# feld[1-9] mit Objekten der Klasse Feld belegen
feld = []
feld.append(None)
for i in range(1,10):
    feld.append(Feld(i))
an_der_reihe = 0
geklickte_felder = []

# The main function that controls the game
def main () :
    looping = True

    # The main game loop
    while looping :
        # Get inputs
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                checken(event.pos)
                
        
        # Processing
        # This section will be built out later
     
        pygame.display.update()
        fpsClock.tick(FPS)
     
main()
