# ---------------------------------------------------------------------------- #

#                                                                              #

# 	Module:       main.py                                                      #

# 	Author:       vaazhlik                                                     #

# 	Created:      8/12/2026, 8:51:15 AM                                        #

# 	Description:  V5 project event based                                       #

#                                                                              #

# ---------------------------------------------------------------------------- #

# Library imports

# from asyncio import wait

from vex import *

import math

import random



# Brain should be defined by default

brain=Brain()

controller_1 = Controller(PRIMARY)

# Before this section of the code, I made a new one, with polling, and it was useless
# The original code in on main_polling.py

months = 8
days = 16 
file_numb = 1
minutes = 30
hours = 5
years = 26
cur_date=[years, months, days,hours,minutes]
#cur_col = controller_1.screen.column()

log_file_created = False
column_position = controller_1.screen.column()
row_position = controller_1.screen.row()
file_name = "default.csv" #

screen_lock = False #custom mutex api


def run_date_screen_temporarily():
    """Intializes the screen and 
       Update the current date on controller screen. 
       This """
    global cur_date, screen_lock, column_position, log_file_created 
    #NOTE: if the global column position is not used , a local copy will override this. resulting in screen getting reset to begin

    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1,14)

    column_position = controller_1.screen.column()
    row_position = controller_1.screen.row()

    #for index in range(len(cur_date)):
    #cur_row = controller_1.screen.row()
    #column_position = controller_1.screen.column()

    start_time = brain.timer.time(MSEC)
    last_blink_time = brain.timer.time(MSEC)
    show_cursor = True

    # Setup milestones
    duration_limit = 30000 # Run for 10 seconds (10,000 ms)
    blink_interval = 250   # Blink speed

    ### Bind all the buttons for user inputs
    controller_1.buttonUp.pressed(increment_days)
    controller_1.buttonDown.pressed(decrement_days)
    controller_1.buttonLeft.pressed(move_cursor_left)
    controller_1.buttonRight.pressed(move_cursor_right)
    controller_1.buttonA.pressed(sd_card)

    print ("start timer Column: " + str(column_position) + " Row: " + str(row_position))

    while brain.timer.time(MSEC) - start_time < duration_limit:
        current_time = brain.timer.time(MSEC)

        if not screen_lock:
            screen_lock = True

            if show_cursor:
                controller_1.screen.set_cursor(1,column_position)
                controller_1.screen.print("_")
                controller_1.screen.set_cursor(1,column_position)
                #print(column_position)
            else:
                controller_1.screen.set_cursor(1,1)
                controller_1.screen.print("{:02d}".format(cur_date[0]) +"/" +\
                                    "{:02d}".format(cur_date[1]) +"/" +\
                                    "{:02d}".format(cur_date[2]) +"-" +\
                                    "{:02d}".format(cur_date[3]) +":" +\
                                    "{:02d}".format(cur_date[4]) )
                controller_1.screen.set_cursor(1,column_position)

            show_cursor = not show_cursor
            wait(blink_interval,MSEC)
            #NOTE: if the wait is faster, the blinking effect will not be observed 
            screen_lock = False

        if log_file_created:
            break


    controller_1.screen.clear_screen()


    ### Cleanup button binding
    # controller_1.buttonUp.pressed(None)
    # controller_1.buttonDown.pressed(None)
    # controller_1.buttonLeft.pressed(None)
    # controller_1.buttonRight.pressed(None)
    # controller_1.buttonA.pressed(None)

""""""

def increment_days():
    """
    Increments the day value.
    """
    global months, days, file_numb, setup, column_position, row_position, screen_lock

    #There is no need for this function, when log file is already created
    if log_file_created:
        return
    # I had a problem, the print block automatically moves the cursor to the next coulum automatically
    # To solve this, I made a new variable in each of the incremental sections, as " coulumn "
    # This sets the current coulumn position as a variable
    # That way, I can set the coulumn position after the print() blocks to the position before
    # This variable has to be kept local

    #if not screen_lock:
        #screen_lock = True
    coulumn = column_position
    column_position = controller_1.screen.column()
    column_position = controller_1.screen.column()
    
    row_position = controller_1.screen.row()
    print ("increment_days Column: " + str(column_position) + " Row: " + str(row_position))

    #wait(2,SECONDS)

    index=int(column_position  // 3) # because list index starts with 0, while screen positions starts with 1
    if index <=0:
        index =0

    if index == 0:
        # This is the code for years
        date_part=cur_date[index] % 99 +1

    elif index == 1:
        # This is the code for months
        date_part=cur_date[index] % 12 +1

    elif index == 2:
        # This is the code for days
        date_part=cur_date[index] % 31 +1

    elif index == 3:
        # This is the code for hours
        date_part=cur_date[index] % 23 +1

    elif index == 4:
        # This is the code for minutes
        date_part=cur_date[index] % 59 +1

    else:
        pass 


    print ("increment days date index: " + str(index) + " Row: " + str(row_position))

    #date_part=cur_date[index] % 31 +1
    cur_date[index] = date_part

    #days = days % 31 + 1
    # print ("Days: " + "{:02d}".format(days))
    print ("Column: " + str(column_position) + " Row: " + str(row_position))
    controller_1.screen.set_cursor(1, index*3 )
    #controller_1.screen._column = int(column_position/3)
    # print ("Days: " + "{:02d}".format(date_part))
    controller_1.screen.print("{:02d}".format(date_part))
    controller_1.screen.set_cursor(1,column_position)
    print ("increment_days Column: " + str(column_position) + " Row: " + str(row_position) + " index: "  + str(index) )
    controller_1.screen.set_cursor(1,coulumn)
        #screen_lock = False

def decrement_days():
    """
    Increments the day value.
    """
    global months, days, file_numb, setup, column_position, row_position, screen_lock

    #There is no need for this function, when log file is already created
    if log_file_created:
        return
    
    # I had a problem, the print block automatically moves the cursor to the next coulum automatically
    # To solve this, I made a new variable in each of the incremental sections, as " coulumn "
    # This sets the current coulumn position as a variable
    # That way, I can set the coulumn position after the print() blocks to the position before
    # This variable has to be kept local

    #if not screen_lock:
        #screen_lock = True
    coulumn = column_position
    column_position = controller_1.screen.column()
    column_position = controller_1.screen.column()
    
    row_position = controller_1.screen.row()
    print ("increment_days Column: " + str(column_position) + " Row: " + str(row_position))

    #wait(2,SECONDS)

    index=int(column_position // 3) # because list index starts with 0, while screen positions starts with 1
    # I am experimenting with the index / index, and I feel that the -1 isn't nessesary 
    # Here is the original line of code:
    # index=int(column_position // 3)-1 # because list index starts with 0, while screen positions starts with 1

    if index <=0:
        index =0

    print ("increment days date index: " + str(index) + " Row: " + str(row_position))

    date_part=cur_date[index] % 31 -1
    if date_part <= 0:
        date_part = 31
    cur_date[index] = date_part

    #days = days % 31 + 1
    # print ("Days: " + "{:02d}".format(days))
    print ("Column: " + str(column_position) + " Row: " + str(row_position))
    controller_1.screen.set_cursor(1, index*3 )
    #controller_1.screen._column = int(column_position/3)
    # print ("Days: " + "{:02d}".format(date_part))
    controller_1.screen.print("{:02d}".format(date_part))
    controller_1.screen.set_cursor(1,column_position)
    print ("increment_days Column: " + str(column_position) + " Row: " + str(row_position) + " Last coulumn position: "  + str(coulumn) )
    controller_1.screen.set_cursor(1,coulumn)
        #screen_lock = False


def move_cursor_left():
    """
    Moves the cursor one position to the left.
    """
    global column_position, row_position, screen_lock
    #NOTE: Acquire the right to update the screen 
    while not screen_lock:
        screen_lock = True

    print("move cur left - Column: " + str(column_position) + " Row: " + str(row_position))

    column_position = controller_1.screen.column()
    #row_position = controller_1.screen.row()

    column_position = (column_position - 1) #%15
    if column_position <=0:
        column_position = 1
    print(" move cur left - Column: " + str(column_position) + " Row: " + str(row_position))

    controller_1.screen.set_cursor(1, column_position)
    controller_1.screen.print("_")
    controller_1.screen.set_cursor(1, column_position)

    #NOTE: Free the screen lock to facilitate date update
    screen_lock = False


def move_cursor_right():
    """
    Moves the cursor one position to the right.
    """
    global months, days, file_numb, setup, column_position, row_position, screen_lock

    #NOTE: Acquire the right to update the screen 
    while not screen_lock:
        screen_lock = True

    #column_position = controller_1.screen.column()
    print("move cur right - Column: " + str(column_position) + " Row: " + str(row_position))

    row_position = controller_1.screen.row()
    print("move cur right - Column: " + str(column_position) + " Row: " + str(row_position))

    #NOTE: Is there is a spelling mistake in the variable name, python will silently create a new variable
    #this is dangerous, leading unexpected behavior eg. column and coulumn
    column_position = (column_position + 1) % 15
    controller_1.screen.set_cursor(1, column_position)
    column_position = controller_1.screen.column()

    print("new Column: " + str(column_position) + " Row: " + str(row_position))
    controller_1.screen.print("_")
    controller_1.screen.set_cursor(1, column_position)

    print("new Column: " + str(column_position) + " Row: " + str(row_position))

    #give up the right to update the screen, so that screen refresh timer can run
    #screen_lock = False



def initialize() :
    """
    Initialize the system by creating an initial storage log file(recent_file.txt) to track time history

    """
    global cur_date


    if brain.sdcard.exists("recent_file.txt"):
        #brain.sdcard.exists

        try:
            with open("recent_file.txt", "r") as file:
            #file.read("timestamp,arm_position_deg,arm_velocity_rpm,arm_torque_nm,arm_power_w")
                content = file.read(14)
                print("----->"+str(content))


            #FIXED: when recent_file exist. read the content and increment the minute

            content_as_list = content.split('-')
            print("content_as_list"+str(content_as_list))
            try:
                for idx in range(4):
                    cur_date[idx]=int(content_as_list[idx])
                    print("cur_date["+str(idx)+"]="+str(cur_date[idx]))
                print("came here")  

            except Exception as e:
                    print("received exception at 334 "+str(e.with_traceback))



            date_part = content.split("-")[-1]
            print("date :"+str(content)+ " mm:"+date_part )
            cur_date[4] = (int(date_part) +1) % 59
            print("incremented date :"+str(cur_date)+ " mm:"+date_part )


        except Exception as e:
            print("Error reading file: " + str(e.with_traceback))

    else:
        print("no such file in sd Card")
        brain.screen.print("Dude! Did you insert the SD card ? ")
        brain.sdcard.savefile("recent_file.txt")
        #brain.sdcard.("recent_file.txt", )
        #brain.sdcard.file.read 

    # #save the current date into the recent file.txt    !!!!!! is it even required ?
    # with open("recent_file.txt","w") as file:
    #     recent_file_name = "{:02d}".format(cur_date[0]) +"-" +\
    #                             "{:02d}".format(cur_date[1]) +"-" +\
    #                             "{:02d}".format(cur_date[2]) +"-" +\
    #                             "{:02d}".format(cur_date[3]) +"-" +\
    #                             "{:02d}".format(cur_date[4])
    #     file.write(recent_file_name)


         
def sd_card ():
    global cur_date #NOTE: without this line date will not be updated in the recent_files
    global file_name #NOTE: without this line, all new writings happen in default.csv in global
    global log_file_created
    if controller_1.buttonA.pressed:
        if brain.sdcard.is_inserted():
            file_name = "{:02d}".format(cur_date[0]) +"-" +\
                                    "{:02d}".format(cur_date[1]) +"-" +\
                                    "{:02d}".format(cur_date[2]) +"-" +\
                                    "{:02d}".format(cur_date[3]) +"-" +\
                                    "{:02d}".format(cur_date[4]) + ".csv"
            try:
                with open(file_name, "w") as file:
                    #write the CSV file header
                    file.write("timestamp,arm_position_deg,arm_velocity_rpm,arm_torque_nm,arm_power_w,arm_current\n")
                    print("File saved as:" +file_name)
                    print(file_name)  

                with open("recent_file.txt","w") as recent_file:
                        last_file_date = "{:02d}".format(cur_date[0]) +"-" +\
                                    "{:02d}".format(cur_date[1]) +"-" +\
                                    "{:02d}".format(cur_date[2]) +"-" +\
                                    "{:02d}".format(cur_date[3]) +"-" +\
                                    "{:02d}".format(cur_date[4])
                        recent_file.write(last_file_date)

            except Exception as e:
                print("Error saving file: " + str(e))
                                         
        else:
            brain.screen.print("Error: No SD card")
    else:
        controller_1.screen.print("Please connect SD card")

    log_file_created = True


#######################################

def lift_weight():
    global file_name
    arm_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
    arm_motor.set_stopping(BrakeType.HOLD)
    arm_motor.set_velocity(50, PERCENT)

    while True:
        if controller_1.buttonUp.pressing():
            arm_motor.spin(DirectionType.FORWARD)

        elif controller_1.buttonDown.pressing():
            arm_motor.spin(DirectionType.REVERSE)
                    
        else:
            arm_motor.stop()

    
        #capture essential motor attributes
        t_stamp = brain.timer.value()
        pos = arm_motor.position(DEGREES)
        vel = arm_motor.velocity(RPM)
        torque = arm_motor.torque(TorqueUnits.NM)
        power = arm_motor.power(PowerUnits.WATT) 
        current = arm_motor.current(CurrentUnits.AMP)

        # Format log entry
        log_entry = "{:.3f}".format(t_stamp) +"," +\
                                "{:.2f}".format(pos) +"," +\
                                "{:.2f}".format(vel) +"," +\
                                "{:.3f}".format(torque) +"," +\
                                "{:.3f}".format(power)+"," +\
                                "{:.3f}".format(current)+"\n"


        #print(log_entry)
        
        # Append attributes to log file on SD card
        try:
            with open(file_name, "a") as f:
                f.write(log_entry)
        except Exception as e:
                brain.screen.print("File write failed")
                print("file write failed exception"+str(e.with_traceback))

# Call at startup
#load_time_from_largest_file()





initialize()
run_date_screen_temporarily()
lift_weight()
# date_screen_temporarily() hold all the other defs, so when it timed runs, all defs run together











# -------------------------------------------------------------------------------------------------------------------#


#Objectives for today, 8/14/26
"""
# Step #1, program the up button and the down button to move to the respective position that the cusror is blinking at. 
# Currently, the up arrow and down arrow only work for the years. 
# Even though the cursor moves to the right to the months feild.
"""

# Step #1 is finished


# Step #2
# I need to make the code dounload into the file as the name.
# This bit of code is for the file renaming process. It is going to take the final date

# For one thing, I need to figure out why the indents 
# are weird on the code below

"""
.format(cur_date[0]) +"/" +\
                                    "{:02d}".format(cur_date[1]) +"/" +\
                                    "{:02d}".format(cur_date[2]) +"-" +\
                                    "{:02d}".format(cur_date[3]) +":" +\
                                    "{:02d}".format(cur_date[4]) )
""" 
def write_2_sd_card():
    if brain.sdcard.is_inserted():
    # Create data to save (must be bytearray)
            data = bytearray("{:02d}".format(cur_date[0]) +"/" +\
                            "{:02d}".format(cur_date[1]) +"/" +\
                                "{:02d}".format(cur_date[2]) +"-" +\
                                "{:02d}".format(cur_date[3]) +":" +\
                                "{:02d}".format(cur_date[4]), 'utf-8' )
"""
def sd_card ():
    if controller_1.buttonA.pressed:
        if brain.sdcard.is_inserted():
            brain.sdcard.savefile(filename, data)
            brain.screen.print(f"Saved: {filename}")
        else:
            brain.screen.print("Error: No SD card")
    else:
        controller_1.screen.print("Please connect SD card")
"""



    # Save file with timestamp as name

# -------------------------------------------------------------------------------------------------- #

# Objectives for today: (8/15/26)



    # I had a problem, the print block automatically moves the cursor to the next coulum automatically
    # To solve this, I made a new variable in each of the incremental sections, as " coulumn "
    # This sets the current coulumn position as a variable
    # That way, I can set the coulumn position after the print() blocks to the position before
    # This variable has to be kept local



## ------------------------------------------------------------------------------------------------------ ##
