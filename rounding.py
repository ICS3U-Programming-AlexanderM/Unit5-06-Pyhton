#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Jan 26 2022
# This program gets input from the user
# and rounds it to a number of decimal
# places decided by the user.


# function to round
def round_decimal(decimal, round):
    decimal[0] = decimal[0] * 10 ** round
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / 10 ** round


def main():
    # declare array
    decimal_input = []
    # get input
    temp_var = input("Enter your decimal: ")
    round_string = input("How many places should it be rounded to: ")
    # error checking
    try:
        temp_float = float(temp_var)
        decimal_input.append(temp_float)
        round_input = int(round_string)
        # call function
        round_decimal(decimal_input, round_input)
        print("The rounded number is {}". format(decimal_input[0]))
    except Exception:
        print("Invalid input(s).")


if __name__ == "__main__":
    main()
