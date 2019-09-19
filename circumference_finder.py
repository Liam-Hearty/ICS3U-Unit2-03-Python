#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program will calculate the circumference of a determined circle radius.

import constants


def main():
    # this function will calculate the circumference

    # input
    radius = int(input("Enter the radius of circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("circumference is {}mm".format(circumference))


if __name__ == "__main__":
    main()
