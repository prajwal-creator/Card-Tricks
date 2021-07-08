import pydealer
from pydealer.const import BOTTOM
import sys
import pygame
from settings import Settings
from CardSet import CardSet
import time

deck = pydealer.Deck()
deck.shuffle()
sel_cards = deck.deal(3)
first_deck = deck.deal(10)
second_deck = deck.deal(15)
third_deck=deck.deal(15)
rem_deck = deck.deal(9)
temp = pydealer.Deck()
temp.empty()
white = (255, 255, 255)
pygame.init()
font1 = pygame.font.Font('Fonts/Walkway_SemiBold.ttf', 32)
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

class CardGame:
    deck = pydealer.Deck()
    deck.shuffle()
    sel_cards = deck.deal(3)
    first_deck = deck.deal(10)
    second_deck = deck.deal(15)
    third_deck = deck.deal(15)
    rem_deck = deck.deal(9)
    comb_deck=pydealer.Deck()
    comb_deck.empty()
    up_deck = pydealer.Deck()
    up_deck.empty()
    down_deck = pydealer.Deck()
    down_deck.empty()
    comb_deck1 = pydealer.Deck()
    comb_deck1.empty()
    n=1
    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Upside Down Trick")
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
                elif event.key == pygame.K_KP_ENTER:
                    self.x = 80
                    self.i=0
                    self._update_screen()
                    self._update_screen_1(self.first_deck)
                    self._update_screen_1(self.second_deck)
                    self._update_screen_1(self.third_deck)
                    self._update_screen_1(self.rem_deck)
                    self.x=80
                    txt = font1.render("click ctrl key to Continue", True, (255, 255, 0))
                    self.screen.blit(txt, (480, 650))
                    pygame.display.flip()

                elif event.key == pygame.K_RCTRL:
                    self.screen.fill(self.settings.bg_color, pygame.Rect(self.x, 60, 100, 155))
                    pygame.display.flip()
                    if self.i == 0:
                        self.k = 15
                        self.first_deck.add(sel_cards[self.i])
                        self.refresh_deck(self.first_deck,self.x,250)
                    elif self.i == 1:
                        self.l = 15
                        self.second_deck.add(sel_cards[self.i])
                        self.refresh_deck(self.second_deck,self.x,250)
                    elif self.i == 2:
                        self.third_deck.add(sel_cards[self.i])
                        self.refresh_deck(self.third_deck,self.x,250)
                    elif self.i == 3:
                        self.x = 80
                        self.comb_deck.add(self.first_deck)
                        self.print_right(self.comb_deck)
                    elif self.i == 4:
                        self.comb_deck.add(self.second_deck)
                        self.print_right(self.comb_deck)
                    elif self.i == 5:
                        self.comb_deck.add(self.third_deck)
                        self.print_right(self.comb_deck)

                    elif self.i == 6:
                        self.update_deck1(self.i)
                        temp.add(self.comb_deck[:48])
                        self.print_right(temp)
                        self.comb_deck1.add(temp)
                        temp.empty()

                    elif self.i == 7:
                        self.update_deck1(self.i)
                        temp.add(self.comb_deck[:48])
                        self.print_right(self.comb_deck1)
                        temp.empty()

                    elif self.i == 8:
                        self.update_deck1(self.i)

                    elif self.i == 9:
                        self.update_deck1(self.i)

                    elif self.i == 10:
                        self.update_deck1(self.i)

                    elif self.i == 11:
                        self.update_deck1(self.i)

                    elif self.i == 12:
                        self.update_deck1(self.i)

                    elif self.i == 13:
                        self.update_deck1(self.i)
                    
                    self.printonscreen(self.i)
                    self.i = self.i+1
                    if self.x < 600:
                        self.x = self.x+140

                elif event.key == pygame.K_LEFT and self.i:
                    self.update_deck(self.i)
    def printonscreen(self,m):
        if m == 0 or m == 1 or m == 2:
            self.screen.fill(self.settings.bg_color, pygame.Rect(480, 650, 650, 100))
            txt = font1.render("click left key to shift the Cards", True, (255, 255, 0))
            txta = font1.render("and Ctrl key to form the decks", True, (255, 255, 0))
            self.screen.blit(txt, (480, 650))
            self.screen.blit(txta, (520, 700))
            pygame.display.flip()
        # if m == 3 or m == 4 or m == 5:
        #     self.screen.fill(self.settings.bg_color, pygame.Rect(480, 650, 650, 100))
        #     txt = font1.render("click Ctrl key to move the cards and to arrange into a single deck", True, (255, 255, 0))
        #     self.screen.blit(txt, (380, 650))
        #     pygame.display.flip()

    def print_right(self,cardslist):
        if self.x<500:
            self.screen.fill(self.settings.bg_color, pygame.Rect(self.x, 250, 100, 600))
            pygame.display.flip()
        self.screen.fill(self.settings.bg_color, pygame.Rect(950, 20, 100, 680))
        pygame.display.flip()
        for var in range(len(cardslist)):
            r, c = Index_Card_Image(3, 5)
            self.CardSet.cards[r * 13 + c].blitmehere(950, 20+var * 10)
            pygame.display.flip()

    def update_deck(self,d):
        if d==1:
            self.first_deck.add(self.second_deck[self.k-1])
            temp.add(self.second_deck[:self.k-1])
            self.second_deck.empty()
            self.second_deck.add(temp)
            temp.empty()
            self.refresh_deck(self.second_deck,220,250)
            self.refresh_deck(self.first_deck,80,250)
            self.k = self.k-1

        if d == 2:
            self.second_deck.add(self.third_deck[self.l - 1])
            temp.add(self.third_deck[:self.l-1])
            self.third_deck.empty()
            self.third_deck.add(temp)
            temp.empty()
            self.refresh_deck(self.third_deck, 360,250)
            self.refresh_deck(self.second_deck, 220,250)
            self.l = self.l - 1


        if d == 3 and self.n == 1:
            self.screen.fill(self.settings.bg_color, pygame.Rect(1000, 250, 200, 600))
            self.third_deck.add(self.rem_deck)
            self.refresh_deck(self.third_deck, 360,250)
            self.n = self.n+1

    def update_deck1(self, d):
        if d == 6:
            temp.add(self.comb_deck[-4:])
            self.comb_deck1.add(temp)
            self.refresh_deck(self.comb_deck1, 820, 250)
            temp.empty()

        if d == 7:
            self.screen.fill(self.settings.bg_color, pygame.Rect(820, 250, 100, 200))
            pygame.display.flip()

        if d == 8:
            z = 51
            while z >= 0:
                if z % 2 == 1:
                    self.up_deck.add(self.comb_deck1[z])
                else:
                    self.down_deck.add(self.comb_deck1[z])
                z = z-1

            self.screen.fill(self.settings.bg_color, pygame.Rect(950, 20, 100, 800))
            self.refresh_deck(self.up_deck,100,100)
            self.refresh_deck(self.down_deck,240,100)


        if d == 9:
            z = 25
            self.up_deck.empty()
            i = 0
            while i <= 25:
                temp.add(self.down_deck[i])
                i = i + 1
            self.down_deck.empty()

            while z >= 0:
                if z % 2 == 1:
                    self.up_deck.add(temp[z])
                else:
                    self.down_deck.add(temp[z])
                z = z - 1

            temp.empty()
            self.screen.fill(self.settings.bg_color, pygame.Rect(240, 100, 100, 600))
            self.refresh_deck(self.up_deck, 240, 100)
            self.refresh_deck(self.down_deck, 380, 100)

        if d == 10:
            z = 12
            self.up_deck.empty()
            i = 0

            while i <= 12:
                temp.add(self.down_deck[i])
                i = i + 1
            self.down_deck.empty()
            while z >= 0:
                if z % 2 == 1:
                    self.down_deck.add(temp[z])
                else:
                    self.up_deck.add(temp[z])
                z = z - 1
            print(self.down_deck)
            temp.empty()
            self.screen.fill(self.settings.bg_color, pygame.Rect(380, 100, 100, 400))
            self.refresh_deck(self.up_deck, 380, 100)
            self.refresh_deck(self.down_deck, 520, 100)

        if d == 11:
            z = 5
            self.up_deck.empty()
            i = 0
            while i <= 5:
                temp.add(self.down_deck[i])
                i = i + 1
            self.down_deck.empty()

            while z >= 0:
                if z % 2 == 1:
                    self.up_deck.add(temp[z])
                else:
                    self.down_deck.add(temp[z])
                z = z - 1
            temp.empty()
            self.screen.fill(self.settings.bg_color, pygame.Rect(520, 100, 100, 400))
            self.refresh_deck(self.up_deck, 520, 100)
            self.refresh_deck(self.down_deck, 660, 100)

        if d == 12:
            self.up_deck.empty()
            self.up_deck.add(self.down_deck)
            self.down_deck.empty()
            self.screen.fill(self.settings.bg_color, pygame.Rect(660, 100, 100, 400))
            self.refresh_deck(self.up_deck, 660, 100)

        if d == 13:
            self.screen.fill(self.settings.bg_color, pygame.Rect(660, 100, 100, 400))
            for var in range(3):
                x = str(self.up_deck[var])
                x = x.split(" ")
                r, c = Index_Card_Image(x[0], x[2])
                self.CardSet.cards[r * 13 + c].blitmehere(660+140*var,350)
                pygame.display.flip()
                time.sleep(0.1)

    def refresh_deck(self,cardslist,m,n):
        self.screen.fill(self.settings.bg_color, pygame.Rect(m, n, 100, 400))
        pygame.display.flip()
        for var in range(len(cardslist)):
            if cardslist == self.up_deck:
                x = str(cardslist[var])
                x = x.split(" ")
                r, c = Index_Card_Image(x[0], x[2])
                self.CardSet.cards[r * 13 + c].blitmehere(m, n + var * 15)
                pygame.display.flip()
            else:
                r, c = Index_Card_Image(3, 5)
                self.CardSet.cards[r * 13 + c].blitmehere(m, n + var * 15)
                pygame.display.flip()

    # def display_card(self,card,j):
    #     x = str(card)
    #     x = x.split(" ")
    #     r, c = Index_Card_Image(x[0], x[2])
    #     self.CardSet.cards[r * 13 + c].blitmehere(self.x,j*15)
    #     pygame.display.flip()
    #     time.sleep(0.5)
    #
    #     r, c = Index_Card_Image(3, 5)
    #     self.CardSet.cards[r * 13 + c].blitmehere(self.x,j*15)
    #     pygame.display.flip()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for var in range(3):
            x = str(sel_cards[var])
            x = x.split(" ")
            r, c = Index_Card_Image(x[0], x[2])
            self.CardSet.cards[r * 13 + c].blitme(-0.8, var)
            pygame.display.flip()
            time.sleep(0.1)

    def _update_screen_1(self,cardslist):
        for var in range(len(cardslist)):
            x = str(cardslist[var])
            x = x.split(" ")
            r, c = Index_Card_Image(x[0], x[2])
            if cardslist == self.rem_deck:
                self.CardSet.cards[r * 13 + c].blitmehere(self.x+550, 250 + var * 15)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(self.x, 250 + var*15)
            pygame.display.flip()
            time.sleep(0.1)

        for var in range(len(cardslist)):
            r, c = Index_Card_Image(3, 5)
            if cardslist == self.rem_deck:
                self.CardSet.cards[r * 13 + c].blitmehere(self.x+550, 250 + var * 15)
            else:
                self.CardSet.cards[r * 13 + c].blitmehere(self.x, 250 + var*15)

            pygame.display.flip()
        self.x = self.x + 140

CardDisplay = CardGame()
CardDisplay.run_game()