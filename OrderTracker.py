class OrderTracker():
    def __init__(self,restaurant_name = '', menu_dict = {}, orders_list = []):
        self.name = restaurant_name
        self.__menu = menu_dict
        self.orders = orders_list
    def __repr__(self):
        return (
            f'{self.name} restaurant has '
            f'{len(self.orders)} orders beeing prepared'
        )
    def __get_menu(self):
        return self.__menu
    
# Unit tests
if __name__ == '__main__':
    carmines_restaurant = OrderTracker('Carmines', {
        'Margerita Pizza': 25,
        'Seafood linguine': 40.5,
        'Bruschetta': 16.55,
        'Tiramissu cake': 9,
    })
    print(carmines_restaurant)
