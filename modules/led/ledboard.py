#!/usr/bin/env python3
"""
    Interface for our led boards for further usage, using nested lists.
    Board includes rows. Rows include pixels. Cols also include pixels.
"""
import neopixel

# CONFIGURATION
ORDER_RGB = neopixel.GRB
GPIO_PIN = neopixel.D18
LUMINOSITY = 0.6

BOARDS_X, BOARDS_Y = 2, 1
SIZE_X, SIZE_Y = 8, 8


class Field(list):
    def _init__(self):
        self.board_quant = BOARDS_X, boards_Y
        self.color_conf = ORDER_RGB, GPIO_PIN, LUMINOSITY

        self.board_rows = []

        for ttb in range(BOARDS_Y):
            new_row = []
            for ltr in range(BOARDS_X):
                new_board = Board(field=self, board_i=ltr, board_j=ttb)
                self.new_row.append(new_board)
            self.board_rows.append(new_row)

        super().__init__(self.board_rows)

class Board(list):
    def __init__(self, field, board_i, board_j):
        self.hwboard = field
        self.pos_x = board_i
        self.pos_y = board_j

    def __str__(self):
        return "<" + str(self.hwboard) + ":" + str(self.pos_x) + "," +\
                str(self.pos_y) + ">"
