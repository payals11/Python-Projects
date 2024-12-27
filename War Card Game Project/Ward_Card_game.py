"""  WAR CARD GAME

Created on December 5, 2020
@author: Payal Shinde

"""

import random


class Card:
    # This contains all the cards, it's values and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def create_card(self):
        return f"Card:{self.suit}  Rank:{self.rank}"


class Deck:
    def __init__(self, suits, ranks, values):
        # Creates pack of 52 playing cards
        self.suits = suits
        self.ranks = ranks
        self.values = values
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                card_obj = Card(suit, self.values[rank])
                created_card = card_obj.create_card()
                self.all_cards.append(created_card)

    def shuffle_cards(self, cards):
        # Shuffles created cards
        random.shuffle(cards)

    def distribute_cards(self):
        # Distributes cards between two players
        self.shuffle_cards(self.all_cards)
        player1_cards = []
        player2_cards = []
        for iter in range(len(self.all_cards)):
            if iter % 2 == 0:
                player1_cards.append(self.all_cards[iter])
            else:
                player2_cards.append(self.all_cards[iter])

        return player1_cards, player2_cards


if __name__ == '__main__':
    print("#####################################################################################")
    print()
    print("                             Welcome to WAR CARD GAME                                ")
    print()
    print("#####################################################################################")

    print("\nThis War Card game is being played between two players!!! You and computer player!!\n")

    player1 = input("Enter player name:").capitalize()
    player2 = 'Computer'

    print(f"\nGame players:\n{player1} and Computer\n")

    print("\n>>>>>>>>>>>>>>>>>>>>><>>>>>>   Game starts   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    cards = Deck(suits, ranks, values)
    player1_cards, player2_cards = cards.distribute_cards()
    gameon = True
    gameround = 0
    player1_card_drawn = []
    player2_card_drawn = []
    player1_won_cards = []
    player2_won_cards = []
    tie_cards = []
    war = str()
    tie_iter = int()

    while gameon:
        gameround += 1
        print(f"\nGame round={gameround}")

        if len(player1_cards) == 0:
            if len(player1_won_cards) == 0:
                print(f"\nPlayer1 {player1} has no cards remaining!!! Player2 Computer Wins!!\n")
                gameon = False
                break
            else:
                player1_cards.extend(player1_won_cards)
                player1_won_cards = []

        if len(player2_cards) == 0:
            if len(player2_won_cards) == 0:
                print(f"\nPlayer2 Computer has no cards remaining!!! Player1 {player1} Wins!!\n")
                gameon = False
                break
            else:
                player2_cards.extend(player2_won_cards)
                player2_won_cards = []

        # Shuffling both player cards
        cards.shuffle_cards(player1_cards)
        cards.shuffle_cards(player2_cards)

        if war == 'Tie':
            # When Tie situation occurs, each player will draw 3-3 cards each

            if len(player1_cards) >= 3 and len(player2_cards) >= 3:
                tie_iter = 1
                print("Tie!!! Now both players will draw 3-3 cards each!!")
            else:
                player1_cards.extend(player1_won_cards)
                player1_won_cards = []
                player2_cards.extend(player2_won_cards)
                player2_won_cards = []
                cards.shuffle_cards(player1_cards)
                cards.shuffle_cards(player2_cards)
                if len(player1_cards) >= 3 and len(player2_cards) >= 3:
                    tie_iter = 1
                    print("Tie!!! Now both players will draw 3-3 cards each!!")
                else:
                    tie_iter = 0
                    if len(player1_cards) < 3:
                        print(
                            f"\nPlayer1 {player1} doesn't have 3 cards remaining to play after tie!!! Player2 "
                            f"Computer Wins!!\n")
                        gameon = False
                        break
                    if len(player2_cards) < 3:
                        print(
                            f"\nPlayer2 Computer doesn't have 3 cards remaining to play after tie!!! Player1 {player1} Wins!!\n")
                        gameon = False
                        break

            while 0 < tie_iter <= 3:
                if gameround > 1:
                    userinput = input("Do you want to continue to play Y/N?").strip()
                    while userinput.strip() not in ('Y', 'y', 'N', 'n'):
                        userinput = input("Please enter valid input Y/N!!").strip()
                    if userinput in ('Y', 'y'):
                        gameon = True
                    else:
                        gameon = False
                        exit()

                print(f"\nPlay {player1}:")
                print("Your available cards:")
                for i in range(1, len(player1_cards) + 1):
                    print(f"{i} = {player1_cards[i - 1]}")
                num = input(f"\nEnter a left side card number which you want to draw: ").strip()

                try:
                    num = int(num)
                except:
                    print("You have entered Invalid input!!")
                finally:
                    while num not in range(1, len(player1_cards) + 1):
                        num = input(f"Please enter valid left side card number 1-{len(player1_cards)}:").strip()
                        try:
                            num = int(num)
                        except:
                            print("Invalid input entered other than numeric valid in range data!!")

                player1_card_drawn.append(player1_cards.pop(num - 1))
                print(f"\nPlayer1 {player1} card drawn = {player1_card_drawn[-1]}")

                print(f"\n{player2} turn:")
                player2_card_drawn.append(player2_cards.pop(0))
                print(f"Player2 Computer card drawn = {player2_card_drawn[-1]}\n")

                tie_iter += 1
        else:
            if gameround > 1:
                userinput = input("Do you want to continue to play Y/N?").strip()
                while userinput.strip() not in ('Y', 'y', 'N', 'n'):
                    userinput = input("Please enter valid input Y/N!!").strip()
                if userinput in ('Y', 'y'):
                    gameon = True
                else:
                    gameon = False
                    break

            print(f"\nPlay {player1}:")
            print("Your available cards:")
            for iter in range(1, len(player1_cards) + 1):
                print(f"{iter} = {player1_cards[iter - 1]}")
            num = input(f"\nEnter a left side card number which you want to draw: ").strip()

            try:
                num = int(num)
            except:
                print("You have entered Invalid input!!")
            finally:
                while num not in range(1, len(player1_cards) + 1):
                    num = input(f"Please enter valid left side card number 1-{len(player1_cards)}:").strip()
                    try:
                        num = int(num)
                    except:
                        print("Invalid input entered other than numeric valid in range data!!")

            player1_card_drawn.append(player1_cards.pop(num - 1))

            print(f"\nPlayer1 {player1} card drawn = {player1_card_drawn[-1]}")

            print(f"\n{player2} turn:")
            player2_card_drawn.append(player2_cards.pop(0))

            print(f"Player2 Computer card drawn = {player2_card_drawn[-1]}\n")

        deal1 = int(player1_card_drawn[-1].split(':')[2])
        deal2 = int(player2_card_drawn[-1].split(':')[2])

        if deal1 > deal2:
            player1_won_cards.extend(player1_card_drawn)
            player1_won_cards.extend(player2_card_drawn)
            player1_won_cards.extend(tie_cards)
            print(f"\nCards won by Player1 {player1}!!\n")
            print(
                f"Player1 {player1} total available cards count =>  Current cards:{len(player1_cards)}  Won cards:{len(player1_won_cards)}")
            print(
                f"Player2 Computer total available cards count =>  Current cards:{len(player2_cards)}  Won cards:{len(player2_won_cards)}\n")
            tie_cards = []
            player1_card_drawn = []
            player2_card_drawn = []
            war = ''
            gameon = True
        elif deal1 < deal2:
            player2_won_cards.extend(player1_card_drawn)
            player2_won_cards.extend(player2_card_drawn)
            player2_won_cards.extend(tie_cards)
            print(f"\nCards won by Player2 Computer!!\n")
            print(
                f"Player1 {player1} total available cards count =>  Current cards:{len(player1_cards)}  Won cards:{len(player1_won_cards)}")
            print(
                f"Player2 Computer total available cards count =>  Current cards:{len(player2_cards)}  Won cards:{len(player2_won_cards)}\n")
            tie_cards = []
            player1_card_drawn = []
            player2_card_drawn = []
            war = ''
            gameon = True
        else:
            war = 'Tie'
            tie_cards.extend(player1_card_drawn)
            tie_cards.extend(player2_card_drawn)
            print(
                f"Player1 {player1} total available cards count =>  Current cards:{len(player1_cards)}  Won cards:{len(player1_won_cards)}")
            print(
                f"Player2 Computer total available cards count =>  Current cards:{len(player2_cards)}  Won cards:{len(player2_won_cards)}\n")
            player1_card_drawn = []
            player2_card_drawn = []
            gameon = True
