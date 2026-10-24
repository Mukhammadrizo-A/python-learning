import random
from random import choice

# heads and tails
coin = choice(["heads", "tails"])
print(coin)

# cards
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)