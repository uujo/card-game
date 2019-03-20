import unittest
from CardGame.Card import Card
from CardGame.CardDeck import CardDeck, NoCardException

class TestCardDeck(unittest.TestCase):

    def test_suffle(self):
        """
        Test the minial randomness of shuffled deckself but not true randomness.
        """
        ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['hearts', 'spades', 'clubs', 'diamonds']
        allCards = [Card(rank, suit) for suit in suits
                                     for rank in ranks]

        # check whether cards in the deck is initialize collectly
        cardDeck = CardDeck()
        allCardsFromDeck = cardDeck.getRemainingCards()
        self.assertCountEqual(allCards, allCardsFromDeck)
        self.assertEqual(allCards, allCardsFromDeck)

        # check the randomness When the cards gets shuffled,
        # there will be factorial of 52 - 52!, 8.06e+67
        # when there will be close to 0% any of the suffled deck will match
        # initial card order. But it is not 0%.
        for i in range(5000):
            cardDeck.shuffle()
            allCardsFromDeck = cardDeck.getRemainingCards()
            self.assertCountEqual(allCards, allCardsFromDeck)
            self.assertNotEqual(allCards, allCardsFromDeck)

    def test_dealOneCard(self):
        """
        Tests the CardDeck's dealOneCard and initialize methods.
        Randomness of dealOneCard is not tested.
        """
        cardDeck = CardDeck()
        self.assertEqual(52, len(cardDeck))

        card = cardDeck.dealOneCard()
        self.assertEqual(51, len(cardDeck))
        self.assertIsInstance(card, Card)

        # dealing all the remaining card
        for i in range(51):
            cardDeck.dealOneCard()

        # cardDeck is empty
        self.assertEqual(0, len(cardDeck))

        with self.assertRaises(NoCardException) as cm:
            cardDeck.dealOneCard()

        self.assertEqual("No more card to deal", str(cm.exception))

        # test initialize()
        cardDeck.initialize()
        self.assertEqual(52, len(cardDeck))


if __name__ == "__main__":
    unittest.main()
