
class Stats:
    def __init__(self,bt):
        self.bt =bt

    def no_of_purchased_tickets(self):
        print("The total number of Purchased Tickets are:", self.bt.counter)

    def percentage_of_purchased_tickets(self):
        percent = (self.bt.counter/self.bt.capacity)*100
        print("The total Percentage of Purchased Tickets are:", round(percent,2),"%")

    def current_income(self):
        current_income = self.bt.dbc.calcIncome()
        print("The Current Income is : $",current_income)

    def total_income(self):
        total_income = 0
        if self.bt.capacity<=60:
            total_income += self.bt.capacity*self.bt.cd.price1

        else:
            capacity_first_half = (self.bt.cd.columns*len(self.bt.cd.first_half))*self.bt.cd.price1
            capacity_second_half = (self.bt.cd.columns*len(self.bt.cd.second_half))*self.bt.cd.price2


            total_income += capacity_first_half+capacity_second_half
        print("The total income is : $",total_income)
