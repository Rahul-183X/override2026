# ---------------------------------------------------------------------------- #

#                                                                              #

# 	Module:       main.py                                                      #

# 	Author:       vaazhlik                                                     #

# 	Created:      8/12/2026, 8:51:15 AM                                        #

# 	Description:  V5 project                                                   #

#                                                                              #

# ---------------------------------------------------------------------------- #



# Library imports

# from asyncio import wait



from vex import *

import math

import random



print("2026/10/15-08:51")

# Brain should be defined by default

brain=Brain()



brain.screen.print("Hello V5")



screen_precision = 0

console_precision = 0

myVariable = 0

Days = 1

Infinaty = 0



def file_print():

    global myVariable, Days, Infinaty, screen_precision, console_precision
    #Useless Stuff and defining "Days"
    brain.screen.set_cursor(1,1)
    brain.screen.set_pen_width(10)
    print("VexCode")
    Days = 1
    #Checking if SD Card is inserted
    if brain.sdcard.is_inserted():
        with open("aug_11.csv","w") as f:
            f.write("Time,Distance\n")
            f.write("1.0,205\n")
            f.write("2.0,210\n")
    else:
        brain.screen.print("Insert SD Card!")
    # Data to save (example)
    data_to_save = "This is the data to save to the SD card."
    brain.screen.print("Days")
    # Create the filename using the timestamp
    filename = str(Days) + ".csv" #f"/{Days}.txt" 
    print("Filename: " + filename)
    # or "/usd/{timestamp}.txt" depending on the Vex Brain's file system
    print(Days)
    #sleep(10)  Wait for 10 seconds before saving the file
    # Write to the SD card
    print("Days: " + str(Days))
    try:
        with open(filename, "w") as file:
            file.write(data_to_save)
        print("File saved as:" +filename)
    except Exception as e:
        print("Error saving file: " + str(e))
    # ---------------------------------------------------------------------------- #

    # Github ython .P                                                              #

    #     Module:       main.py                                                      #

    #     Author:       vaazhlik                                                     #

    #     Created:      8/12/2026, 8:51:15 AM                                        #

    #     Description:  V5 project                                                   #

    #                                                                              #

    # ---------------------------------------------------------------------------- #



    # Library imports

    #from vex import *



    # Brain should be defined by default

    # brain=Brain()



    # brain.screen.print("Hello V5")


controller_1 = Controller(PRIMARY)
"""
def when_started2():
    global myVariable, Days, Infinaty, screen_precision, console_precision
    #Days Section Of Code
    while True:
        if controller_1.buttonDown.pressing():
            Days = Days - 1
        if controller_1.buttonUp.pressing():
            Days = Days + 1
        if Days == 32 :
            Days = 1
        if Days == 0 :
            Days = 1
        if Days < 0 :
            print("Invalid Number")
            Days = 1
        if controller_1.buttonA.pressing():
            break # Come out of the loop if button A is pressed / Stop listening to user input
        sleep(10)  # Add a small delay to avoid busy waiting
        brain.screen.print(" Current Days: " + str(Days))
        brain.screen.next_row()
        controller_1.screen.print(" Current Days: " + str(Days))
        controller_1.screen.next_row()
        # Makin
    when_started1()

# ws2 = Thread( when_started2 )


# print("Days: " + str(Days))



previous = 0
current = 0 




# Define Variables for Year, Month, Hour, Minute
Years_1 = 2
Years_2 = 0
Years_3 = 2
Years_4 = 6
Months_1 = 1
Months_2 = 0
Days_1 = 1
Days_2 = 5
Hours_1 = 1
Hours_2 = 2
Minutes_1 = 3
Minutes_2 = 0






def get_date():
    global myVariable, Days, Infinaty, screen_precision, console_precision, Years_1, Years_2, Years_3, Years_4, Months_1, Months_2, Days_1, Days_2, Hours_1, Hours_2, Minutes_1, Minutes_2
    # Start the second thread for user input
    # ws2.start()
    while True:
        # Move the cursor to different positions for left / right buttons
        if controller_1.buttonLeft.pressed:
            brain.screen.next_row
            brain.screen.print("Left Button Pressed")
            wait(1,SECONDS)  # Add a small delay to avoid busy waiting
        if controller_1.buttonRight.released:
            brain.screen.next_row()
            brain.screen.print("Right Button Pressed")
            wait(1,SECONDS)  # Add a small delay to avoid busy waiting
        # Years coulumns 
        # Years (Up / Down Buttons)
        if brain.screen.column() == 1:
            if controller_1.buttonUp.pressed:
                Years_1 = Years_1 + 1
                brain.screen.print("Years #1: " + str(Years_1))
            if controller_1.buttonDown.pressed:
                Years_1 = Years_1 - 1
                brain.screen.print("Years #1: " + str(Years_1))
        if brain.screen.column() == 2:
            if controller_1.buttonUp.pressed:
                Years_2 = Years_2 + 1
                brain.screen.print("Years #2: " + str(Years_2))
            if controller_1.buttonDown.pressed:
                Years_2 = Years_2 - 1
                brain.screen.print("Years #2: " + str(Years_2))
        if brain.screen.column() == 3:
            if controller_1.buttonUp.pressed:
                Years_3 = Years_3 + 1
                brain.screen.print("Years #3: " + str(Years_3))
            if controller_1.buttonDown.pressed:
                Years_3 = Years_3 - 1
                brain.screen.print("Years #3: " + str(Years_3))
        if brain.screen.column() == 4:
            if controller_1.buttonUp.pressed:
                Years_4 = Years_4 + 1
                brain.screen.print("Years #4: " + str(Years_4))
            if controller_1.buttonDown.pressed:
                Years_4 = Years_4 - 1
                brain.screen.print("Years #4: " + str(Years_4))
        # Years Cycle
        if Years_1 == 10:
            Years_1 = 0
        if Years_2 == 10:
            Years_2 = 0
        if Years_3 == 10:
            Years_3 = 0
        if Years_4 == 10:
            Years_4 = 0
        # Months coulumns
        # Months (Up / Down Buttons)
        if brain.screen.column() == 6:
            if controller_1.buttonUp.pressing():
                Months_1 = Months_1 + 1
                brain.screen.print("Months #1: " + str(Months_1))
            if controller_1.buttonDown.pressing():
                Months_1 = Months_1 - 1
                brain.screen.print("Months #1: " + str(Months_1))
        if brain.screen.column() == 7:
            if controller_1.buttonUp.pressing():
                Months_2 = Months_2 + 1
                brain.screen.print("Months #2: " + str(Months_2))
            if controller_1.buttonDown.pressing():
                Months_2 = Months_2 - 1
                brain.screen.print("Months #2: " + str(Months_2))
        #Days coulumns
        if brain.screen.column() == 9:
            if controller_1.buttonUp.pressing():
                Days_1 = Days_1 + 1
                brain.screen.print("Days #1: " + str(Days_1))
            if controller_1.buttonDown.pressing():
                Days_1 = Days_1 - 1
                brain.screen.print("Days #1: " + str(Days_1))
        if brain.screen.column() == 10:
            if controller_1.buttonUp.pressing():
                Days_2 = Days_2 + 1
                brain.screen.print("Days #2: " + str(Days_2))
            if controller_1.buttonDown.pressing():
                Days_2 = Days_2 - 1
                brain.screen.print("Days #2: " + str(Days_2))
        # Hours coulumns
        if brain.screen.column() == 12:
            if controller_1.buttonUp.pressing():
                Hours_1 = Hours_1 + 1
                brain.screen.print("Hours #1: " + str(Hours_1))
            if controller_1.buttonDown.pressing():
                Hours_1 = Hours_1 - 1
                brain.screen.print("Hours #1: " + str(Hours_1))
        if brain.screen.column() == 13:
            if controller_1.buttonUp.pressing():
                Hours_2 = Hours_2 + 1
                brain.screen.print("Hours #2: " + str(Hours_2))
            if controller_1.buttonDown.pressing():
                Hours_2 = Hours_2 - 1
                brain.screen.print("Hours #2: " + str(Hours_2))
        # Minutes coulumns
        if brain.screen.column() == 15:
            if controller_1.buttonUp.pressing():
                Minutes_1 = Minutes_1 + 1
                brain.screen.print("Minutes #1: " + str(Minutes_1))
            if controller_1.buttonDown.pressing():
                Minutes_1 = Minutes_1 - 1
                brain.screen.print("Minutes #1: " + str(Minutes_1))
        if brain.screen.column() == 16:
            if controller_1.buttonUp.pressing():
                Minutes_2 = Minutes_2 + 1
                brain.screen.print("Minutes #2: " + str(Minutes_2))
            if controller_1.buttonDown.pressing():
                Minutes_2 = Minutes_2 - 1
                brain.screen.print("Minutes #2: " + str(Minutes_2))
        brain.screen.next_row()
        controller_1.screen.next_row()
        if controller_1.buttonA.pressing():
            break # Come out of the loop if button A is pressed / Stop listening to user input  
    print_date_create_file()

# get_date()

# print( str(Years_1) + str(Years_2) + str(Years_3) + str(Years_4) + "/" + str(Months_1) + str(Months_2) + "/" + str(Days_1) + str(Days_2) + "/" + str(Hours_1) + str(Hours_2) + ":" + str(Minutes_1) + str(Minutes_2))



def press_button():
    global previous, current, myVariable, Days, Infinaty, screen_precision, console_precision, Years_1, Years_2, Years_3, Years_4, Months_1, Months_2, Days_1, Days_2, Hours_1, Hours_2, Minutes_1, Minutes_2
    was_pressed = False
    is_pressed = False
    while True: 
        is_pressed = controller_1.buttonUp.pressing()
        if is_pressed and not was_pressed:
            # Button A was just pressed
            print("Button A was pressed")
            get_date()
        was_pressed = is_pressed
        sleep(10)  # Add a small delay to avoid busy waiting

"""

# I'm scraping the section above and commenting it because it is not working very well 
# I made a new sectionn below that is working better and is more efficient

months = 1
days = 1 
file_numb = 1
setup = False

def screen_ready() :
    global months, days, file_numb, setup
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1, 1)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


def days_button():
    global months, days, file_numb, setup
    if controller_1.buttonUp.pressed:
        days = 1 % 31 + 1
        days = days + 1
        print ("Days: " + str(days))
    elif controller_1.buttonDown.pressed:
        days = 1 % 31 - 1
        days = days - 1
        print ("Days: " + str(days))


screen_ready()
days_button()
 