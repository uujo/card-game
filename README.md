# card-game
Sample codes for representing a deck of poker-style playing cards

## Runnig the test (Requires Python 3.5 or new version)

* Clone the this repository: `git clone https://github.com/uujo/card-game.git`
* Set the PYTHONPATH to ([cloned direrctory]/card-game/src/) and run `test_CardDeckTest.py`

  For Mac/Linux
  ```
  > cd [cloned direrctory]/card-game/test/
  > PYTHONPATH=[cloned direrctory]/card-game/src/ python test_CardDeckTest.py`
  ```
  
  For Windows (assumping the codes are cloned in C: drive) 
  ```
  > cd [cloned direrctory]/card-game/test/
  > set PYTHONPATH=C:[cloned direrctory]\card-game\src
  > python test_CardDeckTest.py
  ```
 
## Structur of the code:

### There are 3 modules in CardGame packages
 
1. Card.py: 
    
    * Contains **`Card`** data structure ([collections.namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple) is used).
      Data structure for **`Card`** is borrowed the idea from [_Fluent Python_](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008/ref=sr_1_2?hvadid=241675711667&hvdev=c&hvlocphy=9007779&hvnetw=g&hvpos=1t1&hvqmt=e&hvrand=12351625625351566461&hvtargid=kwd-75527750746&keywords=fluent+python&qid=1553104567&s=gateway&sr=8-2&tag=googhydr-20) 
    
    * Putting **`Card`** data structure in a seperate module might be considered as unecessary decomposition since it is a buildin data structure. 
      However, this [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple) could be replace with Card class with some supporting method if additional requirement is added. In that case, it might make more sense to maintain it in a separate module.
      
2. CardDeckABC.py:

    * Contains **`CardDeckABC`** [Abstract Base Class](https://docs.python.org/3/library/abc.html) for any _CardDecks_ which supports **`shuffle()`** and **`dealOneCard()`**
    * This ABC is added to support different types of decks for different card games (abstracted out common methods).
    
3. CardDeck.py:

    * Includes **`CardDeck`** class which inherits _CardDeckABC_ and implements a card deck with 52 playing cards in four suits: hearts, spades, clubs, diamonds, with face values of Ace,
2-10, Jack, Queen, and King.
    * Contains a custom expetion **(`EmptyCardDeckExcepton`)** which will be raised when **`dealOneCard()`** is called on the empty deck. 
      LookupError could be used instead but using a custom exception represents the specific condition which might be handled different. 

    
### Unittest is created under 'card-game/test' directory  

1. test_CardDeckTest.py
    
    * test **`shuffle()`** and **`dealOneCard()`** methods in CardDeck class
    * To achieve correct tests randomness needs to be tested for both methods (_[addional information](https://www.random.org/analysis/)_).
      However, it is replaced with un imcomplete heuristic test for now.
