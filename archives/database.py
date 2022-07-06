import sqlite3

def loadDatabase(self):

        # connect and create a table in the database #
    try:
        self.connection = sqlite3.connect('alldata.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
                '''
                    create table if not exists userdata(
                        id integer primary key autoincrement,
                        name varchar(50) null,
                        email varchar(50) not null,
                        password varchar(6) not null
                    );
                '''
            )

        self.cursor.execute(
                '''
                    create table if not exists userpurchase(
                        id integer primary key autoincrement,
                        name varchar(50) null,
                        email varchar(50) not null,
                        password varchar(10) not null,
                        cpf int(11) not null,
                        cep int(12) not null,
                        card int(15) not null
                    );
                '''
            )

        self.cursor.execute(
                '''
                    create table if not exists productlocation(
                        id integer primary key autoincrement,
                        local varchar(30) null,
                        date date null,
                        hour int(4) null,
                        climate varchar(50) null
                    );
                '''
            )
            
        self.cursor.execute(
            '''
                create table if not exists productinfo(
                    id integer primary key autoincrement,
                    name varchar(50) not null,
                    price float(10) not null,
                    quantity int(100) not null
                );
            '''
        )

        self.connection.commit()
        print('The connection works!')

        # if the code of the top don't work this will alert #
    except:
        print('The connection do not works!')
