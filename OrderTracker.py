class OrderTracker():
    TAX = 0.09
    """Tracks a restaurant's orders in a list and prepares them in
    FIFO basis """
    def __init__(self,restaurant_name = '', menu_dict = {}, orders_list = []):
        """class constructor"""
        self.name = restaurant_name
        self.menu = menu_dict
        self.__orders = orders_list

    def __repr__(self):
        return (
            f'{self.name} restaurant has '
            f'{len(self.__orders)} orders beeing prepared'
        )
    def __get_orders(self):
        """Private method that returns the list of orders"""
        return self.__orders

    def add_order(self, order):
        """Public method that add an order to the end of the list of orders 
        and returns the modified list of orders"""
        orders_list = self.__get_orders()
        orders_list.append(order)
        return self.__orders
    
    def prepare_order(self):
        """Public method that removes the first order from the list of 
        orders and returns the order that was 'prepared' (removed)"""
        orders_list = self.__get_orders()
        return orders_list.pop(0)
    
    def calculate_bill(self, order_set):
        """Takes an order, calculates the bill and returns the total price"""
        total_price = 0
        for e in order_set:
            total_price += self.menu[e]
        
        return total_price * (1 + self.TAX)

    
    def __len__(self):
        """The length of the object is the number of orders to be prepared"""
        return len(self.__orders)
     
    
# Unit tests
if __name__ == '__main__':
    carmines = OrderTracker('Carmines', {
        'Margerita Pizza': 25,
        'Seafood linguine': 40.5,
        'Bruschetta': 16.55,
        'Tiramissu cake': 9,
    })
    print(carmines)
    print(len(carmines))
    carmines.add_order({'Seafood linguine', 'Bruschetta'})
    order1 = carmines.prepare_order()
    print(order1)
    order1_bill = carmines.calculate_bill(order1)
    print(order1_bill)
