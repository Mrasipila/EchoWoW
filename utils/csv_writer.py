# Writer for the keyboard and mouse recorded (the screen recorder being main/master handled by opencv)
from recorder.abstract_recorder import Recorder
import csv
import datetime


class CsvWriter:

    def __init__(self, recorders: list[Recorder]):
        self.recorders = recorders

        # filenames
        self.filename_kb = open('csvfiles/keyboard_data.csv', 'w+')
        self.filename_ms_click = open('csvfiles/mouse_click_data.csv', 'w+')
        self.filename_ms_scroll = open('csvfiles/mouse_scroll_data.csv', 'w+')
        self.filename_ms_move = open('csvfiles/mouse_move_data.csv', 'w+')

        # writers
        self.keyboard_wr = csv.writer(self.filename_kb, delimiter=' ')
        self.mouse_wr_click = csv.writer(self.filename_ms_click, delimiter=' ')
        self.mouse_wr_scroll = csv.writer(self.filename_ms_scroll, delimiter=' ')
        self.mouse_wr_move = csv.writer(self.filename_ms_move, delimiter=' ')

    # save keyboards data
    def save_keyboard_data(self):
        e = self.recorders[0]
        for data, date in e.data:
            self.keyboard_wr.writerow(str(data) + ";" + str(date))
        # closing filename
        self.filename_kb.close()

    # save mouse data
    def save_mouse_data(self):
        e = self.recorders[1]
        for x, y, pressed, button, date in e.data_click:
            self.mouse_wr_click.writerow(str(x) + ";" + str(y) + ";" + str(pressed) + ";" + str(button) + ";" + str(date))
        for scroll, date in e.data_scroll:
            self.mouse_wr_scroll.writerow(str(scroll) + ";" + str(date))
        for x, y, date in e.data_move:
            self.mouse_wr_move.writerow(str(x) + ";" + str(y) + ";" + str(date))
        # closing filename
        self.filename_ms_click.close()
        self.filename_ms_scroll.close()
        self.filename_ms_move.close()