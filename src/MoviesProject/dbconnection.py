import mysql.connector as msc

class DatabaseConection:
    def __init__(self):
        self.user = 'aditi'
        self.password = 'aditi123'
        self.host = 'localhost'
        self.database = 'moviedb'
        self.conn = None
        self.cursor = None

        # self.conn = msc.connect(user = self.user, password=self.password,
        #                         host=self.host, database=self.database)
        # self.cursor = self.conn.cursor()


        try:
            self.conn = msc.connect(user = self.user, password=self.password,
                                    host=self.host, database=self.database)
            self.cursor = self.conn.cursor()
            print("Connection Established Sucessfully...!!")
            self.clear_table()

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

    def calcIncome(self):
        sql_query = "SELECT SUM(ticketprice) FROM userticket;"
        self.cursor.execute(sql_query)
        data = self.cursor.fetchall()
        return data[0][0]

    def clear_table(self):
        sql_query = "DELETE FROM userticket;"
        try:
            self.cursor.execute(sql_query)
            self.conn.commit()
        except:
            # pass
            print("Some error occured while table deletion....!!")

    def close_connection(self):
        self.conn.close()
        print("Connection closed Succesfully..!!")







# DatabaseConection()
