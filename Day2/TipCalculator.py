# Function to calculate tip and split the bill
def calculate_tip_and_split_bill():
    # Get user input
    total_bill = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
    number_of_persons = int(input("Enter the number of persons to split the bill: "))

    # Calculate tip and total amount
    tip_amount = total_bill * (tip_percentage / 100)
    total_amount = total_bill + tip_amount

    # Split the bill
    amount_per_person = total_amount / number_of_persons

    # Display the results
    print(f"\nTip Amount: ${tip_amount:.2f}")
    print(f"Total Amount (including tip): ${total_amount:.2f}")
    print(f"Amount per person: ${amount_per_person:.2f}")

# Run the program
calculate_tip_and_split_bill()
