"""
Card.py

Class that makes up the properties of a Card in a Deck of Cards. This is the base class for Deck and Player classes.
"""

# TODO: Add tests
# TODO: Build in to a package
# TODO: Build a command-line interface


class Card():
    """
    Creates a Card object that make up the card deck. Each card has it's own value (val) and suit. This 
    will be the base class for the Deck and Player sub classes.
    Inputs: 
        val: (str) Indicates the value of the card
        suit:(str) Indicates the suit of the card
    
    Returns:
        <Card> obj
    """
    def __init__(self,val,suit):
        "Creates a tuple of the value and the suit of the card and allows you to access these individually"
        self.card = (val,suit)
        self.val = val
        self.suit = suit

    def show_card(self):
        """
        Reveals the value and suit of an individual card. 
        Inputs:
            Card Object
        Returns:
            str value stating the value and suit of the card.
        """
        return f'{self.card[0]} of {self.card[1]}'



