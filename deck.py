from card import Card
import random


class Deck:
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck_of_cards = []
        for suit in self.suits:
            for rank in self.ranks:
                card = {'rank': rank, 'suit': suit}
                self.deck_of_cards.append(card)


deck = Deck()
print(deck.deck_of_cards)

# deck.print_deck()
# deck.shuffle_deck()
# deck.print_deck()
#     def add_card(self, new_card):
#         self.deck_of_cards.append(new_card)
#
#     def get_card(self):
#         return self.card
#
#     def print_deck(self):
#         for card in self.deck_of_cards:
#             print(card.get_name())
#
#     def shuffle_deck(self):
#         n = len(self.deck_of_cards)
#         for i in range(n - 1, 0, -1):
#             j = random.randint(0, i)
#             self.deck_of_cards[i], self.deck_of_cards[j] = self.deck_of_cards[j], self.deck_of_cards[i]
#
#
#
# AceOfSpades = Card('Ace of Spades', 1, 4)
# TwoOfSpades = Card('Two of Spades', 2, 4)
# ThreeOfSpades = Card('Three of Spades', 3, 4)
# FourOfSpades = Card('Four of Spades', 4, 4)
# FiveOfSpades = Card('Five of Spades', 5, 4)
# SixOfSpades = Card('Six of Spades', 6, 4)
# SevenOfSpades = Card('Seven of Spades', 7, 4)
# EightOfSpades = Card('Eight of Spades', 8, 4)
# NineOfSpades = Card('Nine of Spades', 9, 4)
# TenOfSpades = Card('Ten of Spades', 10, 4)
# JackOfSpades = Card('Jack of Spades', 11, 4)
# QueenOfSpades = Card('Queen of Spades', 12, 4)
# KingOfSpades = Card('King of Spades', 13, 4)
#
# AceOfHearts = Card('Ace of Hearts', 1, 3)
# TwoOfHearts = Card('Two of Hearts', 2, 3)
# ThreeOfHearts = Card('Three of Hearts', 3, 3)
# FourOfHearts = Card('Four of Hearts', 4, 3)
# FiveOfHearts = Card('Five of Hearts', 5, 3)
# SixOfHearts = Card('Six of Hearts', 6, 3)
# SevenOfHearts = Card('Seven of Hearts', 7, 3)
# EightOfHearts = Card('Eight of Hearts', 8, 3)
# NineOfHearts = Card('Nine of Hearts', 9, 3)
# TenOfHearts = Card('Ten of Hearts', 10, 3)
# JackOfHearts = Card('Jack of Hearts', 11, 3)
# QueenOfHearts = Card('Queen of Hearts', 12, 3)
# KingOfHearts = Card('King of Hearts', 13, 3)
#
# AceOfDiamonds = Card('Ace of Diamonds', 1, 2)
# TwoOfDiamonds = Card('Two of Diamonds', 2, 2)
# ThreeOfDiamonds = Card('Three of Diamonds', 3, 2)
# FourOfDiamonds = Card('Four of Diamonds', 4, 2)
# FiveOfDiamonds = Card('Five of Diamonds', 5, 2)
# SixOfDiamonds = Card('Six of Diamonds', 6, 2)
# SevenOfDiamonds = Card('Seven of Diamonds', 7, 2)
# EightOfDiamonds = Card('Eight of Diamonds', 8, 2)
# NineOfDiamonds = Card('Nine of Diamonds', 9, 2)
# TenOfDiamonds = Card('Ten of Diamonds', 10, 2)
# JackOfDiamonds = Card('Jack of Diamonds', 11, 2)
# QueenOfDiamonds = Card('Queen of Diamonds', 12, 2)
# KingOfDiamonds = Card('King of Diamonds', 13, 2)
#
# AceOfClubs = Card('Ace of Clubs', 1, 1)
# TwoOfClubs = Card('Two of Clubs', 2, 1)
# ThreeOfClubs = Card('Three of Clubs', 3, 1)
# FourOfClubs = Card('Four of Clubs', 4, 1)
# FiveOfClubs = Card('Five of Clubs', 5, 1)
# SixOfClubs = Card('Six of Clubs', 6, 1)
# SevenOfClubs = Card('Seven of Clubs', 7, 1)
# EightOfClubs = Card('Eight of Clubs', 8, 1)
# NineOfClubs = Card('Nine of Clubs', 9, 1)
# TenOfClubs = Card('Ten of Clubs', 10, 1)
# JackOfClubs = Card('Jack of Clubs', 11, 1)
# QueenOfClubs = Card('Queen of Clubs', 12, 1)
# KingOfClubs = Card('King of Clubs', 13, 1)
#
# deck.add_card(AceOfSpades)
# deck.add_card(TwoOfSpades)
# deck.add_card(ThreeOfSpades)
# deck.add_card(FourOfSpades)
# deck.add_card(FiveOfSpades)
# deck.add_card(SixOfSpades)
# deck.add_card(SevenOfSpades)
# deck.add_card(EightOfSpades)
# deck.add_card(NineOfSpades)
# deck.add_card(TenOfSpades)
# deck.add_card(JackOfSpades)
# deck.add_card(QueenOfSpades)
# deck.add_card(KingOfSpades)
#
# deck.add_card(AceOfHearts)
# deck.add_card(TwoOfHearts)
# deck.add_card(ThreeOfHearts)
# deck.add_card(FourOfHearts)
# deck.add_card(FiveOfHearts)
# deck.add_card(SixOfHearts)
# deck.add_card(SevenOfHearts)
# deck.add_card(EightOfHearts)
# deck.add_card(NineOfHearts)
# deck.add_card(TenOfHearts)
# deck.add_card(JackOfHearts)
# deck.add_card(QueenOfHearts)
# deck.add_card(KingOfHearts)
#
# deck.add_card(AceOfDiamonds)
# deck.add_card(TwoOfDiamonds)
# deck.add_card(ThreeOfDiamonds)
# deck.add_card(FourOfDiamonds)
# deck.add_card(FiveOfDiamonds)
# deck.add_card(SixOfDiamonds)
# deck.add_card(SevenOfDiamonds)
# deck.add_card(EightOfDiamonds)
# deck.add_card(NineOfDiamonds)
# deck.add_card(TenOfDiamonds)
# deck.add_card(JackOfDiamonds)
# deck.add_card(QueenOfDiamonds)
# deck.add_card(KingOfDiamonds)
#
# deck.add_card(AceOfClubs)
# deck.add_card(TwoOfClubs)
# deck.add_card(ThreeOfClubs)
# deck.add_card(FourOfClubs)
# deck.add_card(FiveOfClubs)
# deck.add_card(SixOfClubs)
# deck.add_card(SevenOfClubs)
# deck.add_card(EightOfClubs)
# deck.add_card(NineOfClubs)
# deck.add_card(TenOfClubs)
# deck.add_card(JackOfClubs)
# deck.add_card(QueenOfClubs)
# deck.add_card(KingOfClubs)
