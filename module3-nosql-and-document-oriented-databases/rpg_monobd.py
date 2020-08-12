import cred
import pymongo
import sqlite3
'''
I found working with mongodb a little more easy/manageable to work with than PostgreSQL,
however today i learn that relaying on their database/software is not always the best way to go.
i could see myself using mongobd in the future depending on the type of project am working with.

Also establishing a connection could become a little bit of a headache with mongodb. Have to know your 
exact IP address and if using the free version you can only create 1 cluster at a time. When
working with PostgreSQL i was able to work on multiple tables and upload multiple projects at once.
'''
# establishing a connection with mongodb
password = cred.mongo.password
dbname = cred.mongo.dbname
connection = cred.mongo.connection
client = cred.mongo.client
db = cred.mongo.db

# Creating my personal character just to add a lil bit of fun lol
my_character = (1, "Alienell", 10, 10, 10, 10, 10, 10, 10)

Alienell_doc = {
    'doc_type': 'my_character',
    'sql_key': my_character[0],
    'name': my_character[1],
    'level': my_character[2],
    'exp': my_character[3],
    'hp': my_character[4],
    'strength': my_character[5],
    'intelligence': my_character[6],
    'dexterity': my_character[7],
    'wisdom': my_character[8]
}
# inserting my character
db.mongo.insert_one({Alienell_doc})

# Okay back to the action - Extracting data from sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Copying the charactercreator_character table
get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()

# Arranging features
features = ('name', 'level', 'exp', 'hp',
            'strength', 'intelligence', 'dexterity', 'wisdom')

# Asserting/uploading table to my mongodb
db.mongo.insert_many(
    {i: a for i, a in zip(features, character[1:])} for character in characters
)












