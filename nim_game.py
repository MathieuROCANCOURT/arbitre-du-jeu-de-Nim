#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init_nims(nims_number):
    return [True for _ in range(nims_number)]


def show_nims(board):
    print('|' + ''.join(['o|' if nim else ' |' for nim in board]))


if __name__ == "__main__":
    NIMS_NUMBER = 21
    show_nims(init_nims(NIMS_NUMBER))
