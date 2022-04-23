import unittest
from user import User

class testUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.newUser = User("Mercy","Mercy123") # create contact object
    def tearDown(self):
        '''
        tearDown does cleanup after every test case has run
        '''
        User.myUser = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.newUser.username,"Mercy")
        self.assertEqual(self.newUser.password,"Mercy123")

    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.newUser.save_user()
            test_user = User("Joe","Joe123") # new user

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.newUser.save_user() # saving the new user
        self.assertEqual(len(User.myUser),1)

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple users
            objects to our contact_list
            '''
            self.newUser.save_user()
            test_user = User("Joe", "Joe123") # new contact
            test_user.save_user()
            self.assertEqual(len(User.myUser),2)
    
    def test_find_user_by_username(self):

        self.newUser.save_user()
        test_user = User("Joe", "Joe123")
        test_user.save_user()

        found_user = User.find_by_username("Joe")
        self.assertEqual(found_user.password,test_user.password)

    def test_user_exists(self):
        self.newUser.save_user()
        test_user = User("Joe","Joe123")
        test_user.save_user()
        user_exists = User.user_exist("Joe")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        self.assertEqual(User.display_users(), User.myUser)

    
    

if __name__ ==  '__main__':
    unittest.main()
