# Python Conditional Statements — Smart Canteen Discount System

A beginner-friendly Python console program created during a Python lecture on **Conditional Statements**. It demonstrates how a program makes decisions using `if`, `elif`, and `else` in a realistic college-canteen scenario.

## Repository Name

`python-conditionals-smart-canteen`

## Class Demonstration

The class used a canteen bill to explain how conditional statements select one outcome from several possible outcomes.

| Bill Amount                  | Standard Discount |
| ---------------------------- | ----------------- |
| Rs. 3,000 or more            | 20%               |
| Rs. 2,000 to below Rs. 3,000 | 10%               |
| Rs. 1,000 to below Rs. 2,000 | 5%                |
| Below Rs. 1,000              | 0%                |

The program calculates the applicable discount and displays the original bill, discount amounts, total savings, and final payable amount.

## Concepts Covered

- `if`: Executes a block of code when a condition is true.
- `elif`: Checks another condition if previous conditions were false.
- `else`: Executes when none of the previous conditions are true.
- Nested `if` statements: Using conditional statements inside other conditional statements.
- Comparison operators: `>=`, `<=`, `==`, and `>`.
- Input using `input()`.
- Numeric conversion using `float()`.
- String methods using `.lower()`.
- Percentage calculations.
- F-strings for displaying variable values.
- Decimal formatting using `:.2f`.
- Conditional messages based on calculated results.

## Program Features

This version extends the original class demonstration with the following features:

1. **Bill Validation:** Rejects bill amounts that are zero or negative.
2. **Standard Discount:** Applies a discount based on the total bill amount.
3. **Membership Discount:** Asks whether the student has a membership card.
4. **Additional Savings:** Provides an extra 5% membership discount to eligible students.
5. **Total Savings:** Calculates and displays the combined discount amount.
6. **Final Bill Calculation:** Displays the amount the student needs to pay.
7. **Congratulations Message:** Shows a friendly message when a discount is applied.
8. **Formatted Bill Summary:** Displays all monetary values with two decimal places.

## Discount Calculation

The program calculates the membership discount separately on the original bill amount.

**Calculation Example:**

Suppose a student has a bill of Rs. 3,000 and a membership card.

| Description              | Calculation     | Amount    |
| ------------------------ | --------------- | --------- |
| Original Bill            | —               | Rs. 3,000 |
| Standard Discount (20%)  | 3000 × 20 / 100 | Rs. 600   |
| Membership Discount (5%) | 3000 × 5 / 100  | Rs. 150   |
| Total Savings            | 600 + 150       | Rs. 750   |
| Final Payable            | 3000 - 750      | Rs. 2,250 |

**Note:** The additional membership discount is calculated on the original bill, not on the remaining amount after the standard discount.

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```
python smart_canteen_discount.py
```

On some systems, use `python3` instead of `python`.

## Example Run

```
================================
       SMART CANTEEN
================================
Enter your total bill (Rs.): 3000
Do you have a membership card? (yes/no): yes

================================
          BILL SUMMARY
================================
Original Bill: Rs. 3000.00
Regular Discount: Rs. 600.00
Membership Discount: Rs. 150.00
Total Savings: Rs. 750.00
Final Payable: Rs. 2250.00

Congratulations! You saved Rs. 750.00

Thank you for visiting SMART CANTEEN!
```

## Invalid Bill Example

```
================================
       SMART CANTEEN
================================
Enter your total bill (Rs.): -500

Invalid Bill! Please enter a valid amount.

Thank you for visiting SMART CANTEEN!
```

## UI/UX Notes

This is a **console-based Python program**, not a graphical web interface.

Its basic user-experience features include:

- A clear program title and section separators.
- Simple input prompts.
- Currency labels (`Rs.`).
- Two decimal places for monetary values.
- A well-organized bill summary.
- Separate display of standard and membership discounts.
- Friendly messages for successful and invalid transactions.

These features make the program easier to use and understand for beginners.

## Practice Challenges

Try extending the program with these additional features:

1. Reject membership answers other than `yes` or `no`.
2. Display an invalid choice message for incorrect membership input.
3. If the bill is Rs. 5,000 or more, display a free drink message.
4. Add a maximum discount limit.
5. Display which standard discount tier was selected.
6. Ask the user whether they want to generate another bill.
7. Explain why `elif` is more suitable than several independent `if` statements in this scenario.

## Suggested Git Commit

```
Update smart canteen discount system with membership features
```

## Suggested Repository Description

Beginner-friendly Python project demonstrating conditional statements (`if`, `elif`, `else`), comparison operators, nested conditions, percentage calculations, membership discounts, and formatted bill summaries through a real-world canteen discount calculator.
