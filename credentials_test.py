import unittest
from credentials import Credentials

class testCredentials(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.newCredentials = Credentials("Twitter","Martin", "Martin123") # create contact object
    def tearDown(self):
        '''
        tearDown does cleanup after every test case has run
        '''
        Credentials.myCredentials = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.newCredentials.app_name,"Twitter")
        self.assertEqual(self.newCredentials.app_username,"Martin")
        self.assertEqual(self.newCredentials.app_password,"Martin123")

    def test_delete_logins(self):
            '''
            test_delete_logins to test if we can remove a login from our login list
            '''
            self.newCredentials.save_credentials()
            test_cresentials = Credentials("Twitter","Martin","Martin123") # new credential

    def test_save_credentials(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.newCredentials.save_credentials() # saving the new user
        self.assertEqual(len(Credentials.myCredentials),1)



if __name__ ==  '__main__':
    unittest.main()