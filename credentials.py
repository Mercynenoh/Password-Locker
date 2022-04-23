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
