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

def find_user(username, password):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_username(username, password)

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
    return newCredentials

def save_credentials(credentials):
    '''
    Function to save user
    '''
    credentials.save_credentials()

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
                print("Use these short codes for navigation: \n ca - Create Account \n li - Log In ")
               
                

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
                   
                    print(f"New User {username}  has been created\n proceed to log in")
                    continue
                          
                   

                elif my_input =="LI":
                    print('Log in to your account')
                    print('-'*10)
                    print("Enter your username")
                    username = input().strip(' ')
                    print("Enter your password")
                    password = input().strip(' ')
                    if find_user(username, password):
                        print("Welcome back")
                    else:
                        print('Ooops! Cannot find account.')
                
                else:
                    print('You have entered the wrong navigation short-cut')
                    continue
                       
   
                if find_user(username, password):  
                    print("\nUse these short codes to create new credentials: \n CC: create new credentials \n FC: find a credential \n DC: delete a credential \n SC: see all credentials \n LO: log out")
                     
                my_credentials = input().upper()

                if my_credentials == "CC":
                    print('PLease Enter new credentials\n')
                    
                    print("Application name e.g facebook")
                    app_name = input()

                    print ('Application username')
                    app_username = input()

                    print(f"\nDo you already have a password for your account on {app_name}? (Y/N)")
                    has_password = input().upper()
                    if has_password == 'Y':
                    print(f"Enter your {app_name} password")
                    app_password = input()

                    save_credentials(create_credentials(app_name, app_username, app_password))
                    
                    print(f"New Credentials for \n appname:{app_name} \n username:{app_username} \npassword:{app_password}  have been created")
                    break
                # elif has_password == 'N':
               
                #     print("Would you like a system generated password? (T/F)")
                #     gen_pass = input().upper()
                # if gen_pass == 'T':
     
                #     passwordLength = int(10)
                
                                     
                #     account_password = generate_a_password 
                #     print(f"Password generated is {account_password}")  
                #     save_credentials(create_credentials(app_name, app_username, account_password))
                #     print(f"Account credentials for your {app_name} account have been successfully saved.\n") 
                #     continue 
                #     break  
                # elif my_credentials== "FC":
                #     print('Enter the application you\'d like to find')
                #     search_app = input()
                # if login_exist(search_app):
                #     search_credential = login_exists(search_app)
                #     print(f"\nApplication name: {search_credential.app_name}, \n username: {search_credential.aapp_username} \n password: {search_credential.account_password}")

                # else:
                #     print(f"\nThe credentials for {searched_application} don't exist.")

                # if my_credentials== 'DC':
                #     print("Application name:")
                #     print(" "*4 + "*eg. Instagram/Tinder*")
                #       app_name = input().capitalize()
                            
                # if login_exits(app_name):
                #     delete_logins(delete_logins(app_name))
                #     print(f"\nCredentials for {app_name} have been successfully deleted")

                
                # if my_credentials== 'DA':
                #     print("Enter your username")
                #     username = input().capitalize()
                #     print("Enter your password")
                #     login_password = input()

                # if user_exists(username, login_password):
                #     delete_user(find_by_number(username))
                #     print(f"\nYour account has been successfully deleted.\n")





                # if my_credentials == "LO":
                #     print("It's sad to see you leave, come back again")
                    
                #     break
                # else:
                #     print("I really didn't get that. Please use the short codes")                                                        
                    
                    

                

                # if my_credentials == "FC":
                #     print("Enter the appname you want to search for")

                #     search_name = input()
                # if check_existing_names(search_name):
                #     search_name = find_by_app_name(search_name)
                #     print(f"{search_name.app_name}")
                #     print('-' * 20)

                #     print(f"username.......{search_name.app_name}")
                #     print(f"Email address.......{search_name.app_password}")
                # else:
                #     print("That account does not exist")
                #     break


                




                    


if __name__ == '__main__':
    main()


