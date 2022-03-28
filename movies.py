"""
Cinema ...
By Victor
"""
#********************************
#*        Functions             *
#********************************


#List of seats
seat_a = []

#phone number validation
def phone():
    usr_phone = ''
    while usr_phone.isnumeric() == False:
        usr_phone = input('What is your phone number? ') 

#Fucntion to book movies
def movies ():
    #list of movies
    movies = ['The Batman', 'Uncharted', 'The Lost City']
    print("Today's movies")
    print("---------------------------")
    for movie in movies:
        print(movie)
    
    #User chooses movie
    mv = ''
    while mv not in movies:
        mv = input('What movie do you want to watch? ')
    
    return mv
#Session function
def sessions ():
    #list of sessions
    sessions = ['Morning', 'Afternoon', 'Evening' ]
    print("Sessions")
    print("---------------------------")
    for session in sessions:
        print(session)
    
    #User chooses session
    ss = ''
    while ss not in sessions:
        ss = input("Please choose a session. ")
    
    return ss

#Seating function
def seats (seat_a):
 
    row_1 = ['[ 1 ]', '[ 2 ]', '[ 3 ]', '[ 4 ]', '[ 5 ]']
    for n, seat in enumerate(row_1):
        if n+1 in seat_a:
            print ('[ X ]', end='')
        else:
            print(seat, end='')
    print()
    row_2 = ['[ 6 ]', '[ 7 ]', '[ 8 ]', '[ 9 ]', '[ 10]']
    for n, seat in enumerate(row_2):
        if n+6 in seat_a:
            print ('[ X ]', end='')
        else:
            print(seat, end='')
    print()
    row_3 = ['[ 11]', '[ 12]', '[ 13]', '[ 14]', '[ 15]']
    for n, seat in enumerate(row_3):
        if n+11 in seat_a:
            print ('[ X ]', end='')
        else:
            print(seat, end='')
    print()
    print("         SCREEN")
   
    #user chooses a seat
    #While not in seats and 1-15
    while True:
        try:
            seat = ""
            seat = int (input("Enter a seat number: "))
            if seat in seat_a or seat < 1 or seat > 15:
                raise ValueError
            else:
                seat_a.append(seat)
            break
           
        except ValueError:
            print("Not a valid option.")   
#function to print the seat arrangement 
def seat_chart ():
    row_1 = ['[ 1 ]', '[ 2 ]', '[ 3 ]', '[ 4 ]', '[ 5 ]']
    for n, seat in enumerate(row_1):
        if n+1 in seat_a:
            print ('[ X ]', end='')
        else:
            print(seat, end='')
    print()
    row_2 = ['[ 6 ]', '[ 7 ]', '[ 8 ]', '[ 9 ]', '[ 10]']
    for n, seat in enumerate(row_2):
        if n+6 in seat_a:
            print ('[ X ]', end='')
        else:
            print(seat, end='')
    print()
    row_3 = ['[ 11]', '[ 12]', '[ 13]', '[ 14]', '[ 15]']
    for n, seat in enumerate(row_3):
        if n+11 in seat_a:
            print ('[ X ]', end='')
        else:
            print(seat, end='')
    print()
    print("         SCREEN")


#********************************
#*        Main program          *
#********************************

#user info verification
book_again = 'y'
while book_again == 'y':
    name = input("What is your name? ")
    print ("Hello", name)

    usr_phone= phone()

    mv = movies() 

    print (f"You have chosen {mv}")

    ss = sessions()

    print (f"You chose the {ss} session. ")

    seats(seat_a)
    print(seat_a)

    #user chooses option
    seat_chart()
    verf = ''
    while verf not in ('y','n'):
        verf = input(f'{name}, your number is {usr_phone} you have chosen to watch {mv} in the {ss} session. You chose seat {seat_a}. Is this information correct? (y/n) ')

    #verification of the information
    match verf:
        #the information is correct
        case 'y':
            print("Thank you for booking.")  
            book_again = 'n'    
        #the information is incorrect    
        case 'n':
            #user chooses to book again or not
            book_again = ''
            while book_again != 'y' or 'n':  
                book_again = input("Would you like to book again? (y/n) ")
                #the booking process restarts 
                if book_again == 'y':
                    seat_a.clear()
                    break
                #the program closes
                elif book_again == 'n':
                    print("Thanks bye!") 
                    book_again = 'n' 
                    exit()

