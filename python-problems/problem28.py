amount = float(input("Enter bill amount: "))
discount = float(input("Enter discount %: "))

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("\n----- BILL SUMMARY -----")
print(f"Original Amount : {amount:.2f}")
print(f"Discount        : {discount:.2f}%")
print(f"Discount Amount : {discount_amount:.2f}")
print(f"Final Payable   : {final_amount:.2f}")