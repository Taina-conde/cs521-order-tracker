class OrderTracker():
    def __init__(self,restaurant_name = '', menu_dict = {}, orders_list = []):
        self.name = restaurant_name
        self.__menu = menu_dict
        self.orders = orders_list
    def __get_menu(self):
        return self.__menu


