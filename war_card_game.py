'''
A simulation of a game of war (card game) played by 2 computer players
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:
    def __init__(self,suit, rank):
        '''
        suit: str
        rank : str
        value: int; look up the key of values( global dictionary )
        '''
        self.suit = suit
        self.rank = rank
        self.value = values[rank]      
        # common in oop where a class refers to a global dictionary or imported library

        def __str__(self):
            return self.rank + 'of' + self.suit
            

class Deck:
    # split, shuffle, deal cards from the deck object
    def __init__(self):
        '''
        create all 52 card objects
        hold as a list of card objects
        '''
        # a class object holding instances of another class
        # not inheritance
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                # you can print any card here as there is string method of card

    def deck_shuffle(self):
        random.shuffle(self.all_cards)
        # no need to return because random.shuffled is done inplace
        # this function will change the deck.all_cards

    def deal_one(self):
        return self.all_cards.pop()
        # this will also remove card from self.all_cards
        # call 3 times to deal 3 cards 


class Player:
    '''
    hold a player's current list of cards
    # translate a deck/hand of cards with top and bottom to a python list
    # list[0], list[-1]

    '''
    def __init__(self, name):
        self.name = name
        self.all_cards_list = []

    def add_cards(self,new_cards):
        #single card or multiple card from their list
        if type(new_cards)== type([]):
            self.all_cards_list.extend(new_cards)
        else:
            self.all_cards_list.append(new_cards)
            
    def remove_one (self):
        return self.all_cards_list.pop(0)

    def __str__(self):
        return f'player {self.name}: has {len(self.all_cards_list)} cards.'

### main ###


# game initialization
player_one = Player('One')      
player_two = Player('Two')

new_deck = Deck()
new_deck.deck_shuffle()

# split decks to 2 players
for i in range(26):
    player_one.add_cards(new_deck.deal_one())   
    # adds cards from deck to Player.all_cards_list
    player_two.add_cards(new_deck.deal_one()) 


game_on = True
round_count= 0

# round initialization
while game_on:
    round_count += 1 
    print(f'Round = {round_count}')

    # check player hands 
    if len(player_one.all_cards_list) == 0:
        print('Player 1 lost. Player 2 lost')
        game_on = False
        break

    if len(player_two.all_cards_list) == 0:
        print('Player 2 lost. Player 1 lost')
        game_on = False
        break

    
    # start a new round
    player_one_cards = []       
    # the cards player 1 puts on table
    player_one_cards.append(player_one.remove_one())
    # player one remove 1 card from player_one.all_cards_list and
    # add this card to the table (player_one_cards)
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('war')
            if len(player_one.all_cards_list) < 5:
                print('Player 1 unable to pay for war')
                print('player 2 wins')
                game_on = False
                break
            elif len(player_two.all_cards_list) < 5:
                print('Player 2 unable to pay for war')
                print('player 1 wins')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())













