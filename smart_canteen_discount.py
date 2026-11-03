
print("================================")
print("       SMART CANTEEN")
print("================================")

# Taking input from the user
bill_amount = float(input("Enter your total bill (Rs.): "))

# Checking whether the bill is valid
if bill_amount <= 0:

    print("\nInvalid Bill! Please enter a valid amount.")

else:

    # Checking discount eligibility
    if bill_amount >= 3000:
        discount_rate = 20

    elif bill_amount >= 2000:
        discount_rate = 10

    elif bill_amount >= 1000:
        discount_rate = 5

    else:
        discount_rate = 0

    # Asking about membership
    membership = input("Do you have a membership card? (yes/no): ").lower()

    # Calculating discount
    discount_amount = bill_amount * discount_rate / 100

    # Additional membership discount
    if membership == "yes":
        membership_discount = bill_amount * 5 / 100
    else:
        membership_discount = 0

    # Total discount
    total_discount = discount_amount + membership_discount

    # Final payable amount
    final_amount = bill_amount - total_discount

    # Displaying bill summary
    print("\n================================")
    print("          BILL SUMMARY")
    print("================================")

    print(f"Original Bill: Rs. {bill_amount:.2f}")
    print(f"Regular Discount: Rs. {discount_amount:.2f}")
    print(f"Membership Discount: Rs. {membership_discount:.2f}")
    print(f"Total Savings: Rs. {total_discount:.2f}")
    print(f"Final Payable: Rs. {final_amount:.2f}")

    # Congratulations message
    if total_discount > 0:
        print(f"\nCongratulations! You saved Rs. {total_discount:.2f}")

    else:
        print("\nThank you for shopping with us!")
        print("Visit again to enjoy exciting discounts!")

print("\nThank you for visiting SMART CANTEEN!")
