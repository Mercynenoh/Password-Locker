class User:
     
        myUser = []

        def __init__(self,username,password):
             self.username = username
             self.password = password

        def save_user(self):
             User.myUser.append(self)

  