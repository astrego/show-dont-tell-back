import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="quiz",
    user='',
    password='')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS questions;')
cur.execute('CREATE TABLE questions (id serial PRIMARY KEY,'
            'question varchar (300) NOT NULL,'
            'answer_a varchar (100) NOT NULL,'
            'answer_b varchar (100) NOT NULL,'
            'answer_c varchar (100) NOT NULL,'
            'answer_correct varchar (10) NOT NULL,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

# Insert data into the table

cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("I'm gonna make him an offer he can't refuse.",
             'The Godfather',
             'The Godfather II',
             'The Godfather III',
             "a")
            )


cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("Computer says no",
             'Her',
             '2001: A Space Odyssey',
             'E.T.',
             "b")
            )

cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("Steve Buscemy",
             'Mr. Pink',
             'Mr. Blue',
             'Mr. Orange',
             "a")
            )

cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("Jordan Peele",
             'Get Carter',
             'Get Shorty',
             'Get Out',
             "c")
            )

cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("Rosebud",
             'Casablanca',
             'Citizen Kane',
             'Chinatown',
             "b")
            )

cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("Eye of the tiger",
             'Rocky',
             'Rocky II',
             'Rocky III',
             "c")
            )

cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("Phone home",
             'E.T.',
             'Back to the future',
             'Ticket To Paradise',
             "a")
            )

cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("F/A-18E Super Hornet",
             'Top Gun: Maverick',
             'Star Wars: Episode IV: A New Hope',
             'UP',
             "a")
            )

cur.execute('INSERT INTO questions (question, answer_a, answer_b, answer_c, answer_correct)'
            'VALUES (%s, %s, %s, %s, %s)',
            ("Buzz Lightyear",
             'Bambi',
             'Toy Story',
             'Monsters, Inc.',
             "b")
            )

conn.commit()

cur.close()
conn.close()
