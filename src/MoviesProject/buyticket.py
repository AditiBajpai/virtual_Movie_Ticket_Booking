#from cinemadisplay import CinemaDisplay
from MoviesProject.user import User
from MoviesProject.dbconnection import DatabaseConection


class BuyTicket:
    def __init__(self,cd):
        self.cd =cd
        self.counter = 0
        self.capacity  = self.cd.rows*self.cd.columns
        self.records = {}
        self.dbc = DatabaseConection()

    def bookTicket(self):
         print("DO YOU WANT TO BOOK A TICKET? ENTER YES")
         response = input()
         if response.lower()=="yes":
             print("Enter Row to select your seat")
             row = int(input("Enter row : "))
             print("Enter Column to select your seat")
             column = int(input("Enter column : "))
             price = 0
         if self.cd.first_half and self.cd.second_half is not None:
                 if row-1 in self.cd.first_half:
                     price = self.cd.price1
                 else:
                     price = self.cd.price2
         else:
             price = self.cd.price1
         print("Your ticket price is : $", price)
         self.confirmBooking(row,column,price)

    def confirmBooking(self,row,column,price):
        print("Please enter your details:")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter Male/Female: ")
        phone = input("Enter your contact number: ")
        ticketnumber = str(row-1)+","+str(column-1)

        user = User(name,age,phone,gender,price,ticketnumber)
        self.counter+=1
        self.records[ticketnumber]=user
        self.dbc.insert_records(user)
        self.cd.updateSeat(row,column)
        print("Ticket Booked Successfully..!!!")
        self.cd.showSeatMap()
