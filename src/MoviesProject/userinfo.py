
class UserInformation:
    def __init__(self,bt):
        self.bt = bt

    def display_info(self):
        row = int(input("Enter the row number : "))
        column = int(input("Enter the column number : "))
        ticketnumber = str(row-1)+","+str(column-1)
        if ticketnumber in self.bt.records.keys():
            self.display_details(self.bt.records[ticketnumber])
            #print(self.bt.records[ticketnumber])
            print("ticketnumber= ",str(row)+","+str(column))
        else:
            print("The provided ticket number does not exist")

    def display_details(self,data):
        print("NAME : ",data.name )
        print("AGE : ",data.age)
        print("PHONE NUMBER : ", data.phone)
        print("GENDER : ", data.gender)
        print("TICKET PRICE : ", data.ticketprice)
