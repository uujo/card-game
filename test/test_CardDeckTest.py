import unittest

from CardGame.Card import Card
from CardGame.CardDeckABC import EmptyCardDeckError
from CardGame.CardDeck import CardDeck


class TestCardDeck(unittest.TestCase):

    def test_suffle(self):
        """
        Test the minial randomness of shuffled deckself but not true randomness.
        """
        ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        allCards = [Card(rank, suit) for suit in suits
                                     for rank in ranks]

        # Check whether cards in the deck is initialize collectly.
        cardDeck = CardDeck()
        allCardsFromDeck = cardDeck.getAllCards()
        self.assertCountEqual(allCards, allCardsFromDeck)
        self.assertEqual(allCards, allCardsFromDeck)

        # Check the randomness When the cards get shuffled.
        # The total possible cases are the factorial of 52 - 52!, 8.06e+67
        #
        # The probability of getting the same initial order of cards from 5000 samples
        # will be close to 0% from any of the shuffled decks.

        for i in range(5000):
            cardDeck.shuffle()
            allCardsFromDeck = cardDeck.getAllCards()
            self.assertCountEqual(allCards, allCardsFromDeck)
            self.assertNotEqual(allCards, allCardsFromDeck)

    def test_dealOneCard(self):
        """
        Tests the CardDeck's dealOneCard() and initialize() methods.
        Randomness of dealOneCard() is not tested.
        """
        cardDeck = CardDeck()
        self.assertEqual(52, len(cardDeck))

        card = cardDeck.dealOneCard()
        self.assertEqual(51, len(cardDeck))
        self.assertIsInstance(card, Card)

        # Dealing all the remaining cards
        for i in range(51):
            cardDeck.dealOneCard()

        self.assertEqual(0, len(cardDeck))

        with self.assertRaises(EmptyCardDeckError) as cm:
            cardDeck.dealOneCard()

        self.assertEqual("No more card to deal", str(cm.exception))

        # Test initialize() method
        cardDeck.initialize()
        self.assertEqual(52, len(cardDeck))


if __name__ == "__main__":
    unittest.main()
