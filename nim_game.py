#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init_nims(nims_number):
    return [True for _ in range(nims_number)]


def show_nims(board):
    print('|' + ''.join(['o|' if nim else ' |' for nim in board]))


def before_start_game():
    print("Bienvenue dans le jeu de Nim.")
    SAY_YOUR_NAME = "Saisissez votre nom:"
    number_player, start_player1 = 0, False
    name_player1, name_player2 = "", ""

    while number_player != 1 and number_player != 2:
        try:
            number_player = int(input("Vous souhaitez jouer contre l'ordinateur (1) ou votre ami (2) ? [1/2]:"))
        except ValueError:
            print("Erreur de saisie.")

    name_player1 = input(f"Joueur 1: {SAY_YOUR_NAME}")
    if number_player == 2:
        name_player2 = input(f"Joueur 2: {SAY_YOUR_NAME}")

    check_player1_start = ""

    while check_player1_start != 'y' and check_player1_start != 'n':
        try:
            check_player1_start = input(f"Est-ce que c'est {name_player1} qui commence ? [y/n] ")
        except ValueError:
            print("Erreur de saisie.")

    return frozenset([name_player1, name_player2, start_player1, check_player1_start == 'y'])


if __name__ == "__main__":
    NIMS_NUMBER = 21
    before_start_game()
    show_nims(init_nims(NIMS_NUMBER))
