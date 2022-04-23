class User:
     
        myUser = []

        def __init__(self,username,password):
             self.username = username
             self.password = password

        def save_user(self):
             User.myUser.append(self)

        def delete_user(self):
             User.myUser.remove(self)

        @classmethod
        def find_by_username(cls, username):
              for user in cls.myUser:
                 if user.username == username:
                    return user

  