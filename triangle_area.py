#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program prints the area of a triangle
#   user inputs number

import math


def calculate_area(base, height):
    # This function prints the area of a triangle

    # process
    area = (base * height) / 2

    # output
    print("The area is {} cm²".format(area))


def main():
    # this function just calls other functions

    base_from_user = input("Enter the base of a triangle (cm): ")
    height_from_user = input("Enter the height of a triangle (cm): ")

    try:
        height_integer = int(height_from_user)
        base_integer = int(base_from_user)
        calculate_area(height_integer, base_integer)
    except Exception:
        print("{} is not an integer".format(base_from_user))


if __name__ == "__main__":
    main()
