# src/my_package/your_module.py
import pyotp
class APIKey:
    def __init__(self, key):
        self.key = key

    def get_api(self):
        # Thực hiện các tác vụ của bạn
        print(self.key)

class Otp:
    def __init__(self, key):
        self.key = key

    def get_otp(self):
        # Thực hiện các tác vụ của bạn
        topt = pyotp.TOTP(self.key)
        print(topt.now())