# Copyright (c) 2023, Kuronekosan
# This version is still alpha-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

import os
import socket
#FK U IMAPLIB.
import imaplib
import imapclient
from imapclient import IMAPClient
from func import CustomException

# Custom Error Message
imapclient.exceptions.LoginError = CustomException.LoginFailed

class ImapClient:
    def __init__(self, hostname:str, username:str, password:str, port:int = 993, use_uidStatus:bool = True, ssl:bool = True):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.use_uidStatus = use_uidStatus
        self.ssl = ssl
        self.imap = None
        #FK U CPANEL.
        self.cpanel = False
        self.backFolderName = "Imported by PyImExMail"
        self.isOnFolder = []

    def login(self):
        try:
            imapInit = IMAPClient(host = self.hostname, port = self.port, use_uid = self.use_uidStatus, ssl = self.ssl, timeout = 15)
            imapInit.login(username = self.username, password = self.password)
            print("Login Success.")
            self.imap = imapInit

            return self.imap
        except ConnectionResetError:
            raise CustomException.PortError
        except socket.gaierror:
            raise CustomException.HostError
        except TimeoutError:
            raise CustomException.Timeout
        except ConnectionRefusedError:
            raise CustomException.PortError

    def get_list_folders(self):
        response = self.imap.list_folders()
        response = [tup[2] for tup in response]

        # THIS TRY & EXCEPT FIXING THE STUPIDITY OF CPANEL.
        try:
            if self.backFolderName not in response:
                self.imap.create_folder(self.backFolderName)
        except imaplib.IMAP4.error:
            if ('INBOX.' + self.backFolderName) not in response:
                self.imap.create_folder("INBOX." + self.backFolderName)
            self.cpanel = True
            if "INBOX" not in self.isOnFolder:
                self.isOnFolder.append("INBOX")

        return response

    def select_folder(self, name, resetFolderAfter = False):
        self.get_list_folders()
        if self.backFolderName not in self.isOnFolder:
            self.isOnFolder.append(self.backFolderName)
        if name not in self.isOnFolder:
            self.isOnFolder.append(name)
        response = self.imap.select_folder(".".join(self.isOnFolder))
        if resetFolderAfter:
            self.close_folder()

        return response

    def create_folder(self, name, resetFolderAfter = False):
        list_folders = self.get_list_folders()
        if self.backFolderName not in self.isOnFolder:
            self.isOnFolder.append(self.backFolderName)
        if name not in self.isOnFolder:
            self.isOnFolder.append(name)
        if ".".join(self.isOnFolder) not in list_folders:
            self.imap.create_folder(".".join(self.isOnFolder))
        response = True
        if resetFolderAfter:
            self.close_folder()

        return response

    def close_folder(self):
        self.isOnFolder = []
        if self.cpanel:
            self.isOnFolder.append('INBOX')
            self.isOnFolder.append(self.backFolderName)
        else:
            self.isOnFolder.append(self.backFolderName)

    def append_message(self, msg, time, resetFolderAfter = False):
        self.imap.append(".".join(self.isOnFolder), msg, msg_time=time)
        if resetFolderAfter:
            self.close_folder()

        return True