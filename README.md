# Restaurant Order Tracker

This program is a restaurant order tracker. It reads a restaurant's menu file and creates an instance of OrderTracker class using that restaurant's name and menu retrieved from the file. Then, it prompts the user twice for orders to simulate two different customers making their orders in a real restaurant. The program uses a method from the OrderTracker class called validate_order that first checks if the items ordered are part of the restaurant's menu. If they are, the order is added to the queue, otherwise, the user is prompted to make the order again. 
To simulate a real restaurant, the orders are prepared on a first-in first-out basis. Therefore, when the program calls the prepare_order method, the first order that the user entered is prepared and removed from the list of orders. 
Lastly, the program calculates that order's bill and creates an output file called 'bill.txt' with the restaurant's name, the items and quantities ordered, and the total price. 
A further developed version of this program could help restaurants organize their orders in an automated system, which reduces the chance of errors, speeds up the ordering process, maximizes productivity, and, consequentially, makes the business more profitable.  

## Documentation

The following files are needed for the program:
* index.py
* fratellos_menu.txt
* OrderTracker.py

## Instructions

Open the index.py file and run the code in a code editor.
No third-party libraries are needed. 