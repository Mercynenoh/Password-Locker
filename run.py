#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_user(username,password):
    '''
    Function to create a new user
    '''
    newUser = User(username,password)
    return newUser

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete a contact
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_username(username)

def display_user():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()

def create_credentials(app_name, app_username, app_password):
    '''
    Function to create a new account
    '''
    newCredentials = Credentials(app_name, app_username, app_password)
    return myCredentials

def save_credentials(credentials):
    '''
    Function to save user
    '''
    newCredentials.save_credentials()

def delete_logins(newCredentials):
    '''
    Function to delete a contact
    '''
    newCredentials.delete_logins()

def find_by_app_name(app_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_by_app_name(app_name)

def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()

def generate_a_password(passwordLength):
    '''
    Function that generates random password of 8 characters
    '''
    return Credentials.generate_password(passwordLength)

def main():
    print('*'*10 + "Hey, Welcome" + '*'*10)
    print('--'*22)
    print('Have you been having a problem remembering your passwords?\n Worry no more, You can manage your passwords here')
    print('--'*22)
    current_user= input ('What is your name?\n')
    print(f'\n Hello {current_user},')
    while True:
                print("Use these short codes for navigation: \n CA - Create Account \n LO - Log In \n DA - Delete your account \n EX - Exit ")

                my_input = input().upper()

                if my_input == 'CA':
                    print('\n CREATE YOUR ACCOUNT')
                    print('-'*10)

                    print('Please enter your desired Username:\n')
                    username = input()

                    # print(" "*4 + "*the username contains alphabetical letters only and no spaces*")
                    

                    print(' Please enter your password\n')
                    password = input()

                    save_user(create_user(username, password))
                   
                    print(f"New User {username}  has been created")
                    

                if my_input =="LO":
                    print("Already have an account? Sign in\n")
                    print("-"*10)

                    print("Enter your username")
                    username = input().strip(' ').capitalize()
                    print("Enter your password")
                    password = input().strip(' ')

                    print("What would you like to do?")
                else:
                
                    print("\nUse these short codes to create new credentials: \n CC: create new credentials \n FC: find a credential \n DC: delete a credential \n SC: see all credentials \n LO: log out")
                     
                     my_credentials = input().upper()

                if my_credentials = "CC"
                print('')
                if 




                    


if __name__ == '__main__':
    main()


