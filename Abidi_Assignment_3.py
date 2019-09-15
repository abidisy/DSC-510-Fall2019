# File: Abidi_Assignment_3.py
# Name: Syed Abidi
# Date: 09/13/2019
# Course: DSC510: Introduction to Programming

# Display a welcome message for your program.
print('Welcome to the Fiber Optic installation Calculator')
print('This program will calculate the Discount depending on the Fiber cable length purchased by the customer\n')

# Get the company name from the user.
company_name = input('What is the name of your company name? \n' )

# Get the number of feet of fiber optic cable to be installed from the user.
cable_length = float(input("Enter the cable length in feet?  \n"))
x = cable_length



# Evaluate the total cost based upon the number of feet requested.
# The cost of fiber optic cable installation by multiplying the number of feet needed by $0.87.
if x <= 100:
    y = 0.87 * x    # the cost of installation by multiplying cable length and installation charges of $0.87/foot
    print (company_name + ' will pay total installation charges of $',y, 'for the cable length of' ,x, 'feet with the price of $','0.87/feet')


# Evaluate the total cost based upon the number of feet requested.
# The cost of fiber optic cable installation by multiplying the number of feet needed by $0.80
elif x > 100 and x <= 250 :
    y = 0.80 * x    # the cost of installation by multiplying cable length and installation charges of $0.80/foot
    print (company_name + ' will pay total installation charges of $',y, 'for the cable length of' ,x, 'feet with the price of $','0.80/feet')


# Evaluate the total cost based upon the number of feet requested.
# The cost of fiber optic cable installation by multiplying the number of feet needed by $0.70
elif x > 250 and x <= 500 :
    y = 0.70 * x    # the cost of installation by multiplying cable length and installation charges of $0.70/foot
# Display the calculated information including the number of feet requested and company name.
    print (company_name + ' will pay total installation charges of $',y, 'for the cable length of' ,x, 'feet with the price of $','0.70/feet')


# Evaluate the total cost based upon the number of feet requested.
# The cost of fiber optic cable installation by multiplying the number of feet needed by $0.50
elif x > 500 :
    y = 0.50 * x    # the cost of installation by multiplying cable length and installation charges of $0.50/foot
# Display the calculated information including the number of feet requested and company name.
    print (company_name + ' will pay total installation charges of $',y, 'for the cable length of' ,x, 'feet with the price of $','0.50/feet')


else:
    print('Invalid Entry')

