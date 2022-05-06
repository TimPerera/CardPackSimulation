
# Card Simulation

In this project, a deck of Cards is made available, along with the basic methods you could expect to apply on a deck of cards. You can simulate the behaviors of a Player as well. I make no efforts to recognize the color of cards (r/b).

Deck Methods:
- build()
- count()
- show_top()
- show_bottom()
- burn_top()
- shuffle()
- serve()
- show()

Player Methods:
- draw()
- discard()
- discard_all()
- show_hand()
- count()
- total()


Example Use Case:
```
    from card_game import Deck, Player

    deck = Deck(shuffle = True)
    player = Player('example_name')
    player.deck = deck # This makes sure that the player is linked to the deck of cards
```

What's Outstanding in this Project:
- [ ] Build tests
- [ ] Publish to distribution and on PyPI
- [ ] Create game (Black Jack)




