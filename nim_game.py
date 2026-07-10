#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init_nims(nims_number):
    return [True for _ in range(nims_number)]


def show_nims(board):
    print('|' + ''.join(['o|' if nim else ' |' for nim in board]))


def before_start_game():
    print("Bienvenue dans le jeu de Nim.")
    number_player = 0
    name_player1, name_player2 = "", ""
    say_your_name = "Saisissez votre nom:"

    while number_player != 1 and number_player != 2:
        try:
            number_player = int(input("Vous souhaitez jouer contre l'ordinateur (1) ou votre ami (2) ? (1/2):"))
        except ValueError:
            print("Saisie non correcte")

    if number_player == 1:
        name_player1 = input(say_your_name)
        return name_player1, name_player2, True

    name_player1 = input(f"Joueur 1: {say_your_name}")
    name_player2 = input(f"Joueur 2: {say_your_name}")
    return name_player1, name_player2, False


if __name__ == "__main__":
    NIMS_NUMBER = 21
    before_start_game()
    show_nims(init_nims(NIMS_NUMBER))
