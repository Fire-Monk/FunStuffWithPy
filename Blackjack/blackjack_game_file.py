import art
import os
from time import sleep
import random


def sum_new(card_list):
    sum_of_cards = 0
    for card in card_list:
        if str(card) == "A" and sum_of_cards + 11 >= 21:
            sum_of_cards += 1
        elif str(card) == "A" and sum_of_cards + 11 < 21:
            sum_of_cards += 11
        elif str(card) in "JQK":
            sum_of_cards += 10
        else:
            sum_of_cards += card
    return sum_of_cards


def show_card_info(my_cards, comp_first_card):
    print(f"Your cards are: {my_cards}; Your current score: {sum_new(my_cards)}")
    print(f"Computer's first card: {comp_first_card}\n")


def decide_winner(my_total, comp_total, my_cards, computer_cards):
    if sum_new(my_cards) == 21 and len(my_cards):
        print("You won with a blackjack! (ACE + 10/J/Q/K)")
    elif sum_new(computer_cards) == 21 and len(computer_cards):
        print("You've lost, computer got a blackjack! (ACE + 10/J/Q/K)")
    elif my_total > 21:
        print("You lost, you have busted! (You went over 21.)\n")
    elif my_total <= 21:
        if comp_total > 21:
            print("You won, computer has busted! (Computer went over 21.)\n")
        elif comp_total == my_total:
            print("It's a draw!\n")
        elif comp_total < my_total:
            print(f"You won with {my_total - comp_total} points!\n")
        else:
            print(f"You lost by {comp_total - my_total} points!\n")
    else:
        print("The current situation was not perceived by the dumb dev!\n")


def play():
    os.system('cls')  # clears screen
    print(art.blackjack_logo)
    my_cards = []
    computer_cards = []
    for i in range(2):
        my_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    comp_first_card = computer_cards[0]
    show_card_info(my_cards, comp_first_card)
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    while hit == 'y':
        if sum_new(my_cards) <= 21 and sum_new(computer_cards) <= 21:
            my_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
            show_card_info(my_cards, comp_first_card)
            if sum_new(my_cards) <= 21 and sum_new(computer_cards) <= 21:
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
            else:
                hit = 'n'
        else:
            hit = 'n'

    if hit == 'n' and sum_new(computer_cards) < 17:
        computer_cards.append(random.choice(cards))

    my_total = sum_new(my_cards)
    comp_total = sum_new(computer_cards)
    print(f"Your final hand: {my_cards}, final score: {my_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {comp_total}\n")

    decide_winner(my_total, comp_total, my_cards, computer_cards)


# A = 11
# J = Q = K = 10
cards = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play()
os.system('cls')
print(art.blackjack_logo)
sleep(1)
print(art.game_by)
sleep(2)
print(art.aa1)
