
class CinemaDisplay:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.arr =  [["S"]*self.columns for _ in range(self.rows)]
        self.price1 = None
        self.price2 = None
        self.first_half = None
        self.second_half = None

        self.setPrice()
        # self.showSeatMap()



    def showSeatMap(self):
        a = ' '
        for j in range(0,self.columns):
            a+=' ' +str(j+1)
        print(' '+a)

        for i in range(0,self.rows):
            s =''
            for j in range(0,self.columns):
                s+= ' '+self.arr[i][j]
            print((i+1),s)


    def updateSeat(self,row,column):
        if self.arr[row-1][column-1] == 'S':
            self.arr[row-1][column-1] = 'B'
            print("Seat Successfully updated..!!!")

        else:
            print("This Seat is already occupied..")

    def setPrice(self):

        if self.rows*self.columns<=60:
            self.price1 = 10
            self.price2 = 10
        else:
            self.price1 = 10
            self.price2 = 8
            if self.rows%2==0:
                self.first_half = list(range(0,self.rows//2))
                self.second_half = list(range(self.rows//2,self.rows))
            else:
                self.first_half =list(range(0,(self.rows//2)+1))
                self.second_half = list(range(self.rows//2,self.rows))



# c =CinemaDisplay(4,5)
# c.updateSeat(2,3)
