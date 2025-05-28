# Create Flat Rent Calculator

flat_rent = int(input("Enter the flat rent: "))
food_bill = int(input("Enter the food bill: "))
electricity_bill = int(input("Enter the electricity bill: "))
water_bill = int(input("Enter the water bill: "))
internet_bill = int(input("Enter the internet bill: "))
electricity_per_unit = int(input("Enter the units consumed: "))
gas_bill = int(input("Enter the gas bill: "))

#total living person
person = int(input("Enter the number of person: "))

#total electricity bill
current_bill = electricity_bill * electricity_per_unit

# calculate total bill
total_bill = (flat_rent + food_bill + current_bill + water_bill + internet_bill + gas_bill)// person

print("Each person pay : ",total_bill)