#if-else conditional statements

m=12


if m<20:
    print(m, "is the smaller number")
else:
    print(m, "is bigger than 20")

#Write to check if a person is buying oranges at 100 rs and later selling it 1 at 120 rs. Find that he has profit or loss?

actual_cost=float(input("Enter the actual cost"))# input is for taking the value from the user
selling_cost=float(input('Enter the estimated answer'))

if selling_cost>actual_cost:
    profit = selling_cost-actual_cost
    print(profit)
else:
    print('loss')
    
