from random import shuffle

class Card:
    

    ranks = [['A', 'ACE'], [2, 'TWO'], [3, 'THREE'], [4, 'FOUR'], [5, 'FIVE'], [6, 'SIX'], 
            [7, 'SEVEN'], [8, 'EIGHT'], [9, 'NINE'], [10, 'TEN'], ['J', 'JACK'], 
            ['Q', 'QUEEN'], ['K', 'KING']]

    # The weird spacing in `suits` is for art purposes. 
    # The spacing is stripped away in the `self.suit` attribute.
    suits = [['♠', ' SPADE '], ['♣', ' CLUB  '], ['♦', 'DIAMOND'], ['♥', ' HEART ']]


    def __init__(self, id: int):
        # Each card in a 52-card deck is represented uniquely by an integer between 0 and 51 and given by the argument `id`.
        if (id not in range(52)):
            raise Exception('id must be an integer between 0 and 51 inclusive. The value given to id was {}.'.format(id))
        
        # The rank and suit attributes are computed, along with art.
        self.rank_sym = self.ranks[id % 13][0]
        self.rank = self.ranks[id % 13][1]
        for j in range(4):
            if j*13 <= id < (j+1)*13:
                self.suit_sym = self.suits[j][0]
                self.suit_txt_art = self.suits[j][1]
                self.suit = self.suit_txt_art.strip(" ")
        # Just in case you want text-based cards.
        self.text = f"{self.rank} of {self.suit}S"
        # `10` is the only rank symbol represented with two characters, so it's handled separately.
        if self.rank_sym != 10:
            self.art = f"""┌-------┐
|{self.rank_sym}      |
|{self.suit_sym}      |
|{self.suit_txt_art}|
|      {self.suit_sym}|
|      {self.rank_sym}|
└-------┘""" 
        else: 
            self.art =f"""┌-------┐
|{self.rank_sym}     |
|{self.suit_sym}      |
|{self.suit_txt_art}|
|      {self.suit_sym}|
|     {self.rank_sym}|
└-------┘"""

# It's called Deck, but really this could also be used for hands, discard piles, combined decks, etc.
class Deck:
    
    def __init__(self, cards: list):

        self.cards = cards

        if not isinstance(cards, list):
            print(f"Warning: Problem initializing deck object. {self.cards} is not a list.\nPlease try again.")


    # Shuffles the deck.
    def shuffle(self):
        shuffle(self.cards)

    # Prints a message with the number of cards in the Deck.
    def count(self):
        print(f"There are {len(self.cards)} cards in {self}.")


    # Removes and returns the top card of the deck.
    # The cards are thought of being indexed top->bottom : 0 -> len(self.cards)-1.
    def give_card(self, index=0) -> Card:
        try:
            return self.cards.pop(index)
        except (IndexError, AttributeError):
            print(f'''Invalid input: give_card
            The cards in {self} are labeled 0 through {len(self.cards)-1}.
            Try again with an integer in this range.''')


    # Adds the card to the bottom of the deck.
    def take_card(self, card: Card) -> None:
        if card == None:
            return None
        else:
            self.cards.append(card)


    # Displays the first 8 (or fewer) cards in a deck.
    # There's probably a more flexible way to do this allowing more cards displayed...
    # `down` is a list of indices of cards you want displayed face down.
    def reveal1(self, down=[]) -> str:
        # For displaying a face down card. 
        face_down = f"""┌-------┐
|███████|
|███████|
|███████|
|███████|
|███████|
└-------┘"""
        # Collects the card art to be used. 
        art_list = []
        for card in self.cards:
            art_list.append(card.art)
        for i in down:
            art_list[i] = face_down
        # `current` will accumulate and be returned as a string by `reveal`.
        current = [''] * 7
        # First row.
        for art in art_list[:3]:
            # Turns a string into a list with each successive entry being a new line.
            temp = art.split('\n')
            current = [current[i] + ' ' + temp[i] for i in range(len(temp))]
        # Second row.
        if len(art_list) > 3:
            current += ['     ']*7
            for art in art_list[3:5]:
                temp = ([''] * 7) + art.split('\n')
                current = [current[i] + ' ' + temp[i] for i in range(len(temp))]
        # Third row.
        if len(art_list) > 5:
            current += ['']*7
            for art in art_list[5:8]:
                temp = ([''] * 14) + art.split('\n')
                current = [current[i] + ' ' + temp[i] for i in range(len(temp))]
        # Converts a list into a string while separating entries with newlines. 
        current = '\n'.join(current)
        print(current)
    

    # Alternate art. Deck is laid out diagonally.
    def reveal2(self) -> str:
        current = [''] * 7
        # Generates art one card at a time
        # Will handle the last card separately
        for j in range(len(self.cards) - 1):
            # Creates a two new lines on top of `current` with 2j space characters.
            current = [' ' * 2 * j] + current
            # Splits the jth card art into a list of length 7.
            temp = self.cards[j].art.split('\n')
            # Prints the new card 2 spaces to the right and 1 space above the previous card.
            current = [current[i][:2 * j] + temp[i] for i in range(7)] + current[7:]
        # This part is to remove the first letter of 'DIAMOND' from the cards which are not the last card.
        current = [current[i].replace('D', ' ') for i in range(len(current))]
        # Flip last card.
        j = (len(self.cards) - 1)
        current = [' ' * 2 * j] + current
        temp = self.cards[j].art.split('\n')
        current = [current[i][:2 * j] + temp[i] for i in range(7)] + current[7:]
        # Prints the result
        print('\n'.join(current))
    
    #Alternate art. Deck is laid out horizontally.
    def reveal3(self) -> str:
        current = [''] * 7
        # Generates art one card at a time
        for j in range(len(self.cards) - 1):
            # Splits the jth card art into a list of length 7.
            temp = self.cards[j].art.split('\n')
            # Prints the new card 2 spaces to the right and 1 space above the previous card.
            current = [current[i][:2 * j] + temp[i] for i in range(7)] + current[7:]
        # This part is to remove the first letter of 'DIAMOND' from the cards which are not the last card.
        current = [current[i].replace('D', ' ') for i in range(len(current))]
        # Flip last card.
        j = (len(self.cards) - 1)
        temp = self.cards[j].art.split('\n')
        current = [current[i][:2 * j] + temp[i] for i in range(7)] + current[7:]
        # Prints the result
        print('\n'.join(current))
            
# This will merge two Decks into a new Deck.
# For example, merge discard pile or players hand with main deck after a round.
def combine_decks(deck1, deck2):
    d = Deck(deck1.cards + deck2.cards)
    deck1.cards = []
    deck2.cards = []
    return d

def test():
    pass