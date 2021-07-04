import pydealer
from pydealer.const import BOTTOM
import sys
import pygame
from settings import Settings
from CardSet import CardSet
import time


# Deck of 52 Cards
decka = pydealer.Deck()
deckb = pydealer.Deck()
# get the cards in two different stacks
l_cards = decka.get_list([32,36,40,44,48])
r_cards = deckb.get_list([33,37,41,45,49])
rr_cards = r_cards[::-1]

#r_cards = r_cards[::-1]


# Flag Variables for graphics events
Arrange_cards_flag = False

pygame.init()
# Font for text
font1 = pygame.font.Font('Fonts/Walkway_SemiBold.ttf', 32)
font2 = pygame.font.Font('Fonts/Sansation-Bold.ttf', 40)
font3 = pygame.font.Font('Fonts/Walkway_Oblique_Black.ttf', 20)


def initialize_deck():
    print("List of all 10 Cards are:")
    print(l_cards)
    print(r_cards)

# Arrange Cards row-wise



def Index_Card_Image(value,suit):
    column = -1
    row = -1

    if suit == "Clubs":
        row = 0
    elif suit == "Diamonds":
        row = 1
    elif suit == "Hearts":
        row = 2
    elif suit == "Spades":
        row = 3
    else:
        row = -1

    if value == "Ace":
        column = 0
    elif value == "Jack":
        column = 10
    elif value == "Queen":
        column = 11
    elif value == "King":
        column = 12
    else:
        column = int(value) - 1

    return row, column

def rotate(l, y):
    if len(l) == 0:
        return l
    y = y % len(l)
    return l[y:] + l[:y]

class CardGame:
    """Overall class to manage Card Display."""
    l=-6
    step = 0
    counter = -1
    ctrl = False
    name = "MERA BHARATH MAHAN JAIHIND"
    x = 200
    c=0
    y=200
    n=500

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Mera Bharath Mahan Trick")
        self.CardSet = CardSet(self)

    def run_game(self):
        """Start the main loop for the game."""
        self.screen.fill(self.settings.bg_color)

        while True:
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

                # When pressed Enter, the card display starts
                elif event.key == pygame.K_KP_ENTER:
                    self._update_screen()
                    txt = font1.render("Have chosen some 10 Cards", True, (255, 255, 0))
                    self.screen.blit(txt, (350,600))
                    pygame.display.flip()
                    txt = font1.render("click ctrl key to Continue", True, (255, 255, 0))
                    self.screen.blit(txt, (480, 650))
                    pygame.display.flip()

                elif event.key == pygame.K_RCTRL:
                    self.screen.fill(self.settings.bg_color)
                    self._update_screen_2(l_cards)
                    self._update_screen_2(rr_cards)
                    self.ctrl = True
                    for i in range(len(self.name)):
                        txt = font2.render(self.name[self.c], True, (255, 255, 0))
                        self.screen.blit(txt, (self.y, 40))
                        self.y = self.y + 30
                        self.c=self.c+1
                        pygame.display.flip()
                    txt = font1.render("Press Left and Right keys to shift the cards", True, (255, 255, 0))
                    self.screen.blit(txt, (300, 670))
                    pygame.display.flip()
                    txt = font1.render("and space key to remove the Top cards", True, (255, 255, 0))
                    self.screen.blit(txt, (320, 720))
                    pygame.display.flip()


                elif event.key == pygame.K_LEFT and self.ctrl == True:
                    try:
                        n_cards = rotate(l_cards,1)
                        l_cards.clear()
                        for i in range(len(n_cards)):
                            l_cards.append(n_cards[i])
                        self._update_screen_1(l_cards)
                        self.traverse(n_cards[-1], l_cards)
                        self._update_screen_2(l_cards)
                        self.printscreen()
                        self.screen.fill(self.settings.bg_color, pygame.Rect(300, 670, 650, 100))
                        txt = font1.render("You have clicked Left Key", True, (255, 255, 0))
                        self.screen.blit(txt, (380, 700))
                        pygame.display.flip()
                    except:
                        print("Index out of range")

                elif event.key == pygame.K_RIGHT and self.ctrl == True:
                    try:
                        n_cards = rotate(rr_cards, 1)
                        rr_cards.clear()
                        for i in range(len(n_cards)):
                            rr_cards.append(n_cards[i])
                        self._update_screen_1(rr_cards)
                        self.traverse(n_cards[-1], rr_cards)
                        self._update_screen_2(rr_cards)
                        self.printscreen()
                        self.screen.fill(self.settings.bg_color, pygame.Rect(300, 670, 650, 100))
                        txt = font1.render("You have clicked Right Key", True, (255, 255, 0))
                        self.screen.blit(txt, (380, 700))
                        pygame.display.flip()
                    except:
                        print("Index out of range")

                elif event.key == pygame.K_SPACE and self.ctrl == True:
                    self.l+=8
                    self.screen.fill(self.settings.bg_color,pygame.Rect(450, 100, 250, 600))
                    try:
                        a,*lm_cards = l_cards
                        b,*rm_cards = rr_cards
                        l_cards.clear()
                        for i in range(len(lm_cards)):
                            l_cards.append(lm_cards[i])
                        rr_cards.clear()
                        for i in range(len(rm_cards)):
                            rr_cards.append(rm_cards[i])
                        for i in range(self.l):
                            self._update_screen_3(a,1,self.l)
                            self._update_screen_3(b,4,self.l)
                        self._update_screen_2(l_cards)
                        self._update_screen_2(rr_cards)
                        self.n = self.n - 80
                        self.printscreen()
                        self.screen.fill(self.settings.bg_color, pygame.Rect(300, 670, 650, 100))
                        txt = font1.render("You have clicked Tab Key", True, (255, 255, 0))
                        self.screen.blit(txt, (380, 700))
                        pygame.display.flip()
                    except:
                        print("NO cards left")


    def traverse(self,a,n_cards):
        x=str(a)
        x=x.split(" ")
        r,c = Index_Card_Image(x[0],x[2])
        # r, c = Index_Card_Image(3,5)
        y_change=1
        if n_cards == l_cards:
            x_pos=340
            y_pos=100

            while y_pos <= self.n:
                self.screen.fill(self.settings.bg_color, pygame.Rect(340, 100, 100, 560))
                self.CardSet.cards[r*13+c].blitmehere2(x_pos,y_pos)
                pygame.display.flip()
                y_pos = y_pos+y_change
                time.sleep(0.001)
            self.screen.fill(self.settings.bg_color, pygame.Rect(340, 100, 100, 560))
            pygame.display.flip()
            self.CardSet.cards[r * 13 + c].blitmehere2(450,self.n)
            pygame.display.flip()

        if n_cards == rr_cards:
            self.CardSet.cards[r * 13 + c].blitmehere2(710, 100)
            x_pos = 710
            y_pos = 100
            while y_pos <= self.n:
                self.screen.fill(self.settings.bg_color, pygame.Rect(710, 100, 100, 560))
                self.CardSet.cards[r * 13 + c].blitmehere2(x_pos, y_pos)
                pygame.display.flip()
                y_pos = y_pos + y_change
                time.sleep(0.001)
            self.screen.fill(self.settings.bg_color, pygame.Rect(710, 100, 100, 560))
            pygame.display.flip()
            self.CardSet.cards[r * 13 + c].blitmehere2(600, self.n)
            pygame.display.flip()


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for var in range(5):
            # left cards

            x = str(l_cards[var])
            x = x.split(" ")
            r,c = Index_Card_Image(x[0],x[2])
            self.CardSet.cards[r * 13 + c].blitme(1, var)
            pygame.display.flip()
            time.sleep(0.1)

        for var in range(5):
            # right cards
            x = str(r_cards[var])
            x = x.split(" ")
            r, c = Index_Card_Image(x[0], x[2])
            self.CardSet.cards[r * 13 + c].blitme(6,1+var)
            pygame.display.flip()
            time.sleep(0.1)

    def _update_screen_1(self, n_cards):
        # rotation
        if n_cards == l_cards:
            self.screen.fill(self.settings.bg_color, pygame.Rect(450, 100, 100, 560))
        elif n_cards == rr_cards:
            self.screen.fill(self.settings.bg_color, pygame.Rect(600, 100, 100, 560))

        # for var in range(len(n_cards)-1):
        #     r, c = Index_Card_Image(3, 5)
        #     if n_cards == l_cards:
        #         self.CardSet.cards[r * 13 + c].blitmehere(450,100+ var * 80)
        #         time.sleep(0.1)
        #     elif n_cards == rr_cards:
        #         self.CardSet.cards[r * 13 + c].blitmehere(600,100+ var * 80)
        #         time.sleep(0.1)
        #     pygame.display.flip()

        for var in range(len(n_cards) - 1):
            x = str(n_cards[var])
            x = x.split(" ")
            r, c = Index_Card_Image(x[0], x[2])
            if n_cards == l_cards:
                self.CardSet.cards[r * 13 + c].blitmehere(450,100+ var * 80 + 80)
                time.sleep(0.1)
            elif n_cards == rr_cards:
                self.CardSet.cards[r * 13 + c].blitmehere(600,100+ var * 80 + 80)
                time.sleep(0.1)
            pygame.display.flip()

    def _update_screen_2(self, n_cards):
        # rotation
        if n_cards == l_cards:
            self.screen.fill(self.settings.bg_color, pygame.Rect(450, 100, 100, 560))
        elif n_cards == rr_cards:
            self.screen.fill(self.settings.bg_color, pygame.Rect(600, 100, 100, 560))

        # for var in range(len(n_cards)):
        #     r, c = Index_Card_Image(3, 5)
        #     if n_cards == l_cards:
        #         self.CardSet.cards[r * 13 + c].blitmehere(450,100+ var * 80)
        #         time.sleep(0.1)
        #     elif n_cards == rr_cards:
        #         self.CardSet.cards[r * 13 + c].blitmehere(600,100+ var * 80)
        #         time.sleep(0.1)
        #     pygame.display.flip()

        for var in range(len(n_cards)):
            x = str(n_cards[var])
            x = x.split(" ")
            r, c = Index_Card_Image(x[0], x[2])
            if n_cards == l_cards:
                self.CardSet.cards[r * 13 + c].blitmehere(450,100+ var * 80)
                time.sleep(0.1)
            elif n_cards == rr_cards:
                self.CardSet.cards[r * 13 + c].blitmehere(600,100+ var * 80)
                time.sleep(0.1)
            pygame.display.flip()
      


    def _update_screen_3(self,var,i,l):
        # first pos
        x = str(var)
        x = x.split(" ")
        r, c = Index_Card_Image(x[0], x[2])
        self.CardSet.cards[r * 13 + c].blitme(0.2*l,0.2*i)
        pygame.display.flip()
        time.sleep(0.01)

    def printscreen(self):
        self.counter = self.counter + 1
        txt = font2.render(self.name[self.counter], True, (255, 0, 0))
        self.screen.blit(txt, (self.x, 40))
        self.x = self.x + 30
        pygame.display.flip()



CardDisplay = CardGame()
initialize_deck()
CardDisplay.run_game()



