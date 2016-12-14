# Annie L and Ella N
#published: 11/02/16 version 1.2a

from random import randint 
from random import shuffle 


print("Welcome to Go Fish-bot Version 0.5a.  I am the premier Go Fish program in the universe.")
user = input("Hello!  What is your name? [Type your name and press enter.] ")
print("Hello,", user, "today we are going to play Go Fish!")
# These lines introduce the user to our program and records their name.

rules = int(input("Do you know how to play Go Fish? Enter 0 for NO and 1 for YES. "))

if rules == 0:
    print ('''
Object Of The Game: The objective of the game is to win the most books of cards. A book is any four of a kind and suits do not matter!\n
   The Deal: Any player can deal one card to each player; whoever has the lowest card will be the dealer.\n The dealer then shuffles the cards, hands them over to the player
   on his right who cuts them, and then gives them back to the dealer. The dealer will then deal the cards clockwise, one at a time, face down, beginning with the
   player on his left. Depending on the amount of players, if there are 2 to 3 people playing, each player gets seven cards. Since four people are playing, each player gets five cards.
   The remainder of the pack is placed face down on the table to form the stock.\n The Play: The player to the left of the dealer then looks directly at and says the name of any opponent they choose.
   You MUST have a least one card that you ask an opponent for. The player you ask must hand over all the cards requested. If your opponent doesn't have the card you asked for your opponent will say,
   Go Fish! As long as you succeed in getting cards, you can keep asking players for cards. When a player gets a book, that book should be verified by the others and placed down. Turns go to the left.\n
   Finishing The Game: When all the books in the game have been won, the winner is the player with the most amount of books.\n Good Luck!
   ''')
else:
    print ("Great, you're ready to play! Good Luck!")
    

def are_you_ready():
    print (input("are you ready to play?[enter 1 for no, 2 for yes]"))
    if are_you_ready == 1:
        print ("Ok go whenever you are ready")
    else:
        print ("We are ready to start")
    
deck = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
full_deck = deck * 4 
card_dealt = deck[0]
#SEE WHO GOES FIRST




def dealer():
    p1hand = []
    p2hand = []
    p3hand = []
    p4hand = []
    card_dealt = 0
    while card_dealt < 1:
        p1hand.append(full_deck[0])
        full_deck.remove(full_deck[0])
        p2hand.append(full_deck[0])
        full_deck.remove(full_deck[0])
        p3hand.append(full_deck[0])
        full_deck.remove(full_deck[0])
        p4hand.append(full_deck[0])
        full_deck.remove(full_deck[0])
        card_dealt += 1
first_player = min(value[p1hand[0]], value[p2hand[0]], value[p3hand[0]], value[p4hand[0]]) 
if value[p1hand[0]] == goes_first:
            print ("Player 1 deals the cards because they have the lowest card.")
            first_player = 1
elif value[p2hand[0]] == goes_first:
            print (" Player 2 deals the cards because they have the lowest card.")
            first_Player = 2 
elif value[p3hand[0]] == goes_first:
            print (" Player 3 deals the cards because they have the lowest card.")
            first_player = 3   
elif value[p4hand[0]] == goes_first:
            print ("Player 4 deals the cards because they have the lowest card.")
            first_player = 4
else:
             print ("I guess something happened. Please restart the program.")


if first_player == 1:
    deal_card()
elif first_player == 2:
    deal_card()	 
elif first_player == 3:
    deal_card
elif first_player == 4:
    deal_card
else:
	print ("Something went wrong. Try again.")


		
	
def deal_card ():
    p1hand = []
    p2hand = []
    p3hand = []
    p4hand = []
    card_dealt = 0
    while card_dealt < 5:
        p1hand.append(full_deck[0])
        full_deck.remove(full_deck[0])
        p2hand.append(full_deck[0])
        full_deck.remove(full_deck[0])
        p3hand.append(full_deck[0])
        full_deck.remove(full_deck[0])
        p4hand.append(full_deck[0])
        full_deck.remove(full_deck[0])
        card_dealt += 1

def ask():
    player_turn = 0
    if player_turn == 1:
        asking_player.append(card_dealt)
        ask_player = (input("Who do you want to ask for a card?[p1hand, p2hand, p3hand, p4hand]"))
        ask_card = (input("What card do you want?"))
        print (ask_player, "Do you have a", ask_card, "?[respond yes or no]")
    elif player_turn == 2:
        asking_player.append(card_dealt)
        ask_player = (input("Who do you want to ask for a card?[p1hand, p2hand, p3hand, p4hand]"))
        ask_card = (input("What card do you want?"))
    elif player_turn == 3:
        asking_player.append(card_dealt)
        ask_player = (input("Who do you want to ask for a card?[p1hand, p2hand, p3hand, p4hand]"))
        ask_card = (input("What card do you want?"))
    else:
        asking_player.append(card_dealt)
        ask_player = (input("Who do you want to ask for a card?[p1hand, p2hand, p3hand, p4hand]"))
        ask_card = (input("What card do you want?"))
    if ask == "yes":
        ask_player.remove(card_dealt)
        asking_player.append(card_dealt)
    elif ask == "no":
        print ("Go Fish!")
    else:
        print ("That's not an answer!")
		start_game()
ask()
dealer()
deal_card()
start_game