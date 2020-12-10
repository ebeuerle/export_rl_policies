# -*- coding: utf-8 -*-
import csv

class CsvWriter(object):
    @staticmethod
    def write(output):
        filename = "output.csv"
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerows(output)

    @staticmethod
    def append(output):
        filename = "output.csv"
        with open(filename, "a") as f:
            writer = csv.writer(f)
            writer.writerows(output)
