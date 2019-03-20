from CardGame.CardDeckABC import CardDeckABC
from CardGame.Card import Card

class CardDeck(CardDeckABC):
    """
    Contains deck of 52 cards

    """
    # rank and suits are ordered by its value (ascending order)
    _ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    _suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self.initialize()

    def initialize(self):
        """ Initialize 52 cards with suits and ranks) """
        cards = [Card(rank, suit) for suit in self._suits
                                    for rank in self._ranks]
        self.setAllCards(cards)

    def setAllCards(self, cards):
        """
        Set cards in the deck by given parameter cards

        Parameters
        ---------
        cards (list): list of Card objects
        """
        self._cards = cards

    def getAllCards(self):
        """
        Returns
        -------
        list
            All the cards in the deck. [Card, Card, ...]
        """
        return self._cards
