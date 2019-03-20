from random import randint
from CardGame.Card import Card

class NoCardException(Exception):
    pass

class CardDeck:
    """
    Contains deck of 52 cards

    """
    # rank and suits are ordered by its value
    _ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    _suits = ['hearts', 'spades', 'clubs', 'diamonds']

    def __init__(self):
        self.initialize()

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    #def __contains__(self, card):
    #    return (card in self._cards)

    def initialize(self):
        """ Initialize 52 cards with suits and ranks) """
        self._cards = [Card(rank, suit) for suit in self._suits
                                        for rank in self._ranks]
    def getRemainingCards(self):
        """
        Returns
        -------
        list
            All the cards in the deck. [Card, Card, ...]
        """
        return self._cards

    def shuffle(self):
        """
        Shuffles cards in the deck using Fisher–Yates shuffle (O(n) time shuffling)
        `ref: <https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm>`_
        """
        deckSize = len(self._cards)
        for i in range(deckSize - 1, -1, -1):
            randomIndex = randint(0, i)
            self._cards[randomIndex], self._cards[i] = self._cards[i], self._cards[randomIndex]

    def dealOneCard(self):
        """
        Deals one card from the deck.

        Returns
        -------
        Card
            randomly selected card from the deck
        """
        deckSize = len(self._cards)
        if deckSize == 0:
            raise NoCardException("No more card to deal")

        randomIndex = randint(0, deckSize - 1)
        return self._cards.pop(randomIndex)
