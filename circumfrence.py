#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sept 2021
# This program calculates the circumcfrence of a circle using (tau)

import constants


def main():
    # This program calculates the circumcfrence of a circle using (tau)

    # input
    radius = int(input("Enter the radius of the circle (mm): "))

    # process
    circumfrence = radius * constants.TAU

    # output
    print("The circumfrence would be {} mm².".format(circumfrence))
    print("\nDone.")


if __name__ == "__main__":
    main()
