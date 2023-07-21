import sys

from rent import *
from return_ import *
import operations


def main():
    """This is the main function"""
    print("\n" + "++" * 25)
    print("\t Welcome to Costume Rental Application")
    print("++" * 25)
    while True:
        option = operations.get_option()
        if option == 1:
            rent()

        elif option == 2:
            return_costume()

        elif option == 3:
            sys.exit("\n\t\t Thank you for using our application.")
        else:
            print("\n\t\t\t!!! Invalid Input !!!\nPlease Select the values as per the provided options.")
            continue


main()
