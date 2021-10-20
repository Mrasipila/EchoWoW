# Writer for the keyboard and mouse recorded (the screen recorder being main/master handled by opencv)
from recorder.abstract_recorder import Recorder
import csv
import datetime


class CsvWriter:

    def __init__(self, recorders: list[Recorder]):
        self.recorders = recorders
        self.filename_kb = open('csvfiles/keyboard_data.csv', 'w+')
        self.filename_ms = open('csvfiles/mouse_data.csv', 'w+')
        self.keyboard_wr = csv.writer(self.filename_kb, delimiter=' ')
        self.mouse_wr = csv.writer(self.filename_ms, delimiter=' ')

    def save_keyboard_data(self):
        for e in self.recorders:
            for data, date in e.data:
                self.keyboard_wr.writerow(str(data) + ";" + str(date))
        self.filename_kb.close()
