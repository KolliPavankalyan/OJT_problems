'''24. Write a Python class Restaurant with attributes like menu_items, 
book_table, and customer_orders, and methods like add_item_to_menu, book_tables, 
and customer_order. Perform the following tasks now: - Now add items to the menu. 
- Make table reservations. - Take customer orders. - Print the menu. - Print table reservations.
 - Print customer orders. Note : Use dictionaries and lists to store the data. '''


class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.coustomer_order = []

    def menu_item(self,item_name,price):
        self.menu_items[item_name]=price
        

    def book_tables(self,table_num):
        self.book_table.append(table_num)
    
    def customer_orders(self,table_num,order_items):
        self.coustomer_order.append({"table_num" : table_num, 'order_items':order_items}) 
         
    
    def Print_the_menu(self):
        for item,price in self.menu_items.items():
            print("{}  -   {}".format(item,price))

    def Make_table_reservations(self):
        print("Reservation tables   :")
        for table in self.book_table:
            print("table {}".format(table))

            
    def Print_customer_orders(self):
        print('Customer Orders:')
        for i in self.coustomer_order:
            print("Table_num {} : order Items {}".format(i['table_num'],i['order_items']))



obj  = Restaurant()
obj.menu_item("chicken", 200)
obj.menu_item("fish",400)
obj.menu_item("chili chicken",250)

obj.book_tables(1)
obj.book_tables(2)
obj.book_tables(3)


obj.Print_the_menu()

obj.Make_table_reservations()

obj.customer_orders(1,["chicken","motton"])
obj.customer_orders(2,["fish","motton"])
obj.customer_orders(3,["chili chicken","motton"])
obj.Print_customer_orders()
