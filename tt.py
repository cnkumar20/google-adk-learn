from tastytrade_api.authentication import TastytradeAuth
from tastytrade_api.account.account_handler import TastytradeAccount
from tastytrade_api.account.balances_positions import TastytradeAccountPositions
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('ACCOUNT', 'username')
password = config.get('ACCOUNT', 'password')


# Initialize the authentication object
auth = TastytradeAuth(username, password)

# Log in to the API
auth_data = auth.login()
print("Session token:", auth.session_token)

account = TastytradeAccount(auth.session_token, "https://api.tastytrade.com")
accounts = account.get_accounts()
position = TastytradeAccountPositions(auth.session_token, "https://api.tastytrade.com")

acc_num = accounts[0]["account"]["account-number"]
print(f"BALANCE: {position.get_account_balances(acc_num)}")
#print(accounts)
"""
if auth_data:
    print("Successfully logged in!")
else:
    print("Failed to log in.")

# Validate the session
is_valid = auth.validate_session()

if is_valid:
    print("Session is valid.")
else:
    print("Session is invalid or expired.")

# Destroy the session (log out)
if auth.destroy_session():
    print("Successfully logged out.")
else:
    print("Failed to log out.")
"""
