import Cards
print("Press Enter to proceed through the demo.")
input()

print("It could be useful to follow along in the code.")

print("Let's make a deck...")
l = []
for i in range(52):
    l.append(Cards.Card(i))
deck = Cards.Deck(l)
input()

print("Lets look at this deck using all of the different display types!")
input()

print("Here's the first:")
deck.reveal1()
input()

print("It only displays the first 8 cards for laziness reasons.")
input()

print("Here's the second:")
deck.reveal2()
input()

print("This one should probably only be used for smaller decks...")
input()

print("aaaand the third:")
deck.reveal3()
input()

print("I like the third one the best for decks with a lot of cards.")
input()

print("Hopefully no one thinks the rank 10 cards are not rank 1 cards...")
input()

print("Let's shuffle the deck and reveal it again...")
deck.shuffle()
deck.reveal3()
input()

print("The art is updated every time the deck is modified!")
input()

print("Let's make a hand for you and I...")
your_hand = Cards.Deck([])
my_hand = Cards.Deck([])
input()

print("At this point I would make a player list, but I wont.")
input()

print("Now the dealer deals us both two cards from the top of the deck...")
for i in range(2):
    your_hand.take_card(deck.give_card())
    my_hand.take_card(deck.give_card())
input()

print("Let's reveal what you drew. Here's the first display type:")
your_hand.reveal1()
input()

print("The second:")
your_hand.reveal2()
input()

print("Third:")
your_hand.reveal3()
input()

print("I kind of like the second one here, tbh.")
input()

print("Observe that the top four cards have been removed from the deck:")
deck.reveal3()
input()

print("Let's play a round of 5-card draw. I'll shuffle the deck again...")
deck.shuffle()
input()

print("Let's make a deck representing a 5-card draw...")
draws = Cards.Deck([])
for i in range(5):
    draws.take_card(deck.give_card())
input()

print("Here's the flop...")
draws.reveal1([3, 4])
input()

print("Now the turn...")
draws.reveal1([4])
input()

print("And the river.")
draws.reveal1()
input()

print("Here's your hand for reference...")
your_hand.reveal2()
input()

print("And here's my hand. Who won?")
my_hand.reveal2()
input()

print("Now let's make a discard pile and discard our cards...")
print("A player list would be handy here...")
discard = Cards.Deck([])
discard = Cards.combine_decks(discard, my_hand)
discard = Cards.combine_decks(discard, your_hand)
input()

print("Now we combine the discard pile with the deck and shuffle...")
deck = Cards.combine_decks(discard, deck)
deck.shuffle()
input()

print("Observe your hand: ")
your_hand.reveal1()
input()

print("Mine is also empty: ")
my_hand.reveal1()
print("And so is the discard pile:")
discard.reveal1()
input()

print("The deck should be back to 52 cards:")
deck.reveal3()
input()

deck.reveal2()
print("The end!")