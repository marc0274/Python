'''
Code Challenge #8: Shopping Cart

See README on GITHUB for instructions

Program Analysis

Inputs: price, name, quantity

Outputs:product name, price, quantity, total, tax, subtotal

Algorithm: sub = price * qt, ta = stotal * .08,  tot = sub + tax, get user input for product name, price, and quantity. Then put it in a dictionary,
add dictionary to a list, print out the total, subtotal and tax, along with everything in list.

'''


# Write your code here
import json

products = []

f = "shopping_cart.save"

def read():
    with open(f, 'r') as fs:
        string_text = fs.read()
        products = json.loads(string_text)

def writefile():
    with open(f,'w') as fs:
        fs.write(json.dumps(products))
            



def carttotal(price,qt):
    sub = price * qt
    
    return sub




def tax(stotal):
    ta = stotal * .08
    return ta

def Total(sub, tax):
    tot = sub + tax
    return tot


read()
while True:

    cart = {}

    print("MENU: \n[1] Add a product\n[2] Remove a product\n[3] Print the shopping cart\n[4] Quit Program")
    menu = input("Please select a number: ")

    if menu == '1':
        print("Add a Product")
        
        nm = input("Enter a name:  ")
        

        prc = float(input("Enter the unit price: "))
        

        qnt = int(input("Enter the quantity: "))
         
        cart['Name'] = nm
        cart['Price'] = prc
        cart['Quantity'] = qnt 
        products.append(cart)

        print("Item added!")

        print("")
        print("")
        continue

  
    
    if menu == '2':
        rem = input("Enter the name of the item to remove: ")
        if rem in cart:
            try:
                map(cart.pop, ['Name:','Price','Quantity'])
                print("item removed")
                print("")
                print("")
        
            except:
                print("Please enter a valid item")
                print("")
                print("")
                continue
    
    if menu == '3':
        

        z = 0.00
        print("")
        print("")
        print("Your Shopping Cart")
        print("-"*55)
        print("Name"," "*20, "|   Price   | Qty | Sub-Total")
        print("-"*55)
        
    
        for cart in products:
            z = z + carttotal(cart['Price'],cart['Quantity'])
            y = carttotal(cart['Price'],cart['Quantity'])
            print("{}                       |   ${}   |  {}  | ${}".format(cart['Name'],cart['Price'],cart['Quantity'],y))
            
        print("-"*55)
        
        taxes = tax(z)
        finish = Total(z,taxes)
        print("                                  Sub Total | ${} \n                             Sales Tax (8%) | ${} \n                                      Total | ${}".format(z,taxes,finish))
    
    if menu == '4':
        writefile()
        print("Shopping List Saved!")
        print("Program exited")
        break


'''

Questions:

What are the datatypes needed for the product dictionary?
For the product dictionary you need strings, int, and float.

How many functions did you use in your program, your function analysis should tell me what they are for. Why did you decide on the functions you chose?
my program used 3 functions. These functions do all the math to calculate the taxes, subtotal, and total. They made it easy to bring the math in.

What list and dictionary methods did you use and what lines numbers do they appear on? What does each method do?
Quick question I have is why dictionaries can't add stuff inside a if statement? The dictionary and list method are on the 35th and 40th line. One method creates a list where the
dictionary can go in. The other method is the dictionary where the price, name, and quantity of the products are stored from the user input.

'''
