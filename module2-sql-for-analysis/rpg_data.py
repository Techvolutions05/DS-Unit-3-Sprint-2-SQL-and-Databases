import psycopg2
import sqlite3

# Stablishing a connection with PostgreSQL

dbname = '-------'
user = '-------'
password = '----------'  # Sensitive! Don't share/commit
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

# connected - creating a example to populate (from the tk)
# create_table_statement = """
# CREATE TABLE rpg_data (
#   id SERIAL PRIMARY KEY,
#   name varchar(40) NOT NULL,
#   data JSONB
# );
# """
#
# pg_curs.execute(create_table_statement)
# pg_conn.commit()

pg_curs.execute('SELECT * FROM rpg_data;')
pg_curs.fetchall()

# insert_statement = """
# INSERT INTO rpg_data (name, data) VALUES
# (
#   'Zaphod Beeblebrox',
#   '{"key": "value", "key2": true}'::JSONB
# )
# """

# pg_curs.execute(insert_statement)
# pg_conn.commit()


pg_curs.execute('SELECT * FROM rpg_data;')
pg_curs.fetchall()

# stablishing connection with sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = "SELECT * FROM charactercreator_character;"
sl_curs.execute(get_characters)
characters = sl_curs.fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_character);')
sl_curs.fetchall()

create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""


pg_curs.execute(create_character_table)
pg_conn.commit()

for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)

pg_conn.commit()

pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()
