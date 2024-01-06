# step 0 - import sqlite3
import sqlite3
import queries as q

# step 1
# connect to the database
# tripple-check the spelling of your database filename
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2
cursor = connection.cursor()

# step 3 - Write a query
# (See the queries.py file)

# step 4 - Execute the query on the cursor and fetch the results
# "Pulling the results from the cursor"
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
