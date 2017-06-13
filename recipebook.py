#!/usr/bin/env python
import apsw
import string
import webbrowser

class Cookbook():
    def __init__(self):
        global connection
        global cursor
        self.totalcount = 0
        connection=apsw.Connection("recipebook.db3")
        cursor=connection.cursor()

    def Menu():
        cbk = Cookbook() # Initialize the class
        loop = True
        while loop == True:
            print('=' * 70)
            print('  RECIPE DATABASE  '.center(70, '='))
            print('=' * 70)
            print('\t1 - Show All Recipes')
            print('\t2 - Search for a Recipe')
            print('\t3 - Show a Recipe')
            print('\t4 - Delete a Recipe')
            print('\t5 - Add a Recipe')
            print('\t6 - Print a Recipe')
            print('\t0 - Exit')
            print('=' * 70)

            response = input('Enter a Selection (0 - 6) --> ')

            if response == '1': # Show all recipes
                pass

            elif response == '2': # Search for a recipe
                pass

            elif response == '3': # Show a single Recipe
                pass

            elif response == '4': # Delete Recipe
                pass

            elif response == '5': # Add a recipe
                pass

            elif response == '6': # Print a recipe
                pass

            elif response == '0': # Exit the program
                print('Good-Bye')
                loop = False

            else:
                print('Unrecognized Command. Try Again.')

    
if __name__ == '__main__':
    Cookbook.Menu()