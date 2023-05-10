# Copyright (c) 2023, Kuronekosan
# This version is still pre-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

import os
import sys
import socket
import imapclient
from imapclient import IMAPClient
from func import CustomException
from dotenv import load_dotenv

# Version of this program
__version__ = "1.0.0"
#Check if the system have python > 3.7
if sys.version_info < (3, 7):
    print("This program requires Python 3.7 or later.")
    sys.exit(1)
#Load .env File
load_dotenv()
# Custom Error Message
imapclient.exceptions.LoginError = CustomException.LoginFailed

class ImapClient:
    def __init__(self, hostname:str, username:str, password:str, port:int, use_uidStatus:bool, ssl:bool):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.use_uidStatus = use_uidStatus
        self.ssl = ssl

    def main(self):
        try:
            imapInit = IMAPClient(host = self.hostname, port = self.port, use_uid = self.use_uidStatus, ssl = self.ssl, timeout = 15)
            login = imapInit.login(username = self.username, password = self.password)
            print("Login Success.")
        except ConnectionResetError:
            raise CustomException.PortError
        except socket.gaierror:
            raise CustomException.HostError

ujank = ImapClient(os.getenv('IMAP_HOST'), os.getenv('IMAP_USERNAME'), os.getenv('IMAP_PASSWORD'), os.getenv('IMAP_PORT'), True, True)
ujank.main()