# Copyright (c) 2023, Kuronekosan
# This version is still alpha-release
# Check the github for the project https://github.com/SandyMaull/PyImExMail

from imapclient import exceptions

class HostError(Exception):
    def __init__(self):            
        message = "Hostname Not Found, Check Hostname Configuration."
        super().__init__(message)

class PortError(Exception):
    def __init__(self):            
        message = "Port Can't Access, Check Port Configuration."
        super().__init__(message)

class LoginFailed(Exception):
    def __init__(self, message):            
        message = "Login Failed, Check Username & Password Configuration."
        super().__init__(message)

class Timeout(Exception):
    def __init__(self):            
        message = "Connection Timeout, Check Your Connection."
        super().__init__(message)