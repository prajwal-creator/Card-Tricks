import pydealer
# from pydealer.const import BOTTOM

deck = pydealer.Deck()
sel_cards = deck.deal(3)
first_deck = deck.deal(10)
second_deck = deck.deal(15)
third_deck = deck.deal(15)
rem_deck = deck.deal(9)
#
# first_deck.add(second_deck[-1])
# sm_deck=second_deck.deal(14,end=BOTTOM)
a = deck.empty()
temp = pydealer.Deck()
temp.empty()
# temp.add(second_deck[:14])
# second_deck.empty()
# second_deck.add(temp)
# temp.add(second_deck[-4:])
i=14
while i>=0:
    temp.add(second_deck[i])
    i=i-1
print(second_deck)

