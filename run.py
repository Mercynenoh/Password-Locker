#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_user(username,password):
    '''
    Function to create a new user
    '''
    newUser = User(username,password)
    return myUser

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


