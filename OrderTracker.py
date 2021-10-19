class OrderTracker():
    def __init__(self,restaurant_name = '', menu_dict = {}, orders_list = []):
        self.name = restaurant_name
        self.__menu = menu_dict
        self.orders = orders_list
    def __repr__(self):
        return (
            f'{self.name} restaurant has'
            f'{len(self.orders)} orders beeing prepared'
        )
    def __get_menu(self):
        return self.__menu
    


