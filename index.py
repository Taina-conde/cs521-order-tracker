"""
Taina Batista Conde
Class: CS 521 - Fall 1
Date: 10/19/2021
Final Project
Description: Main program using OrderTracker class

"""
from OrderTracker import OrderTracker

def read_menu(file_str):
    """Reads a file that contains a restaurant's menu, and returns
    the restaurants name as string and the menu as dictionary"""
    menu_dict = {}
    name_str = ''
    with open('fratellos_menu.txt', 'r') as input_file:
        for num, line_str in enumerate(input_file):
            # The first line of the file is the restaurant's name
            if num == 0 :
                name_str += line_str.strip()
            else:
                stripped_str = line_str.strip()
                # consider only the lines that have content to create the 
                # menu dictionary
                if stripped_str != '':
                    line_list = stripped_str.split(':')
                    # transform the keys to uppercase to make them uniform
                    menu_dict[line_list[0].upper()] = float(line_list[1])
    return name_str, menu_dict

def get_order():
    """ Prompts the user for one order item at a time and returns
    the a set with the order items, quantities in tuples"""
    order_set = set()
    is_order_done = False
    while is_order_done == False:
        if len(order_set) != 0:
            is_done_input = input('Anything else: y/n ')
            if is_done_input.lower() != 'y' and is_done_input.lower() != 'n':
                print(
                    'Enter y to continue ordering or n if you are done'
                )
                continue
            if is_done_input.lower() == 'n':
                is_order_done = True
        while is_order_done == False:
            order_input = input(
                    'Enter one order item and quantity separated by a comma '
                    '- for example - Your Dish, 1 : '
                    )
            try:
                item_quantity_list = order_input.split(',')
                if len(item_quantity_list) >= 3:
                    raise IndexError
                item = item_quantity_list[0].strip()
                quant = int(item_quantity_list[1].strip())
                if item.isdigit() == True:
                    raise ValueError

            except ValueError: 
                print(
                    'The first element must be a string and the '
                    'second an integer'
                    )
            
            except IndexError:
                print(
                    'Please, enter one item and the quantity comma-separated.'
                    )
            else:
                item_quantity_tuple = (item.upper(), quant)
                order_set.add(item_quantity_tuple)
                break
    return order_set

def print_bill(restaurant_name, order, total_price): 
    """Writes an output file with the order bill """
    out_file = open('bill.txt', 'w')
    out_file.write(f'{restaurant_name} \n')
    for item_tuple in order:
        out_file.write(
            f'{item_tuple[0].capitalize()} #{item_tuple[1]} \n'
        )
    out_file.write(f'Total price: {total_price}')
    out_file.close()

if __name__ == '__main__':
    name_str, menu_dict = read_menu('fratellos_menu.txt')
    # finished reading the file and getting the necessary info from it.
    # create instance of OrderTracker
    fratellos = OrderTracker(name_str, menu_dict)

    # prompt the user to make a new order until he/she makes a valid order
    # the order is invalid if one of the items is not in the menu
    # make two orders just to test the program
    for num in range(2):
        print('-' * 79)
        is_valid = False
        while is_valid == False:
            print(f'# ORDER NUMBER {num + 1}')
            new_order = get_order()
            is_valid, message = fratellos.validate_order(new_order)
            print(message)
            print('-' * 79)

    print(fratellos)
    order_ready = fratellos.prepare_order()
    print('. \n . \n .')
    print(f'Order of {order_ready} is ready! Enjoy!')
    print('. \n . \n .')
    print(f'Calculating the bill ...')
    bill_float = fratellos.calculate_bill(order_ready)
    print_bill(fratellos.name, order_ready, bill_float )
    


    

    
    
   





        

        

    

    



