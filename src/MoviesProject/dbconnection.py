import mysql.connector as msc

class DatabaseConection:
    def __init__(self):
        self.user = 'admin'
        self.password = 'mysqlpassword@123'
        self.host = 'localhost'
        self.database = 'moviedb'
        self.conn = None
        self.cursor = None

        try:
            self.conn = msc.connect(user = self.user, password=self.password,
                                    host=self.host, database=self.database)
            self.cursor = self.conn.cursor()
            print("Connection Established Sucessfully...!!")
            # print(self.conn)

        except:
            print("Some error ocured while conecting")

    def insert_records(self,data):
        if self.cursor is not None and self.conn is not None:
            sql_query = "INSERT INTO userticket (name, gender, age,ticketprice,phone,ticketnumber ) VALUES (%s, %s,%s, %s,%s, %s)"
            value = (data.name,data.gender,data.age,data.ticketprice,data.phone,data.ticketnumber)
            self.cursor.execute(sql_query,value)
            self.conn.commit()
            print("Successfully Inserted")


    def __repr__(self):
        pass



# DatabaseConection()
