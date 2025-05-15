#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: april, 2025
# The program creates a program that
# uses nested loops to print out all
# the valid RGB colors.
def main():
    # this function uses a nested loop
    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(0, 256, 15):
        for green in range(0, 256, 15):
            for blue in range(0, 256, 15):
                # Make sure it shows the color correspondent
                print(
                    "\033[38;2;{};{};{}mRGB({:3d}, {:3d}, {:3d}) \033[38;2;255;255;255m".format(
                        red, green, blue, red, green, blue
                    )
                )


if __name__ == "__main__":
    main()
