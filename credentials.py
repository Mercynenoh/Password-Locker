import random
import string

class Credentials:

    myCredentials =[]

    def __init__(self,app_name,app_username,app_password):
        
        self.app_name = app_name
        self.app_username = app_username
        self. app_password = app_password

    def save_credentials(self):
              Credentials.myCredentials.append(self)


    def delete_logins(self):
             Credentials.myCredentials.remove(self)

    @classmethod
    def find_by_app_name(cls, app_name):
            for credentials in cls.myCredentials:
                if credentials.app_name == app_name:
                    return credentials

    @classmethod
    def login_exists(cls,app_name,app_username,app_password):
        '''
        method checks if login exits from the credential list
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for login in cls.myCredentials:
            if login.app_name == app_name and login.app_username == app_username and login.app_password == app_password:
                return True
        return False

    @classmethod
    def display_credentials(cls):
                return cls.myCredentials

    @staticmethod
    def generate_password(passwordLength):
        '''
        method that generates a random password for the user
        '''
        random_alphanumeric = string.ascii_letters + string.digits
        password = ''.join((random.choice(random_alphanumeric) for i in range(passwordLength)))
        return password
