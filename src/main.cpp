// ---------------------------------------------------------------------------- //
//                                                                              //
//  Module:       main.cpp                                                     //
//  Author:       vaazhlik                                                     //
//  Created:      8/12/2026, 8:51:15 AM                                        //
//  Description:  V5 project event based                                       //
//                                                                              //
// ---------------------------------------------------------------------------- //

#include "vex.h"
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>

using namespace vex;

// Brain should be defined by default
Brain brain;
Controller controller1(PRIMARY);

// Global date variables
int months = 8;
int days = 16;
int file_numb = 1;
int minutes = 30;
int hours = 5;
int years = 26;
int cur_date[5] = {years, months, days, hours, minutes};

int column_position = 1;
int row_position = 1;
const char* file_name = "default.csv";

bool screen_lock = false;  // custom mutex api

// Forward function declarations
void run_date_screen_temporarily();
void increment_days();
void decrement_days();
void move_cursor_left();
void move_cursor_right();
void sd_card();
void experiment();

/**
 * Initializes the screen and updates the current date on controller screen.
 */
void run_date_screen_temporarily() {
    cur_date[0] = years;
    cur_date[1] = months;
    cur_date[2] = days;
    cur_date[3] = hours;
    cur_date[4] = minutes;

    controller1.screen.clearScreen();
    controller1.screen.setCursor(1, 1);

    column_position = controller1.screen.column();
    row_position = controller1.screen.row();

    int start_time = brain.timer.time(msec);
    int last_blink_time = brain.timer.time(msec);
    bool show_cursor = true;

    // Setup milestones
    int duration_limit = 100000;  // Run for 100 seconds (100,000 ms)
    int blink_interval = 250;      // Blink speed in milliseconds

    // Bind all the buttons for user inputs
    controller1.buttonUp.pressed(increment_days);
    controller1.buttonDown.pressed(decrement_days);
    controller1.buttonLeft.pressed(move_cursor_left);
    controller1.buttonRight.pressed(move_cursor_right);
    controller1.buttonA.pressed(sd_card);

    printf("start timer Column: %d Row: %d\n", column_position, row_position);

    while (brain.timer.time(msec) - start_time < duration_limit) {
        int current_time = brain.timer.time(msec);

        if (!screen_lock) {
            screen_lock = true;

            if (show_cursor) {
                controller1.screen.setCursor(1, column_position);
                controller1.screen.print("_");
                controller1.screen.setCursor(1, column_position);
            } else {
                controller1.screen.setCursor(1, 1);
                char date_str[20];
                snprintf(date_str, sizeof(date_str), "%02d/%02d/%02d-%02d:%02d",
                        cur_date[0], cur_date[1], cur_date[2], cur_date[3], cur_date[4]);
                controller1.screen.print(date_str);
                controller1.screen.setCursor(1, column_position);
            }

            show_cursor = !show_cursor;
            wait(blink_interval, msec);
            screen_lock = false;
        }
    }

    controller1.screen.clearScreen();
}

/**
 * Increments the day value.
 */
void increment_days() {
    int coulumn = column_position;
    column_position = controller1.screen.column();
    row_position = controller1.screen.row();

    printf("increment_days Column: %d Row: %d\n", column_position, row_position);

    int index = (int)(column_position / 3);
    if (index <= 0) {
        index = 0;
    }

    int date_part = 0;

    if (index == 0) {
        // Years
        date_part = cur_date[index] % 99 + 1;
    } else if (index == 1) {
        // Months
        date_part = cur_date[index] % 12 + 1;
    } else if (index == 2) {
        // Days
        date_part = cur_date[index] % 31 + 1;
    } else if (index == 3) {
        // Hours
        date_part = cur_date[index] % 23 + 1;
    } else if (index == 4) {
        // Minutes
        date_part = cur_date[index] % 59 + 1;
    }

    printf("increment days date index: %d Row: %d\n", index, row_position);

    cur_date[index] = date_part;

    printf("Column: %d Row: %d\n", column_position, row_position);
    controller1.screen.setCursor(1, index * 3);
    char formatted[3];
    snprintf(formatted, sizeof(formatted), "%02d", date_part);
    controller1.screen.print(formatted);
    controller1.screen.setCursor(1, column_position);
    printf("increment_days Column: %d Row: %d index: %d\n", column_position, row_position, index);
    controller1.screen.setCursor(1, coulumn);
}

/**
 * Decrements the day value.
 */
void decrement_days() {
    int coulumn = column_position;
    column_position = controller1.screen.column();
    row_position = controller1.screen.row();

    printf("decrement_days Column: %d Row: %d\n", column_position, row_position);

    int index = (int)(column_position / 3);
    if (index <= 0) {
        index = 0;
    }

    int date_part = cur_date[index] - 1;
    if (date_part <= 0) {
        date_part = 31;
    }
    cur_date[index] = date_part;

    printf("Column: %d Row: %d\n", column_position, row_position);
    controller1.screen.setCursor(1, index * 3);
    char formatted[3];
    snprintf(formatted, sizeof(formatted), "%02d", date_part);
    controller1.screen.print(formatted);
    controller1.screen.setCursor(1, column_position);
    printf("decrement_days Column: %d Row: %d\n", column_position, row_position);
    controller1.screen.setCursor(1, coulumn);
}

/**
 * Moves the cursor one position to the left.
 */
void move_cursor_left() {
    // Acquire the right to update the screen
    while (!screen_lock) {
        screen_lock = true;
    }

    printf("move cur left - Column: %d Row: %d\n", column_position, row_position);

    column_position = controller1.screen.column();

    column_position = (column_position - 1);
    if (column_position <= 0) {
        column_position = 1;
    }
    printf("move cur left - Column: %d Row: %d\n", column_position, row_position);

    controller1.screen.setCursor(1, column_position);
    controller1.screen.print("_");
    controller1.screen.setCursor(1, column_position);

    // Free the screen lock to facilitate date update
    screen_lock = false;
}

/**
 * Moves the cursor one position to the right.
 */
void move_cursor_right() {
    // Acquire the right to update the screen
    while (!screen_lock) {
        screen_lock = true;
    }

    printf("move cur right - Column: %d Row: %d\n", column_position, row_position);

    row_position = controller1.screen.row();
    printf("move cur right - Column: %d Row: %d\n", column_position, row_position);

    column_position = (column_position + 1) % 15;
    controller1.screen.setCursor(1, column_position);
    column_position = controller1.screen.column();

    printf("new Column: %d Row: %d\n", column_position, row_position);
    controller1.screen.print("_");
    controller1.screen.setCursor(1, column_position);

    printf("new Column: %d Row: %d\n", column_position, row_position);

    // Give up the right to update the screen
    screen_lock = false;
}

/**
 * Experiment function to test file reading.
 */
void experiment() {
    FILE* file = fopen("/", "r");
    if (file != nullptr) {
        char content[11];
        fread(content, 1, 10, file);
        printf("----->%s\n", content);
        fclose(file);
    } else {
        printf("Error reading file\n");
    }
}

/**
 * SD Card save handler.
 */
void sd_card() {
    if (controller1.buttonA.pressing()) {
        if (brain.sdcard.isInserted()) {
            char file_name_buffer[32];
            snprintf(file_name_buffer, sizeof(file_name_buffer), "%02d-%02d-%02d-%02d-%02d.csv",
                    cur_date[0], cur_date[1], cur_date[2], cur_date[3], cur_date[4]);

            FILE* file = fopen(file_name_buffer, "w");
            if (file != nullptr) {
                fprintf(file, "timestamp,arm_position_deg,arm_velocity_rpm,arm_torque_nm,arm_power_w");
                fclose(file);
                printf("File saved as: %s\n", file_name_buffer);
            } else {
                printf("Error saving file\n");
            }
        } else {
            brain.screen.print("Error: No SD card");
        }
    } else {
        controller1.screen.print("Please connect SD card");
    }
}

/**
 * Main function - Entry point for the program
 */
int main() {
    // Initialize Brain Screen
    brain.screen.clearScreen();
    brain.screen.setCursor(1, 1);
    brain.screen.print("VEX V5 Date/Time Controller");

    // Run the date screen temporarily
    run_date_screen_temporarily();

    return 0;
}
