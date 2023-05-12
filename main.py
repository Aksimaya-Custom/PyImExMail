# Copyright (c) 2023, Kuronekosan
# This version is still alpha-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

import os
import sys
import time
import platform
import argparse
from getpass import getpass
from func.MboxReader import MboxReader
from func.ImapClient import ImapClient
from func.ProgressBar import progressBar

# Version of this program
__version__ = "1.3.2"
#Check if the system have python > 3.7
if sys.version_info < (3, 7):
    print("This program requires Python 3.7 or later.")
    sys.exit(1)

def arguments_and_validation():
    msg = "Export Import E-Mail with Python."
 
    # Initialize parser
    parser = argparse.ArgumentParser(description = msg)

    # Adding optional argument
    parser.add_argument("-d", "--Data", help = "Select Mbox Data", required=True)
    parser.add_argument("-ho", "--Host", help = "Define the IMAP Host", required=True)
    parser.add_argument("-u", "--User", help = "Define the IMAP Username", required=True)
    parser.add_argument("-s", "--ssl", help = "Use SSL for connection (Optional)", action='store_true')
    parser.add_argument("-p", "--Port", help = "Define the IMAP Port (Optional)")
    args = parser.parse_args()

    password = getpass()
    data = args.Data
    host = args.Host
    user = args.User
    ssl = args.ssl if args.ssl else False
    port = args.Port if args.Port else 993 if ssl else 143
    port = int(port)

    if os.path.exists(data) is False:
        print("Data is not found.")
        sys.exit(1)

    if data.lower().endswith('.mbox') is False:
        print("Data is not MBOX format.")
        sys.exit(1)

    return data, host, user, password, ssl, port

def main(data, host, user, password, port, ssl):
    ujank = ImapClient(host, user, password, port, True, ssl)
    ujank.login()
    mboxReader = MboxReader(data)
    print("Now i'll import the MBOX to server, please take a seat and have a good coffee :)")
    with mboxReader as mbox:
        for mbox in progressBar(list(mbox), suffix = 'Complete', length=50):
            ujank.create_folder("Uncategorized" if mbox['X-Gmail-Labels'] is None else mbox['X-Gmail-Labels'].split(',')[0], True)
            ujank.select_folder("Uncategorized" if mbox['X-Gmail-Labels'] is None else mbox['X-Gmail-Labels'].split(',')[0])
            dateParse = mboxReader.parse_date(mbox['Date'])
            ujank.append_message(mbox.as_bytes().decode(encoding='UTF-8'), dateParse, True)
    print("Email Successfully Imported...")
    sys.exit(0)


if __name__ == "__main__":
    # Main Execute
    if platform.system() == 'Windows':
        clear = lambda: os.system('cls')
        clear()
    elif platform.system() == 'Linux':
        clear = lambda: os.system('clear')
        clear()
    else:
        print("OS not Recognized by Program, exiting...")
        time.sleep(1)
        sys.exit(1)

    print("PyImExMail Upload (v{})\nCopyright (c) 2023, Kuronekosan.\nThis version is still alpha-release\nCheck the github for the project https://github.com/SandyMaull/PyImExMail\n".format(__version__))
    data = arguments_and_validation()
    result = main(data[0], data[1], data[2], data[3], data[5], data[4])
    sys.stdout.flush()
    sys.exit(result)