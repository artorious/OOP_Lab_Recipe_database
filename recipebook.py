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
                cbk.PrintAllRecipes()
                print('Total Recipes - {}'.format(cbk.totalcount))
                print('-' * 70)
                res = input('Press Return Key to Continue --> ')

            elif response == '2': # Search for a recipe
                pass

            elif response == '3': # Show a single Recipe
                cbk.PrintAllRecipes()
                try:
                    res = int(input('Select a Recipe -> '))
                    if res <= cbk.totalcount:
                        cbk.PrintSingleRecipe(res)
                    elif res == cbk.totalcount + 1:
                        print('Back to Menu.....')
                    else:
                        print('Unrecognized Command. Returning to menu.')
                except ValueError:
                    print('Not a Number......Back to menu.')


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
        
    def PrintAllRecipes(self):
        print('{0} {1} {2} {3}'.format('Item'.ljust(5), 'Name'.ljust(30), \
        'Serves'.ljust(20), 'Source'.ljust(30)))
        print('-' * 70)
        sql = 'SELECT * FROM Recipes'
        cntr = 0
        for x in cursor.execute(sql):
            cntr += 1
            print('{0} {1} {2} {3} ' .format(str(x[0]).rjust(5), x[1].ljust(30), \
                x[2].ljust(20), x[3].ljust(30)))
            print('-' * 70)
            self.totalcount = cntr
    
    def PrintSingleRecipe(self, which):
        sql = 'SELECT * FROM Recipes WHERE pkID = {}'.format(str(which))
        print('-' * 70)
        for x in cursor.execute(sql):
            recipeid = x[0]
            print('Title: ' + x[1])
            print('Serves: ' + x[2])
            print('Source: ' + x[3])
        print('-' * 70)
        sql = 'SELECT * FROM Ingredients WHERE pkID = {}'.format(recipeid)
        print('Ingredients List: ')
        for x in cursor.execute(sql):
            print(x[1])
        print(' ')
        print('Instructions: ')
        sql = 'SELECT * FROM Instructions WHERE RecipeID = {}'.format(recipeid)
        for x in cursor.execute(sql):
            print(x[1])
        print('-' * 70)
        resp = input('Press return key to continue -> ')
    
if __name__ == '__main__':
    Cookbook.Menu()