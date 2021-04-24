def database():
    email = input('What is your email address \n')
    firstName = input('What is your first name \n')
    lastName = input('What is your last name \n')
    password = input('Create your password \n')

    account_number = 2799300519
    userDetails = [firstName, lastName, password, account_number]


    print(type(userDetails))

    database()