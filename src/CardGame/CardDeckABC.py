import abc
from random import randint

class EmptyCardDeckException(LookupError):
    """
    Custom exception class inherited from built-in LookupError
    Exeption indicates there is no more card to deal from the deck
    """

class CardDeckABC(abc.ABC):
    """
    ABC for CardDeck. It requires to implement suffle() and dealOneCard() method
    abc.ABC syntax is only works Python 3.5+

    """

    def __init__(self):
        self.setAllCards([])

    def __len__(self):
        return len(self.getAllCards())

    def __getitem__(self, index):
        return self.getAllCards()[index]

    @abc.abstractmethod
    def setAllCards(self, cards):
        """
        Assings list of cards to the poperty of object.
        By convention this method usually called inside __init__ method

        i.e. self._cards = cards

        Parameters
        ---------
        cards (list): list of objects
        """

    @abc.abstractmethod
    def getAllCards(self):
        """
        Resturns the property set by initialize function
        i.e. return self._cards

        Returns
        -------
        list
            All the cards in the deck. [obj1, obj2, ...]
        """

    def shuffle(self):
        """
        Shuffles cards in the deck using Fisher–Yates shuffle (O(n) time shuffling)
        `ref: <https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm>`_
        """
        deckSize = len(self.getAllCards())
        for i in range(deckSize-1, -1, -1):
            allCards = self.getAllCards()
            # randint is inclusive:
            # randint(0, 9) selects any number between 0 to 9 including both 0 and 9
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
            raise EmptyCardDeckException("No more card to deal")

        # randint is inclusive:
        # randint(0, 9) selects any number between 0 to 9 including both 0 and 9
        randomIndex = randint(0, deckSize - 1)
        return self.getAllCards().pop(randomIndex)
