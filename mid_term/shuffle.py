#! /usr/bin/env python3

import pprint
import random
from typing import List

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

card_names = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 'Jack',
    12: 'Queen',
    13: 'King',
    14: 'Ace'
}


def make_suit(suit: str) -> List[str]:
    '''
    Generates a list containing all of the cards in a single suit

    Args:
        suit (str): the suit for which to generate the cards

    Returns:
        List[str]: a list containing all the cards in the suit.
                   each card is a string with the card value
                   followed by the suit in the format:

                   $Value of $Suit

                   Examples:

                        4 of Hearts
                        8 of Diamonds
                        10 of Clubs
                        Queen of Hearts
                        Ace of Spades
    '''
    suit_cards = []

    for value in range(2, 15):

        card = "{} of {}".format(card_names[value], suit)
        suit_cards.append(card)

    return suit_cards


def make_deck() -> List[str]:
    '''
    Generates a list containing a string for each of the cards in a standard
    playing deck

    A "standard" deck of playing cards consists of 52 Cards in each of the 4
    suits of Spades, Hearts, Diamonds, and Clubs. Each suit contains 13 cards:
    Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King

    Returns:
        List[str]: List containing string for each of the cards in a standard
                   deck. See make_suit() for string format
    '''
    deck: List[str] = []

    for suit in suits:
        deck += make_suit(suit)

    return deck


def shuffle_deck(deck):
    '''
    Shuffles deck of cards in place, i.e. modifies the passed deck parameter
    but doesn't return a new value

    Args:
        deck (List[str]): List containing strings, each representing cards in a
                        standard deck
    '''
    random.shuffle(deck)


def deal(num_of_players: int, cards_per_player: int, deck: List[str]) -> List[List[str]]:
    '''
    Creates a nested list of hands for the requested number of players.
    Each hand is a list holding the requested number of cards.

    After dealing the deck will no longer include the cards that have been
    dealt to the players.

    Args:
        num_of_players (int): Number of players in the game,
                              ie the number of hands to create

        cards_per_player (int): The number of cards each player should receive

        deck (List[str]): the deck of cards from which to deal out hands

    Returns:
        List[List[str]]: a nested list of cards.  One list for each player,
                         with each list containing the number of requested
                         cards
    '''
    hands: List[List[str]] = []

    for hand in range(num_of_players):

        cards_start = hand * cards_per_player
        cards_end = cards_start + cards_per_player
        hands.append(deck[cards_start:cards_end])

    del deck[0:(num_of_players * cards_per_player)]

    return hands


def main():
    deck = make_deck()

    print('\nDeck:')
    pprint.pprint(deck)

    shuffle_deck(deck)

    hands = deal(4, 5, deck)

    print('\nHands:')
    pprint.pprint(hands)

    print('\nDeck after Dealing Cards:')
    pprint.pprint(deck)


if __name__ == '__main__':
    main()
