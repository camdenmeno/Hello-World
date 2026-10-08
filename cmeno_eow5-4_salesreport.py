# Camden Meno
# 9/24/2026
# Week 5 - End of Week Assignment - Exercise 4


print("4.")

# sales report

while True:
    sale = input("Enter a sales amount (or type 'done' to finish): ")
    
    if sale.lower() == "done":
        break
    with open(sales_report.txt, "a"):
as file:
    file.write(f"{float(sale):.2f}\n")
    
print("Sales entry complete. Values saved to sales_report.txt")
