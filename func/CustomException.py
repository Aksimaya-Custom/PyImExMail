# Copyright (c) 2023, Kuronekosan
# This version is still pre-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

from imapclient import exceptions

class HostError(Exception):
    def __init__(self):            
        # Call the base class constructor with the parameters it needs
        message = "Hostname Not Found, Check Hostname Configuration."
        super().__init__(message)

class PortError(Exception):
    def __init__(self):            
        # Call the base class constructor with the parameters it needs
        message = "Port Can't Access, Check Port Configuration."
        super().__init__(message)

class LoginFailed(Exception):
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        message = "Login Failed, Check Username & Password Configuration."
        super().__init__(message)