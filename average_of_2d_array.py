#!/usr/bin/env python3

# Created by: Andrew_Ten-Den
# Created on: June 2022
# This program uses a 2D array to find the average

import random


def sum_of_numbers(passed_in_2D_list):
    # this function averages all the elements in  a 2D array

    average = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            average += single_element

    return average


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = int(input("How many rows would you like: "))
    columns = int(input("How many columns would you like: "))

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    sum = sum_of_numbers(a_2d_list)
    average = sum / (rows * columns)
    print("The average of all the numbers is: {0} ".format(average))
    print("Done")


if __name__ == "__main__":
    main()
