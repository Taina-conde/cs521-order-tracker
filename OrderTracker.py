class OrderTracker():
    def __init__(self,restaurant_name = '', menu_dict = {}, orders_list = []):
        self.name = restaurant_name
        self.menu = menu_dict
        self.__orders = orders_list
    def __repr__(self):
        return (
            f'{self.name} restaurant has '
            f'{len(self.__orders)} orders beeing prepared'
        )
    def __get_orders(self):
        return self.__orders

    def add_order(self, order):
        orders_list = self.__get_orders()
        orders_list.append(order)
        return self.__orders
    
    def prepare_order(self):
        orders_list = self.__get_orders()
        return orders_list.pop(0)
    
    
    
    
# Unit tests
if __name__ == '__main__':
    carmines_restaurant = OrderTracker('Carmines', {
        'Margerita Pizza': 25,
        'Seafood linguine': 40.5,
        'Bruschetta': 16.55,
        'Tiramissu cake': 9,
    })
    print(carmines_restaurant)
