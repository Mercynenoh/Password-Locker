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
