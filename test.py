# Annie L and Ella N
#started: 9/29/16 version 0.5a

from random import randint 
from random import shuffle 


print("Welcome to Go Fish-bot Version 0.5a.  I am the premier Go Fish program in the universe.")
user = input("Hello!  What is your name? [Type your name and press enter.] ")
print("Hello,", user, "today we are going to play Go Fish!")
# These lines introduce the user to our program and records their name.

rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES. "))

if rules == 0:
print ("Object Of The Game: The objective of the game is to win the most of cards. A book  is any four of a kind and suits do not matter!\n
   The Deal: Any player can deal one card to each player and whoever has the lowest card is the dealer.\n The dealer then shuffles the cards and hands them over to the player
   on his right who cuts them, and then gives them back to the dealer. The dealer will then deal the cards clockwise, one at a time, face down, beginning with the
   player on his left. Depending on the amount of players, if there are 2 to 3 people playing, each player gets seven cards. Since four people are playing, each player gets five cards.
  The remainder of the pack is placed face down on the table to form the stock.\n The Play: The player to the left of the dealer then looks directly at and says the name of any opponent they choose.
   You MUST have a least one card that you ask an opponent for. The player you ask must hand over all the cards requested. If your opponent doesn't have the card you asked for your opponent will say,
   Go Fish! As long as you succeed in getting cards, you can keep asking players for cards. When a player gets a book, that book should be verified by the others and placed down. Turns go to the left.\n
   Finishing The Game: When all the books in the game have been won, the winner is the player with the most amount of books.\n Good Luck!”)
else:
    print "Great, you're ready to play! Good Luck!”

deck = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
full_deck = deck * 4 
   card_dealt = deck[0]
#SEE WHO GOES FIRST




def dealer():
    p1hand = 0
    p2hand = 0
    p3hand = 0
    p4hand = 0
	# cards_dealt = 0
	# while cards_dealt < 5:
	# deal_card_to p1
	# remove from deck
	# deal card to p2
	# remove from deck
	# deal to p3hand
	# remove from deck
	# deal to p4hand
	# remove from deck
	# cards_dealt += 1
while p1hand < 2:
	p1hand.append(deck)
    deck.remove(deck[0])
 while p2hand < 2:
	p2hand.append(deck)
    deck.remove(deck[0])
    while p3hand < 2:
	p3hand.append(deck)
    deck.remove(deck[0])
    while p4hand < 2:
	p4hand.append(deck)
    deck.remove(deck[0])


def deal_card ():
    p1hand = 0
    p2hand = 0
    p3hand = 0
    p4hand = 0
    while p1hand < 5:
	p1hand.append(deck)
    deck.remove(deck[0])
 while p2hand < 5:
	p2hand.append(deck)
    deck.remove(deck[0])
    while p3hand < 5:
	p3hand.append(deck)
    deck.remove(deck[0])
    while p4hand < 5:
	p4hand.append(deck)
    deck.remove(deck[0])

def ask():
   player_turn = 0
   if player_turn == 1:
      asking_player.append(card_dealt)
      ask_player = (input("Who do you want to ask for a card?[p1hand, p2hand, p3hand, p4hand]")
      ask_card = (input("What card do you want?")
	print (ask_player, "Do you have a", ask_card, "?[respond yes or no]")
	elif player_turn == 2:
	 asking_player.append(card_dealt)
      ask_player = (input("Who do you want to ask for a card?[p1hand, p2hand, p3hand, p4hand]")
      ask_card = (input("What card do you want?")
	elif player_turn == 3:
	 asking_player.append(card_dealt)
      ask_player = (input("Who do you want to ask for a card?[p1hand, p2hand, p3hand, p4hand]")
      ask_card = (input("What card do you want?")
	 else:
	  asking_player.append(card_dealt)
      ask_player = (input("Who do you want to ask for a card?[p1hand, p2hand, p3hand, p4hand]")
      ask_card = (input("What card do you want?")
	  if ask == "yes":
		ask_player.remove(card_dealt)
		asking_player.append(card_dealt)
	elif ask = "no":
	print "Go Fish!"
	else:
	print "That's not an answer!"
