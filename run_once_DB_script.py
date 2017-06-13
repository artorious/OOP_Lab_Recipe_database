#!/usr/bin/env python
# A simple run-once(throwaway) scrip to create and set up database with afew entries
import apsw

# Open/Create DB
connection = apsw.Connection("recipebook.db3")
cursor = connection.cursor()
# Sqlite3 Table
sql = 'CREATE TABLE Recipes(pkid INTEGER PRIMARY KEY, name TEXT, \
                            servings TEXT, source TEXT)'
cursor.execute(sql)
# Sqllite3 Table
sql = 'CREATE TABLE Instructions(pkid INTEGER PRIMARY KEY, instructions TEXT,\
                                    recipeID NUMERIC)'
cursor.execute(sql)
#Sqlite3 Table
sql = 'CREATE TABLE Ingredients(pkid INTEGER PRIMARY KEY, ingredients TEXT,\
                                recipeID NUMERIC)'
cursor.execute(sql)

# Add Data to Table
sql = 'INSERT INTO Recipes(name, servings, source) VALUES("Spanish Rice", 4, "Greg Walters")'
cursor.execute(sql)

# Get value assigned to pkID in Table
sql = "SELECT last_insert_rowid()"
cursor.execute(sql)
for x in cursor.execute(sql):
    lastid = x[0]

# Add data to table
sql = 'INSERT INTO Instructions(recipeID, instructions) VALUES(%s,\
        "Brown hambuger. Stir in all othe ingredients. Bring to a boil. Stir.\
        Lower to simmer. Cover and cook for 20 minutes or untill all liquid is \
        absorbed.")' % lastid
cursor.execute(sql)

# Add data to table
sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, \
        "1 cup parboiled Rice (uncooked). Nyanya, Royco, spices.")' % lastid
cursor.execute(sql)

                                                                