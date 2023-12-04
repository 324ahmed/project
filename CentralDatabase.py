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
cursor.execute('''
    CREATE TABLE IF NOT EXISTS RESERVATION(
        ReservationID INTEGER PRIMARY KEY AUTOINCREMENT,
        AccountID TEXT,
        PlateNumber TEXT,
        College TEXT,
        FOREIGN KEY (AccountID) REFERENCES ACCOUNT(ID),
        FOREIGN KEY (PlateNumber, College) REFERENCES GOLF_CART(PlateNumber, College),
        UNIQUE(AccountID)
    )
''')

conn.commit()

