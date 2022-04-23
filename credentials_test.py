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

if __name__ ==  '__main__':
    unittest.main()
