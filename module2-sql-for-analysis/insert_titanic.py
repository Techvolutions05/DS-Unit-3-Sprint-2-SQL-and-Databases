import psycopg2
import pandas as pd
import credit

conn = psycopg2.connect(
    dbname=credit.cred.dbname,
    user=credit.cred.user,
    password=credit.cred.password,
    host=credit.cred.host
)

curs = conn.cursor()

titanic = pd.read_csv("titanic.csv")

query = '''
DROP TABLE IF EXISTS Titanic;
CREATE TABLE titanic (
    Survived INT,
    Pclass INT,
    Name VARCHAR(100),
    Sex VARCHAR(10),
    Age INT,
    Siblings INT,
    Parents INT,
    Fare REAL
);
'''
curs.execute(query)


def get_statement(row):
    titanic['Name'] = titanic['Name'].str.replace("'", "")
    base = "INSERT INTO titanic (Survived, Pclass, Name, Sex, Age, Siblings, Parents, Fare) VALUES "
    row[2] = row[2].replace("'", "")
    return base + str(tuple(row)) + ";"


for row in titanic.values:
    query = get_statement(row)
    print(query)
    print(titanic.shape)
    curs.execute(query)
conn.commit()
