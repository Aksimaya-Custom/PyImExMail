# Copyright (c) 2023, Kuronekosan
# This version is still pre-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

import os
import sys
import time
import platform
from func.MboxReader import MboxReader
from func.ImapClient import ImapClient

# Version of this program
__version__ = "1.0.0"
#Check if the system have python > 3.7
if sys.version_info < (3, 7):
    print("This program requires Python 3.7 or later.")
    sys.exit(1)

def check_platform():
    return "Windows" if platform.system() == "Windows" else "Linux" if platform.system() == "Windows" else "Unknown"


def main():
    ujank = ImapClient(os.getenv('IMAP_HOST'), os.getenv('IMAP_USERNAME'), os.getenv('IMAP_PASSWORD'), os.getenv('IMAP_PORT'), True, True)
    ujank.login()
    mboxReader = MboxReader('second.mbox')
    with mboxReader as mbox:
        for message in mbox:
            # print(message['X-Gmail-Labels'].split(',')[0] + "\n")
            # print(message['Date'] + "\n")
            # print(message.as_string() + "\n\n")
            ujank.create_folder(message['X-Gmail-Labels'].split(',')[0], True)
            ujank.select_folder(message['X-Gmail-Labels'].split(',')[0])
            dateParse = mboxReader.parse_date(message['Date'])
            ujank.append_message(message.as_string(), dateParse, True)






if __name__ == "__main__":
    # Main Execute
    if check_platform() == 'Windows':
        clear = lambda: os.system('cls')
        clear()
    elif check_platform() == 'Linux':
        clear = lambda: os.system('clear')
        clear()
    else:
        print("OS not Recognized by Program, exiting...")
        time.sleep(1)
        sys.exit(1)

    print("PyImExMail Upload (v{})".format(__version__))
    result = main()
    sys.stdout.flush()
    sys.exit(result)