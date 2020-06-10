"""
This program is a part of a project in the Faculty of Engineering at Minia Universiy.
Author : Omar Tariq Abd El-Raziq
Prof. : Dr. Hassan A. Alansary
Department : Systems and Computers Engineering
"""

# Having the ticket type from the user
ticketType = input('Enter your ticket type (1/2) : ')
# Having the seat number from the user
seatNumber = input('Enter your seat number : ')

# Checking if the user has entered numeric values or not
if ticketType.isnumeric() and seatNumber.isnumeric():
    # changing the data type of the variables (from str to int)
    ticketType = int(ticketType)
    seatNumber = int(seatNumber)

    if ticketType == 2:
        # making sure that the user hasn't entered an invalid seat number
        if 0 < seatNumber <= 64:
            # calculating the remainder
            remainder = seatNumber % 4

            if remainder == 0 or remainder == 1:
                print(f"Your seat number is {seatNumber} , you are beside a window")
            else:
                print(f"Your seat number is {seatNumber} , you are not beside a window")
        else:
            print('Enter a valid seat number (at max 64)')

    elif ticketType == 1:  # else if
        # making sure that the user hasn't entered an invalid seat number
        if 0 < seatNumber <= 47:
            # calculating the remainder
            remainder = seatNumber % 3

            if remainder == 0 or remainder == 1 or seatNumber == 47:
                print(f"Your seat number is {seatNumber} , you are beside a window")
            else:
                print(f"Your seat number is {seatNumber} , you are not beside a window")

        else:
            print('Enter a valid seat number (at max 47)')

    else:
        print('please enter a valid ticket type (1/2) only')

else:
    print('Please enter valid values')
