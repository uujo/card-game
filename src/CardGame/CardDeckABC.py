from abc import ABC, abstractmethod
from random import randint

class EmptyCardDeckError(LookupError):
    """
    Custom exception class inherited from built-in LookupError
    Exception indicates that there are no more cards to deal from the deck
    """

class CardDeckABC(ABC):
    """
    CardDeckABC is an abstract base class for CardDeck.
    It requires its subclass to implement shuffle() and dealOneCard() methods.
    abc.ABC syntax is added in Python 3.5
    """

    def __init__(self):
        self.setAllCards([])

    def __len__(self):
        return len(self.getAllCards())

    def __getitem__(self, index):
        return self.getAllCards()[index]

    @abstractmethod
    def setAllCards(self, cards):
        """
        Assings list of cards to the property of object.
        By convention, this method is usually called inside __init__ method.

        i.e. self._cards = cards

        Parameters
        ---------
        cards (list): list of objects
        """

    @abstractmethod
    def getAllCards(self):
        """
        Returns the property set by the setAllCards() method.

        i.e. return self._cards

        Returns
        -------
        list
            All the cards in the deck. [obj1, obj2, ...]
        """

    def shuffle(self):
        """
        Shuffles cards in the deck using Fisher–Yates shuffle (O(n) time shuffling).

        `ref: <https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm>`_
        """
        deckSize = len(self.getAllCards())
        for i in range(deckSize-1, -1, -1):
            allCards = self.getAllCards()
            # randint is inclusive:
            # randint(0, 9) selects any number between 0 to 9, including both 0 and 9
            randomIndex = randint(0, i)
            allCards[randomIndex], allCards[i] = allCards[i], allCards[randomIndex]

    def dealOneCard(self):
        """
        Deals one card from the deck.

        Returns
        -------
        Card
            randomly selected card from the deck
        """
        deckSize = len(self.getAllCards())
        if deckSize == 0:
            raise EmptyCardDeckError("No more card to deal")

        # randint is inclusive:
        # randint(0, 9) selects any number between 0 to 9, including both 0 and 9
        randomIndex = randint(0, deckSize - 1)
        return self.getAllCards().pop(randomIndex)
