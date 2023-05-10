# Copyright (c) 2023, Kuronekosan
# This version is still pre-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

from func.MboxReader import MboxReader

mboxReader = MboxReader('data.mbox')
with mboxReader as mbox:
    for message in mbox:
        # print(message.as_string() + "\n\n\n")
        # print(message['from'])
        # print(message['subject'])
        print(message['X-Gmail-Labels'].split(',')[0] + "\n\n")
        # print(message)