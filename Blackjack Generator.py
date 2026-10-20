import random
import pandas as pd

## number of decks used
size = 8

## number of players going against the dealer
player_count = 1

## at what score does the dealer stop hitting
dealer_limit = 17

## score players will hit up to
hit_limit = 10

## data points desired per hit limit
points = 50000
shoe_id = 0
hand_count = int(points/player_count)
data = []
base_deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
shoe = []
hand_id = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.lost = False
        self.win = "Won"
        self.blackjack = False

    def hit(self):
        if not self.lost:
            x = random.choice(shoe)
            shoe.remove(x)
            self.hand.append(x)
            self.tally()
        else:
            return

    def tally(self):
        total = sum(self.hand)

        while total > 21 and 11 in self.hand:
            self.hand[self.hand.index(11)] = 1
            total = sum(self.hand)

        if total > 21:
            self.lost = True
        return total



def build_shoe():
    global shoe
    global shoe_id
    shoe_id += 1
    shoe = []
    for _ in range(size*4):
        for i in base_deck:
            shoe.append(i)
    return


def play_hand():
    global hand_id
    hand_id += 1
    players = []
    dealer = None
    for i in range(1, player_count + 1):
        players.append(Player(i))

    for p in players:
        p.hit()
        p.hit()
        if p.tally() == 21:
            p.blackjack = True
        if not p.lost:
            while p.tally() < hit_limit:
                p.hit()

    dealer = Player("Dealer")
    dealer.hit()
    dealer.hit()
    if dealer.tally() == 21:
        dealer.blackjack = True
    while dealer.tally() < dealer_limit:
        dealer.hit()
        if dealer.lost:
            pass
        else:
            for p in players:
                if dealer.tally() > p.tally():
                    p.lost = True

    for p in players:
        if p.lost:
            p.win = "Lost"

        if p.tally() > dealer.tally() and not p.lost:
            pass
        elif p.tally() == dealer.tally() and not p.lost:
            p.win = "Tie"
        elif p.tally() < dealer.tally() and not dealer.lost:
            p.win = "Lost"

        if p.blackjack and dealer.blackjack:
            p.win = "Tie"
        elif p.blackjack and dealer.tally() == 21:
            p.win = "Won"
        elif dealer.blackjack and p.tally() == 21:
            p.win = "Lost"

        data.append({
            "hand_id": hand_id,
            "Shoe ID": shoe_id,
            "player": p.name,
            "Hand": ",".join(map(str, p.hand)),
            "Score": p.tally(),
            "Dealer": dealer.tally(),
            "Count": len(p.hand),
            "Won": p.win,
            "Showing": dealer.hand[1],
            "BJ": p.blackjack,
            "Hit limit": hit_limit,
        })

def main():
    global hand_id
    build_shoe()
    for _ in range(hand_count):
        play_hand()
        if len(shoe) < size*26:
            build_shoe()


def multi():
    global hit_limit
    while hit_limit <= 21:
        main()
        hit_limit += 1
    df = pd.DataFrame(data)
    df.to_csv('BlackjackSimData.csv', index=False)
multi()
