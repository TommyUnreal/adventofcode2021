import os
from typing import Match
import numpy

class BingoChart():
    numbers  = []
    unmarked = []
    bingo    = False

    def __init__(self, numbers) -> None:
        self.numbers  = numbers
        self.unmarked = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
    
    def mark_number(self, num) -> None:
        for row in range(5):
            for col in range(5):
                if self.numbers[row][col] == num:
                    self.unmarked[row][col] = 0
                    return
    
    def check_bingo(self) -> bool:
        returnval = False
        for row in self.unmarked:
            if all(i < 1 for i in row):
                self.bingo = True
                return True
        for col in numpy.transpose(self.unmarked):
            if all(i < 1 for i in col):
                self.bingo = True
                return True
        return False

    def get_sum_of_masked_numbers(self) -> list:
        flattened_numbers  = list(numpy.concatenate(self.numbers).flat)
        flattened_unmarked = list(numpy.concatenate(self.unmarked).flat)
        print(flattened_numbers, flattened_unmarked)
        return sum([flattened_numbers[i] * flattened_unmarked[i] for i in range(25)])

def print_result():
    global drawn_numbers
    global bingo_charts
    for num in drawn_numbers:

        if len(bingo_charts) == 1:
            bingo_charts[0].mark_number(num)
            print(bingo_charts[0].get_sum_of_masked_numbers()*num)
            return

        print(num)
        for chart in bingo_charts:
            chart.mark_number(num)
            chart.check_bingo()
        bingo_charts = [chart for chart in bingo_charts if not chart.bingo]



__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

drawn_numbers = []
bingo_charts  = []

with open(os.path.join(__location__,"input.txt")) as file:
    drawn_numbers = list(map(int, file.readline().strip().split(",")))
    file.readline() #empty line
    while True:
        chart_list = []
        for i in range(5):
            chart_list.append(list(map(int, file.readline().strip().split())))
        bingo_charts.append(BingoChart(chart_list))
        if not file.readline():
            break

print_result()

