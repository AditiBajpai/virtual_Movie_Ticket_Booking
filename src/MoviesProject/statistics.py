#
#
# 1. number of purchased Ticket
# Select count(tickets) FROM table_name WHERE ticket_status="B%"
#
# 2. percentage of purchased Tickets
#    snumber of purchased ticets * totaltickets/100
#
# 3. current income
#    SELECT SUM(total_money) FROM table_name  WHERE ticket_status="B%"
# 4. total income
#    SELECT SUM(total_money) FROM table_name  WHERE ticket_status="B%" or ticket_status="S%"

 class Stats:

     def __init__(self):
         pass

     def no_of_purchased_tickets(self):
         query = "SELECT COUNT(ticketnumber) FROM userticket WHERE booking="B%" "
         cursor.execute(query)
         data = cursor.fetchall
         print(data)
