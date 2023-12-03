import sqlite3


conn = sqlite3.connect("Database.db")
cursor = conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS ACCOUNT
            ( 
                ID          TEXT     NOT NULL,
                FirstName   TEXT     NOT NULL,
                LastName    TEXT     NOT NULL,
                Password    TEXT     NOT NULL,
                email       TEXT     NOT NULL,
                PhoneNum    VARCHAR(10) NOT NULL,
                PRIMARY KEY (ID),
                UNIQUE(email),
                UNIQUE(PhoneNum) 
            );
        ''')

cursor.execute('''
            CREATE TABLE IF NOT EXISTS GOLF_CART
            ( 
                PlateNumber TEXT     NOT NULL, 
                College     TEXT     NOT NULL,
                PRIMARY KEY (PlateNumber)
            );
        ''')

conn.commit()

