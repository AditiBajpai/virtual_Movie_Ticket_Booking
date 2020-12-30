from MoviesProject.buyticket import BuyTicket
from MoviesProject.cinemadisplay import CinemaDisplay

row = int(input("Enter number of rows in the cinema hall: "))
column = int(input("Enter number of columns in the cinema hall: "))

cd = CinemaDisplay(row,column)
bt = BuyTicket(cd)
while True:
    print("Press 1 to Show the seats")
    print("Press 2 to Buy a Ticket")
    print("Press 3 to view Statistics")
    print("Press 4 to See Booked Tickets User Info")
    print("Press 5 to Exit")

    output = int(input())

    if output == 1:
        cd.showSeatMap()

    elif output == 2:
        bt.bookTicket()
    elif output == 3:
        pass
    elif output == 4:
        pass
    elif output == 5:
        pass
