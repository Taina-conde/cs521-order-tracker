"""
Taina Batista Conde
Class: CS 521 - Fall 1
Date: 10/19/2021
Final Project
Description: OrderTracker class

"""

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
            f'{self.name} has {len(self.__orders)} orders beeing prepared. '
            f'Orders queue: {self.__orders}'

        )
    def get_orders(self):
        """Returns the list of orders"""
        return self.__orders

    def validate_order(self, order):
        """ Checks if the order items are in the menu and add the order
        to the list if they are - returns (True, message). 
        Returns (False, item) if item is not in the menu"""
        for element in order:
            # order is a set of tuples. The first element of a tuple is the
            # item and the second the quantity
            if element[0] not in self.menu.keys():
                return  (
                    False, 
                    f'{element[0]} is not in the Menu. '
                    f'Please, try again.'
                )
        self.__add_order(order)
        return (True, (
            f'Your order of {order} was added to the queue! '
            f'Orders in queue: {len(self.__orders) - 1}'
            ))
            


    def __add_order(self, order):
        """Adds an order to the end of the list of orders 
        and returns the modified list of orders"""
        orders_list = self.get_orders()
        orders_list.append(order)
    
    def prepare_order(self):
        """Removes the first order from the list of 
        orders and returns the order that was 'prepared' (removed)"""
        orders_list = self.get_orders()
        return orders_list.pop(0)
    
    def calculate_bill(self, order_set):
        """Takes an order, calculates the bill and returns the total price
        with two decimal points"""
        total_price = 0
        for e in order_set:
            item = e[0]
            item_quantity = e[1]
            total_price += self.menu[item] * item_quantity
        return round(total_price * (1 + self.TAX), 2)

    
    def __len__(self):
        """The length of the object is the number of orders to be prepared"""
        return len(self.__orders)
     
    
# Unit tests
if __name__ == '__main__':
    TAX = 0.09
    NAME = 'Carmines Restaurant'
    MENU = {
        'PIZZA': 25,
        'SEAFOOD LINGUINE': 40.5,
        'BRUSCHETTA': 16.55,
        'TIRAMISU': 9,
    }
    FIRST_ORDER =  {('PIZZA', 1), ('TIRAMISU', 2)}
    FIRST_ORDER_BILL = round(
            (MENU['PIZZA'] * 1 + MENU['TIRAMISU'] * 2) * (1 + TAX),
            2
        )
    ORDER_X = {('SEAFOOD LINGUINE', 2), ('BRUSCHETTA', 1)}
    ORDER_Y = {('NOT IN MENU', 1)}
    
    # instantiate OrderTracker obj
    carmines = OrderTracker( NAME, MENU , [FIRST_ORDER])
    # Assert tests
    # test get_orders method
    orders_list = carmines.get_orders()
    assert orders_list == [FIRST_ORDER], (
        f'Error getting the orders list '
        f'{orders_list} != {list(FIRST_ORDER)}'
    )
    # test prepare_order method
    order_1 = carmines.prepare_order()
    assert order_1 == FIRST_ORDER, (
                f'Error preparing first order in queue ' 
                f'{carmines.prepare_order()} != {FIRST_ORDER}'
            )
    # test calculate_bill method
    order_1_bill = carmines.calculate_bill(order_1)
    assert order_1_bill == FIRST_ORDER_BILL, (
            f'Error calculating order bill, '
            f'{order_1_bill} != {FIRST_ORDER_BILL}'
        )
    # test validate_order method
    is_valid_x = carmines.validate_order(ORDER_X)[0]
    assert is_valid_x == True, (
            f'Error validating a valid order.'
        )
    is_valid_y = carmines.validate_order(ORDER_Y)[0]
    assert is_valid_y == False, (
            f'Error: validate and add an invalid order to queue.'
        )
    assert carmines.get_orders() == [ORDER_X], (
        f'Error adding valid order to queue'
    )

    
    
