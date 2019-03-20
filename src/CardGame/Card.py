from collections import namedtuple

"""
Representation of the card with rank and suits
This doesn't have to be in the separate module.
However, it can be replace with class if some methods need to be attached.
i.e values of the card
"""

Card = namedtuple("Card", ["rank", "suit"])
