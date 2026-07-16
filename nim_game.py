#!/usr/bin/env python
# -*- coding: utf-8 -*-

import secrets

MATCH_NUMBER = 21
ERROR_INPUT = "Erreur de saisie."


def init_nims():
    """
    Setting up the board game

    :return: True array
    """
    return [True for _ in range(MATCH_NUMBER)]


def show_nims(board):
    """
    Show the board game where an “o” indicates that there is a match

    :param board: True and False array
    """
    print('|' + ''.join(['o|' if nim else ' |' for nim in board]))


def before_start_game():
    print("Bienvenue dans le jeu de Nim.")
    SAY_YOUR_NAME = "Saisissez votre nom:"
    number_player, start_player1, is_computer = 0, False, False

    while number_player != 1 and number_player != 2:
        try:
            number_player = int(input("Vous souhaitez jouer contre l'ordinateur (1) ou votre ami (2) ? [1/2]:"))
        except ValueError:
            print(ERROR_INPUT)

    name_player1 = input(f"Joueur 1: {SAY_YOUR_NAME}")
    if number_player == 2:
        name_player2 = input(f"Joueur 2: {SAY_YOUR_NAME}")
    else:
        is_computer = True
        name_player2 = "Ordinateur"

    check_player1_start = ""

    while check_player1_start != 'y' and check_player1_start != 'n':
        try:
            check_player1_start = input(f"Est-ce que c'est {name_player1} qui commence ? [y/n] ")
        except ValueError:
            print(ERROR_INPUT)

    return name_player1, name_player2, (start_player1 or check_player1_start == 'y'), is_computer


def take_match(board, number_match):
    first_index_match = board.index(True)
    last_index_match_remove = first_index_match + number_match

    if last_index_match_remove < MATCH_NUMBER:
        board[first_index_match:last_index_match_remove] = [False] * number_match
    else:
        board[first_index_match:MATCH_NUMBER] = [False] * (MATCH_NUMBER - first_index_match)
    return board


def computer_play(board):
    match_to_take = (board.count(True) - 1) % 5

    if match_to_take == 0:
        return 4 - secrets.randbelow(4)
    return match_to_take


def loop_game():
    name_player1, name_player2, start_player1, computer_is_play = before_start_game()
    board = init_nims()

    if start_player1:
        turn_order = (name_player1, name_player2)
    else:
        turn_order = (name_player2, name_player1)

    your_turn, match_remove = 0, 0
    while any(board):
        if computer_is_play and turn_order[your_turn] is name_player2:
            match_remove = computer_play(board)
            print(f"L'{turn_order[your_turn]} a pris {match_remove} allumette(s)")
        else:
            match_remove = input(
                f"{turn_order[your_turn]}, combien d'allumettes souhaites-tu retirer (entre 1 et 4).")

            while not (len(match_remove) == 1 and match_remove.isdigit() and 1 <= int(match_remove) <= 4):
                print(ERROR_INPUT)
                match_remove = input(
                    f"{turn_order[your_turn]}, combien d'allumettes souhaites-tu retirer (entre 1 et 4).")

        board = take_match(board, int(match_remove))
        show_nims(board)
        your_turn = (your_turn + 1) % 2

    print(f"{turn_order[your_turn]}, vous avez gagné. Félicitations !")


if __name__ == "__main__":
    loop_game()
