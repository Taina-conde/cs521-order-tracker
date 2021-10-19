"""
Taina Batista Conde
Class: CS 521 - Fall 1
Date: 10/19/2021
Final Project
Description: Main program using OrderTracker class

"""
from OrderTracker import OrderTracker

if __name__ == '__main__':
    menu_dict = {}
    name_str = ''
    with open('fratellos_menu.txt', 'r') as input_file:
        for num, line_str in enumerate(input_file):
            # The first line of the file is the restaurant's name
            if num == 0 :
                name_str += line_str
            else:
                stripped_str = line_str.strip()
                # consider only the lines that have content to create the 
                # menu dictionary
                if stripped_str != '':
                    line_list = stripped_str.split(':')
                    print(line_list)
                    # transform the keys to uppercase to make them uniform
                    menu_dict[line_list[0].upper()] = float(line_list[1])
        
        print('menu dict', menu_dict)
        print('name : ', name_str)


