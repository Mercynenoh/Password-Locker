#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_user(username,password):
    '''
    Function to create a new contact
    '''
    newUser = User(username,password)
    return newUser

def save_users(user):
    '''
    Function to save contact
    '''
   user.save_user()

def del_contact(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()
