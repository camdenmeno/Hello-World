# Camden Meno
# 9/24/2026
# Week 5 - End of Week Assignment - Exercise 3


print("3.")

# extract file
with open("transactions.txt", "r") as file:
    for line in file:
        customer, amountdue = line.strip().split(",")

        # print result
        print(f"Customer: {str(customer)} | Amount Due: ${float(amountdue)}")
