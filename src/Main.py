from MoviesProject.buyticket import BuyTicket
from MoviesProject.cinemadisplay import CinemaDisplay
from MoviesProject.statistics import Stats
from MoviesProject.userinfo import UserInformation
row = int(input("Enter number of rows in the cinema hall: "))
column = int(input("Enter number of columns in the cinema hall: "))

cd = CinemaDisplay(row,column)
bt = BuyTicket(cd)
stats = Stats(bt)
user = UserInformation(bt)

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
        stats.no_of_purchased_tickets()
        stats.percentage_of_purchased_tickets()
        stats.current_income()
        stats.total_income()
    elif output == 4:
        user.display_info()
    elif output == 5:
        bt.dbc.close_connection()
        break
