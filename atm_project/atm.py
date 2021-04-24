import datetime

import dataclasses

import random


def init():
    print('Welcome to Bank Zuri')
    print('Thank you for choosing to bank with us')
    now = datetime.datetime.now()
    print('Current date and time: ')
    print(now.strftime('%d-%m-%Y %H:%M:%S'))
init()
have_account = int(input("Do you have an account with us? 1. YES 2. NO \n"))


def withdrawal_operation():
    withdrawal_amount = int(input('How much would you like to withdraw? \n'))
    print('Please wait while your transaction is processing')
    print('Please take your cash')
    withdrawal_option = int(input('Would you like to perform another function? 1. Yes 2. No \n'))
    if withdrawal_option == 1:
        login()
    elif withdrawal_amount == 2:
        exit()
    else:
        print('Invalid option selected')

    withdrawal_operation()


def deposit_operation():

    userDetails = ['aminat', 'olayinka', 'olayinkaaminat6@gmail.com', 1000]

    deposit_amount = int(input("How much will you like to deposit? \n"))
    print('Processing Cash Deposit')

    balance = (userDetails[3] + int(deposit_amount))

    print('Your balance is %d' %balance)
    bank_operation()

def complaints_operation():
    print('How can we help you today?')
    complaint = input('Please Enter your complaint. \n')
    print('you will be attended to')
    print('Thank you for trusting us')
    another_action = int(input('Would you like to perform another action? 1. Yes 2. No \n'))
    if another_action == 1:
       bank_operation()
    elif another_action == 2:
        print('Thank you for banking with us')
        exit()
    else:
        print('Invalid selection')
        complaints_operation()

def bank_operation():
    print('**********Welcome**********')

    operations = int(input('What Operation would you like to perform? 1. Withdrawal 2. Cash Deposit 3. Complaints 4. exit \n'))

    if operations == 1:
        withdrawal_operation()

    elif operations == 2:

        deposit_operation()
    elif operations == 3:

        complaints_operation()

    elif operations == 4:
            exit()

    else:
        print('You selected an invalid option')

        bank_operation()

def login():
    print('Welcome back, Please Login here.')
    loginAccountNumber = int(input('Enter Account Number \n'))
    Password = input('Enter Password \n')

    bank_operation()

def register():
    print('***Register***')
    email = input('What is your email address \n')
    firstName = input('What is your first name \n')
    lastName = input('What is your last name \n')
    password = input('Create your password \n')
    print('Your account has been Created')

    try:

        account_number = generateAccountNumber()

    except ValueError:

        print('Account validation failed')
        init()

    user = [email, firstName, lastName, password, account_number]

    print('Your account number is %d' % account_number)
    print("Please keep it safe")
    print('----------------------------------')

    login()

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

if have_account == 1:
        login()

elif have_account == 2:
    register()

else:
    print('Invalid option selected')

init()