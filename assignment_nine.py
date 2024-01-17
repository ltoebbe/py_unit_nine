# Liam Toebbe
# Jan 2024
# Unit 9 Final Project: A game of War

from card import Card
from deck import Deck
import random

deck = Deck(Card)
deck.shuffle_deck()
deck.print_deck()

player_hand = deck.deck_of_cards[0:26]
print('player hand is', player_hand)


dealer_hand = deck.deck_of_cards[26:52]
print('dealer hand is', dealer_hand)


# def compare_value():
#
