# Syed Abidi - DSC510 - Assignment  Week-2

# The Purpose of this program is to calculate the cost of fiber Optic
print ("Welcome")
company = input("what's your company name? \n")
fiber_length = float(input("What's the length of optic cable in feet?\n"))
print ("Here is your receipt: ")

install_cost = fiber_length * 0.87

print("The Company name is: " + company)
print("The fiber length to install: " ,fiber_length,  "feet" + "\n" +  "Calculated cost is: $0.87/foot")
print("Total installation cost is: $", install_cost)
