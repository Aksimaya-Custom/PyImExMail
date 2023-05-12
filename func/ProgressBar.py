# Copyright (c) 2023, Kuronekosan
# This version is still alpha-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

import time

# Generator for Progress Bar
def progressBar(iterable, suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    # Thx for the info, i learn a lot about generator and iterator
    # Love you guys from stackoverflow.
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar(iteration, name):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{name[:7] if len(name) > 7 else name} |{bar}| {percent}% {suffix}', end = printEnd, flush=True)

    # Initial Call
    printProgressBar(0, '')
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1, item['Subject'])
    # Print New Line on Complete
    print()