import os
import copy
from typing import Match

def to_char_bite(s):
    """Return string value of 0/1 of bolean type."""
    match s:
        case True:
            return "1"
        case False:
            return "0"

def count_active_bytes(diagnostic_report):
    """Return list of occurancies of active bites in list of records. 
    
    Array size is cumputed from len of first record. F.e. 8 for '00011010'.
    """
    tmp_active_bites = []
    for line in diagnostic_report:
        if not tmp_active_bites:
            tmp_active_bites = [0] * len(line)
        for i in range(len(line)):
            if line[i] == "1":
                tmp_active_bites[i] += 1

    return tmp_active_bites

def filter_records(diagnostic_report, key):
    """Filter diagnostic_report by key.

    If key is 'keep_most':
       Determine the most common value (0 or 1) in the current bit position in string record, and keep only numbers with that bit in that position.
    If key is 'keep_least':
       Determine the least common value (0 or 1) in the current bit position in string record, and keep only numbers with that bit in that position.
    """
    global n_of_lines
    global active_bites
    tmp_active_bites = copy.deepcopy(active_bites)
    for a in range(len(tmp_active_bites)):
        match key:
            case "keep_most":
                tmp_active_bites  = count_active_bytes(diagnostic_report)
                diagnostic_report = [r for r in diagnostic_report if r[a] == to_char_bite(tmp_active_bites[a] >= len(diagnostic_report) / 2)]
            case "keep_least":
                tmp_active_bites  = count_active_bytes(diagnostic_report)
                diagnostic_report = [r for r in diagnostic_report if r[a] == to_char_bite(tmp_active_bites[a] < len(diagnostic_report) / 2)]
        if len(diagnostic_report) == 1:
            break
        
    return diagnostic_report[0]

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

n_of_lines        = -1
active_bites      = []
diagnostic_report = []

with open(os.path.join(__location__,"input.txt")) as file:
    line = "0"
    while line:
        line = file.readline().strip()
        if line:
            diagnostic_report.append(line)
        #initialize
        if not active_bites:
            active_bites = [0] * len(line)
        for i in range(len(line)):
            if line[i] == "1":
                active_bites[i] += 1
        n_of_lines += 1

oxygen_generator_rating = int(filter_records(diagnostic_report, "keep_most"), 2)
co2_scrubber_rating     = int(filter_records(diagnostic_report, "keep_least"), 2)

print(oxygen_generator_rating*co2_scrubber_rating, oxygen_generator_rating, co2_scrubber_rating)