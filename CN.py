# Python version of the Password Generator

# Function to generate password
def generate_password(name, roll_no, reg_no, dob):
    # Extracting the dynamic password components
    first_letter_name = name[0].upper()  # First letter of name in uppercase
    last_letter_name = name[-1].lower()  # Last letter of name in lowercase
    
    last_two_roll_no = roll_no[-2:]  # Last 2 digits of roll number
    first_roll_no = roll_no[0]  # First digit of roll number
    
    first_two_reg_no = reg_no[:2]  # First 2 digits of registration number
    last_three_reg_no = reg_no[-3:]  # Last 3 digits of registration number
    
    dob_parts = dob.split("-")  # Split DOB into day, month, year
    year = dob_parts[2]  # Year part
    day = dob_parts[0]  # Day part
    month = dob_parts[1]  # Month part
    last_two_dob_year = year[-2:]  # Last 2 digits of the year
    first_day = day[0]  # First digit of the day
    first_month = month[0]  # First digit of the month

    # Construct the password
    generated_password = (first_letter_name + last_letter_name + last_two_roll_no + first_roll_no +
                          first_two_reg_no + last_three_reg_no + last_two_dob_year + first_day + first_month)
    
    return generated_password

# Main program starts here
if __name__ == "__main__":
    # Input details from user
    name = input("Enter your Name: ")
    roll_no = input("Enter your Roll Number: ")
    reg_no = input("Enter your Registration Number: ")
    dob = input("Enter your Date of Birth (dd-mm-yyyy): ")

    # Generate password
    generated_password = generate_password(name, roll_no, reg_no, dob)

    # Display the generated password
    print(f"Generated Password: {generated_password}")

    # Input the password from the user and validate
    input_password = input("Please enter the displayed password: ")

    if input_password == generated_password:
        print("Password validated successfully!")
        print(f"User Name: {name}")
        print(f"Password: {generated_password}")
    else:
        print("Password validation failed. Please try again.")
