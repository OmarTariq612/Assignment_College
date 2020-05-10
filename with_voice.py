import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)


def speech(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


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
        if seatNumber <= 64:
            # calculating the remainder
            remainder = seatNumber % 4

            if remainder == 0 or remainder == 1:
                speech(f"Your seat number is {seatNumber} , you are beside a window")
            else:
                speech(f"Your seat number is {seatNumber} , you are not beside a window")
        else:
            speech('Enter a valid seat number at maximum 64 for the second class')

    elif ticketType == 1:  # else if
        # making sure that the user hasn't entered an invalid seat number
        if seatNumber <= 47:
            # calculating the remainder
            remainder = seatNumber % 3

            if remainder == 0 or remainder == 1 or seatNumber == 47:
                speech(f"Your seat number is {seatNumber} , you are beside a window")

            else:
                speech(f"Your seat number is {seatNumber} , you are not beside a window")

        else:
            speech('Enter a valid seat number at maximum 47 for the first class')

    else:
        speech('please enter a valid ticket type (1/2) only')

else:
    speech("Please enter valid values")
