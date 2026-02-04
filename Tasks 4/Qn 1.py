# Create Odd and Even Number List from the given List

nums = [10, 501, 22, 37, 100, 999, 87, 351]

# To save the Value
even_number = []
odd_number = []

# Loop to check all the numbers
for n in nums:
    if n % 2 == 0:
        even_number.append(n)
    else:
        odd_number.append(n)

# Print the values after the loop ends
print("Even numbers:- ", even_number)
print("Odd numbers:- ", odd_number)
