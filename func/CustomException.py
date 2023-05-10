from imapclient import exceptions

class HostError(Exception):
    def __init__(self):            
        # Call the base class constructor with the parameters it needs
        message = "Hostname Tidak Dapat Ditemukan, Check Kembali Hostname."
        super().__init__(message)

class PortError(Exception):
    def __init__(self):            
        # Call the base class constructor with the parameters it needs
        message = "Port Tidak Dapat Diakses, Check Kembali Port."
        super().__init__(message)

class LoginFailed(Exception):
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        message = "Login Gagal, Check Kembali Username & Password."
        super().__init__(message)