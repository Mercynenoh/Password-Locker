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

    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.newUser.save_user() # saving the new contact
        self.assertEqual(len(User.myUser),1)

if __name__ ==  '__main__':
    unittest.main()
