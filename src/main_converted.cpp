// ---------------------------------------------------------------------------- //
//                                                                              //
// 	Module:       main.cpp                                                    //
// 	Author:       vaazhlik                                                    //
// 	Created:      8/12/2026, 8:51:15 AM                                       //
// 	Description:  V5 project event based                                      //
//                                                                              //
// ---------------------------------------------------------------------------- //

// Library imports
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

// Assuming VEX library includes would look like this
// #include "vex.h"

// Brain should be defined by default
// Brain brain;
// Controller controller_1(PRIMARY);

int months = 8;
int days = 16;
int file_numb = 1;
int minutes = 30;
int hours = 5;
int years = 26;
std::vector<int> cur_date = {years, months, days, hours, minutes};

int column_position = 1;  // controller_1.screen.column()
int row_position = 1;     // controller_1.screen.row()
std::string file_name = "default.csv";

bool screen_lock = false;  // custom mutex api


void run_date_screen_temporarily() {
    // Initializes the screen and 
    // Update the current date on controller screen. 
    // This ""

    global cur_date, screen_lock, column_position;

    // controller_1.screen.clear_screen();
    // controller_1.screen.set_cursor(1, 14);

    column_position = 1;  // controller_1.screen.column()
    row_position = 1;     // controller_1.screen.row()

    long start_time = 0;  // brain.timer.time(MSEC);
    long last_blink_time = 0;  // brain.timer.time(MSEC);
    bool show_cursor = true;

    // Setup milestones
    long duration_limit = 100000;  // Run for 10 seconds (10,000 ms)
    long blink_interval = 250;     // Blink speed

    // Bind all the buttons for user inputs
    // controller_1.buttonUp.pressed(increment_days);
    // controller_1.buttonDown.pressed(decrement_days);
    // controller_1.buttonLeft.pressed(move_cursor_left);
    // controller_1.buttonRight.pressed(move_cursor_right);
    // controller_1.buttonA.pressed(sd_card);

    printf("start timer Column: %d Row: %d\n", column_position, row_position);

    while (true) {  // brain.timer.time(MSEC) - start_time < duration_limit
        long current_time = 0;  // brain.timer.time(MSEC)

        if (!screen_lock) {
            screen_lock = true;

            if (show_cursor) {
                // controller_1.screen.set_cursor(1, column_position);
                // controller_1.screen.print("_");
                // controller_1.screen.set_cursor(1, column_position);
            } else {
                // controller_1.screen.set_cursor(1, 1);
                // controller_1.screen.print();
                std::string date_str = "";
                char buffer[20];
                sprintf(buffer, "%02d/%02d/%02d-%02d:%02d", 
                        cur_date[0], cur_date[1], cur_date[2], cur_date[3], cur_date[4]);
                date_str = std::string(buffer);
                // controller_1.screen.set_cursor(1, column_position);
            }

            show_cursor = !show_cursor;
            // wait(blink_interval, MSEC);
            screen_lock = false;
        }
    }

    // controller_1.screen.clear_screen();
}


void increment_days() {
    // Increments the day value.

    int coulumn = column_position;
    column_position = 1;  // controller_1.screen.column()
    
    row_position = 1;  // controller_1.screen.row()
    printf("increment_days Column: %d Row: %d\n", column_position, row_position);

    int index = (int)(column_position / 3);
    if (index <= 0) {
        index = 0;
    }

    int date_part = 0;

    if (index == 0) {
        // This is the code for years
        date_part = cur_date[index] % 99 + 1;
    } else if (index == 1) {
        // This is the code for months
        date_part = cur_date[index] % 12 + 1;
    } else if (index == 2) {
        // This is the code for days
        date_part = cur_date[index] % 31 + 1;
    } else if (index == 3) {
        // This is the code for hours
        date_part = cur_date[index] % 23 + 1;
    } else if (index == 4) {
        // This is the code for minutes
        date_part = cur_date[index] % 59 + 1;
    }

    printf("increment days date index: %d Row: %d\n", index, row_position);

    cur_date[index] = date_part;

    printf("Column: %d Row: %d\n", column_position, row_position);
    // controller_1.screen.set_cursor(1, index * 3);
    
    char buffer[20];
    sprintf(buffer, "%02d", date_part);
    // controller_1.screen.print(buffer);
    // controller_1.screen.set_cursor(1, column_position);
    
    printf("increment_days Column: %d Row: %d index: %d\n", column_position, row_position, index);
    // controller_1.screen.set_cursor(1, coulumn);
}


void decrement_days() {
    // Decrements the day value.

    int coulumn = column_position;
    column_position = 1;  // controller_1.screen.column()
    
    row_position = 1;  // controller_1.screen.row()
    printf("increment_days Column: %d Row: %d\n", column_position, row_position);

    int index = (int)(column_position / 3);
    if (index <= 0) {
        index = 0;
    }

    printf("increment days date index: %d Row: %d\n", index, row_position);

    int date_part = cur_date[index] % 31 - 1;
    if (date_part <= 0) {
        date_part = 31;
    }
    cur_date[index] = date_part;

    printf("Column: %d Row: %d\n", column_position, row_position);
    // controller_1.screen.set_cursor(1, index * 3);
    
    char buffer[20];
    sprintf(buffer, "%02d", date_part);
    // controller_1.screen.print(buffer);
    // controller_1.screen.set_cursor(1, column_position);
    
    printf("increment_days Column: %d Row: %d Last coulumn position: %d\n", column_position, row_position, coulumn);
    // controller_1.screen.set_cursor(1, coulumn);
}


void decrement_days_dummy() {
    // Decrements the day value.

    int column_position_local = 1;  // controller_1.screen.column()
    int index = (int)(column_position_local / 3) - 1;
    
    if (index <= 0) {
        index = 0;
    }

    int date_part = (cur_date[index] - 1 + 31) % 31;

    int column = column_position_local;

    cur_date[index] = date_part;
    printf("column_position:%didx:%d\n", column_position_local, index);

    // controller_1.screen.set_cursor(1, index * 3);
    
    char buffer[20];
    sprintf(buffer, "%02d", date_part);
    // controller_1.screen.print(buffer);

    // controller_1.screen.set_cursor(1, column);
}


void move_cursor_left() {
    // Moves the cursor one position to the left.

    while (!screen_lock) {
        screen_lock = true;
    }

    printf("move cur left - Column: %d Row: %d\n", column_position, row_position);

    column_position = 1;  // controller_1.screen.column()

    column_position = (column_position - 1);
    if (column_position <= 0) {
        column_position = 1;
    }
    printf(" move cur left - Column: %d Row: %d\n", column_position, row_position);

    // controller_1.screen.set_cursor(1, column_position);
    // controller_1.screen.print("_");
    // controller_1.screen.set_cursor(1, column_position);

    screen_lock = false;
}


void move_cursor_right() {
    // Moves the cursor one position to the right.

    while (!screen_lock) {
        screen_lock = true;
    }

    printf("move cur right - Column: %d Row: %d\n", column_position, row_position);

    row_position = 1;  // controller_1.screen.row()
    printf("move cur right - Column: %d Row: %d\n", column_position, row_position);

    column_position = (column_position + 1) % 15;
    // controller_1.screen.set_cursor(1, column_position);
    column_position = 1;  // controller_1.screen.column()

    printf("new Column: %d Row: %d\n", column_position, row_position);
    // controller_1.screen.print("_");
    // controller_1.screen.set_cursor(1, column_position);

    printf("new Column: %d Row: %d\n", column_position, row_position);
}


void experiment() {
    std::string content_to_save = "";
    char buffer[100];
    sprintf(buffer, "%02d-%02d-%02d-%02d-%02d", 
            cur_date[0], cur_date[1], cur_date[2], cur_date[3], cur_date[4]);
    content_to_save = std::string(buffer);

    // Check if file exists
    std::ifstream file_check("recent_file.txt");
    if (file_check.good()) {
        file_check.close();

        try {
            std::ifstream file("recent_file.txt");
            std::string content(14, ' ');
            file.read(&content[0], 14);
            file.close();
            
            printf("------->%s\n", content.c_str());

            std::string date_part = content.substr(content.length() - 2);
            printf("date :%d %d %d %d %d mm:%s\n", 
                   cur_date[0], cur_date[1], cur_date[2], cur_date[3], cur_date[4], date_part.c_str());
            
            cur_date[4] = (std::stoi(date_part) + 1) % 59;
            printf("incremented date :%d %d %d %d %d mm:%s\n", 
                   cur_date[0], cur_date[1], cur_date[2], cur_date[3], cur_date[4], date_part.c_str());

        } catch (const std::exception &e) {
            printf("Error reading file: %s\n", e.what());
        }
    } else {
        printf("no such file in sd Card\n");
        
        try {
            std::ofstream file("recent_file.txt");
            file.write(content_to_save.c_str(), content_to_save.length());
            file.close();
        } catch (const std::exception &e) {
            printf("Error writing file: %s\n", e.what());
        }
    }
}


void sd_card() {
    if (true) {  // controller_1.buttonA.pressed
        // if (brain.sdcard.is_inserted())
        {
            char filename[100];
            sprintf(filename, "%02d-%02d-%02d-%02d-%02d.csv", 
                    cur_date[0], cur_date[1], cur_date[2], cur_date[3], cur_date[4]);
            
            try {
                std::ofstream file(filename);
                file.write("timestamp,arm_position_deg,arm_velocity_rpm,arm_torque_nm,arm_power_w", 
                           strlen("timestamp,arm_position_deg,arm_velocity_rpm,arm_torque_nm,arm_power_w"));
                file.close();
                
                printf("File saved as:%s\n", filename);
                printf("%s\n", filename);

            } catch (const std::exception &e) {
                printf("Error saving file: %s\n", e.what());
            }
        }
        // else
        // {
        //     brain.screen.print("Error: No SD card");
        // }
    } else {
        // controller_1.screen.print("Please connect SD card");
    }
}


void confirm() {
    printf("Confirm Date: %4d/%02d/%02d\n", years, months, days);
    printf("Days: %02d\n", days);
    printf("Column: %d Row: %d\n", column_position, row_position);
}


void lift_weight() {
    // arm_motor = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False);
    // arm_motor.set_stopping(BrakeType.HOLD);
    // arm_motor.set_velocity(50, PERCENT);

    while (true) {
        // if (controller_1.buttonUp.pressing())
        // {
        //     arm_motor.spin(DirectionType.FORWARD);
        // }
        // else if (controller_1.buttonDown.pressing())
        // {
        //     arm_motor.spin(DirectionType.REVERSE);
        // }
        // else
        // {
        //     arm_motor.stop();
        // }

        // Capture essential motor attributes
        double t_stamp = 0.0;  // brain.timer.value()
        double pos = 0.0;      // arm_motor.position(DEGREES)
        double vel = 0.0;      // arm_motor.velocity(RPM)
        double torque = 0.0;   // arm_motor.torque(TorqueUnits.NM)
        double power = 0.0;    // arm_motor.power(PowerUnits.WATT)

        // Format log entry
        char log_entry[200];
        sprintf(log_entry, "%.3f-%.2f-%.2f-%.3f-%.3f", t_stamp, pos, vel, torque, power);

        printf("%s\n", log_entry);

        // Append attributes to log file on SD card
        try {
            std::ofstream f(log_entry, std::ios::app);
            f.write(log_entry, strlen(log_entry));
            f.close();
        } catch (const std::exception &e) {
            printf("File write failed\n");
        }
    }
}


void write_2_sd_card() {
    // if (brain.sdcard.is_inserted())
    {
        // Create data to save (must be bytearray)
        char data[200];
        sprintf(data, "%02d/%02d/%02d-%02d:%02d",
                cur_date[0], cur_date[1], cur_date[2], cur_date[3], cur_date[4]);
        
        // brain.sdcard.savefile(filename, data);
        // brain.screen.print(f"Saved: {filename}");
    }
}


int main() {
    // Call at startup
    experiment();
    run_date_screen_temporarily();
    // lift_weight();
    
    return 0;
}
