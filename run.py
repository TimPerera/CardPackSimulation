"""
Run.py
Command Line Interface for Playing Cards
"""
import sys
import argparse

from deck import Deck
from player import Player

class PlayCardsApp():

    def __init__(self, verbose):
        self.verbose = verbose
    @staticmethod
    def parse_args(arguments):
        """
        list of players - Default [player]
        how many cards to serve (opt)
        verbose
        """
        parser = argparse.ArgumentParser()
        # Number of players playing
        parser.add_argument('-p','--players', action='store',
                            default='player',
                            nargs='*',
                            help = 'List of players playing.')
        # How many cards to serve to each player
        parser.add_argument('-n','--num_cards',
                            default = 1,
                            help = 'Choose how many cards to distribute to each player')
        # Choose whether to shuffle the cards in the deck
        parser.add_argument('-s','--shuffle',
                            default = 'Y',
                            choices = ['Y','N'],
                            help = 'Choose whether to shuffle the deck.')
        # For more logging (troubleshooting) choose whether to be verbose
        parser.add_argument('-v', '--verbose',
                            default='Y',
                            choices = ['Y', 'N'])
        args = parser.parse_args(arguments)
        return args

    def run(self,players,num_cards,shuffle):
        """
        Initializes and executes Playing Card Modules (Cards, Deck, Player)
        """
        deck = Deck() # Instantiate and build the deck of cards as well as the Card Object (inheritance)

        if shuffle == 'Y':
            deck.shuffle()
        
        for player in players: # Ensure that each player is playing from the same deck
            player = Player()
            player.deck = deck
        
        deck.serve(num_cards, [players]) # Distribute cards to all the players


if __name__ == '__main__':
    args = PlayCardsApp.parse_args(sys.argv[1:])
    app = PlayCardsApp(args.verbose)
    app.run(args.players, args.num_cards, args.shuffle)

