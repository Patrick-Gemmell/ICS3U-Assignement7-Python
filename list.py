#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: Dec 2019
# This gets random numbers then finds the users number using an array

import random


def main():
    # This function creates an array and finds if user number is in the array

    # Variables
    checker_val = 0

    # Array
    number_array = []

    # Welcome
    print("This program determines if user inputted numbers appear on a "
          "randomly generated list")

    input("\nPress enter to generate a list of 50 numbers ")

    print("\nList of numbers: \n")

    # Adding numbers to an array
    for repeater in range(50):
        random_number = random.randint(1, 100)
        print("Random Number " + str(repeater + 1) + " is " +
              str(random_number))
        number_array.append(random_number)

    # Input
    print("\nPlease enter the number you wish to")
    user_number = input("search for: ")

    try:
        # Process
        user_number = int(user_number)
        for repeater in range(len(number_array)):
            if user_number == number_array[repeater]:
                # Output
                print("\nThe number " + str(user_number) +
                      " is located on the list at the " + str(repeater + 1)
                      + "th place")
                checker_val = 1

    except Exception:
        checker_val = 1
        print("\nPlease input a proper integer number")

    # Output 2
    if checker_val == 0:
        print("\nYour number was not on the list")


if __name__ == "__main__":
    main()
