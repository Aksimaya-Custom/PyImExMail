# Copyright (c) 2023, Kuronekosan
# This version is still alpha-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

import os
import email
import datetime
from email.policy import default

class MboxReader:
    def __init__(self, filename):
        self.handle = open(filename, 'rb')
        assert self.handle.readline().startswith(b'From ')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.handle.close()

    def __iter__(self):
        return iter(self.__next__())

    def __next__(self):
        lines = []
        while True:
            line = self.handle.readline()
            if line == b'' or line.startswith(b'From '):
                yield email.message_from_bytes(b''.join(lines), policy=default)
                if line == b'':
                    break
                lines = []
                continue
            lines.append(line)

    def parse_date(self, date):
        response = email.utils.parsedate_to_datetime(date)
        return response