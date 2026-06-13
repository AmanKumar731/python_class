# def greet( name= "Guest"):
#     print("Welcome " + name)

# greet("Aman")




# function with parameters and no return value

balance = 1000.00
def update_balance(amount=500.00):
    new_balance = balance + amount
    print("Balance updated successfully. New balance: " + str(new_balance))

update_balance()


# #function with parameters and return value
# def calculate_total_bill(rate, quantity):
#     total = rate * quantity
#     return total