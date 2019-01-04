import random

deck = [x for x in range (0, 52)]
random.shuffle(deck)

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

for card in deck:
    rank = ranks[ card % 13]
    suit = suits[ card // 13]
    print("{} of {}".format(rank, suit))

# random card generation
randomCard = random.randint(0, 51)
randomRank = ranks[ randomCard % 13 ]
randomSuit = suits[ randomCard // 13]
print("Random card = {} of {}".format(randomRank, randomSuit))

for i in range (0, 26):
    