"""
Run.py
Command Line Interface for Playing Cards
"""
import sys
import argparse
from collections import namedtuple

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

    def create_deck(self, shuffle):
        # Instantiate and build the deck of cards as well as the Card Object (inheritance)
        deck = Deck(shuffle)
        return deck
    def ready_player(self,player,deck,num_cards):
        player.deck = deck # Linking player to the deck
        # Declare namedtuple
        player_info = namedtuple('player_info',['name','hand','count','total'])
        new_player = player_info(player.name,
                                 player.draw(num_cards).show_hand(),
                                 player.count(),
                                 player.total())
        return new_player




if __name__ == '__main__':
    args = PlayCardsApp.parse_args(sys.argv[1:])
    app = PlayCardsApp(args.verbose)
    deck = app.create_deck(args.shuffle)
    list_of_players = []
    players = args.players[0].split(',')
    for player in players:
        list_of_players.append(app.ready_player(Player(player), deck, int(args.num_cards)))
    print('Ready!')


    

