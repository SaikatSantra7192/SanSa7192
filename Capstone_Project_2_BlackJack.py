import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing= True

class Card:    
    def __init__(self,suit,rank):
        self.suit= suit
        self.rank= rank
        
    def __str__(self):
        return (f'{self.rank} of {self.suit}')
    
    @property
    def value(self):
        return self.values.get(self.rank)
    
class Deck:    
    def __init__(self):
        self.deck=[]
        self.computer=[]
        self.player=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    '''            
    def __str__(self):
        deck_show = ''
        for card in self.deck:
            deck_show += '\n '+card.__str__() 
        return 'The deck has:' + deck_show'''
        
    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
    
    def remove(self, card):
        if card in self.deck:
            self.deck.remove(card)
            return True
        else:
            return False
    
    def init_deal(self):
        count=1
        while count<5:
            if count%2==0:
                comp=self.deck.pop()
                self.computer.append(comp)
                count+=1
                
            elif count%2!=0:
                playr=self.deck.pop()
                self.player.append(playr)
                count+=1
            else:
                break
        
        
        return (self.computer,self.player)
    
    '''def __str__(self):
        hand_comp= ''
        hand_player= ''
        for comp in self.computer:
            hand_comp += '\n '+comp.__str__()
        for card in self.player:
            hand_player += '\n '+card.__str__()
        return (f'The computer has: {hand_comp} \n\nThe player has: {hand_player}')'''
        
    def is_empty(self):
        return (len(self.deck) == 0)
    
class Hand:
    def __init__(self):
        self.hand=Deck().init_deal()
        self.hand_com=self.hand[0]
        self.hand_playr=self.hand[1]
        self.value_comp = 0 
        self.value_player = 0
        self.aces = 0
        
    def add(self):
        self.val_comp=(' '.join(val.split()[0] for val in self.hand_com))
        self.val_player=(' '.join(val.split()[0] for val in self.hand_playr))
        self.val_comp_lst=self.val_comp.split()
        self.val_player_lst=self.val_player.split()
        
        for val in self.val_comp_lst:
            self.value_comp += values[val]
        for val in self.val_player_lst:
            self.value_player += values[val]
            
    def __str__(self):
        deck_comp = ''
        deck_playr=''
        for card in self.hand_com:
            deck_comp += '\n '+card.__str__()
        for card in self.hand_com:
            deck_playr += '\n '+card.__str__()
        
        return (f'Computer Value {deck_comp} \nPlayer value {deck_playr}')
    

x=Deck()
x.shuffle()
x.init_deal()
y=Hand()
y.add()

print(x)
print(y)