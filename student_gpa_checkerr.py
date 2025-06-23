# Name: Dima Hassan
# File Name: student_gpa_checker.py
# Description: This app accepts student names and GPAs, then determines if they qualify
#              for the Dean's List (GPA >= 3.5) or the Honor Roll (GPA >= 3.25).

def main():
    """
    Main function to run the student GPA checker application.
    """
    print("Welcome to the Student GPA Checker!")
    print("Enter 'zzz' for the last name to quit at any time.")

    while True:
        # Ask for and accept the student's last name
        last_name = input("\nEnter student's last name: ").strip()

        # Quit processing student records if the last name entered is 'zzz'
        if last_name.upper() == 'zzz':
            print("Exiting application. Goodbye!")
            break

        # Ask for and accept a student's first name
        first_name = input("Enter student's first name: ").strip()

        # Ask for and accept the student's GPA as a float
        while True:
            try:
                gpa_str = input("Enter student's GPA: ").strip()
                gpa = float(gpa_str)
                if not (0.0 <= gpa <= 4.0): # Optional: Basic GPA validation
                    print("GPA must be between 0.0 and 4.0. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid GPA. Please enter a numerical value (e.g., 3.75).")

        print(f"\nProcessing record for: {first_name} {last_name} (GPA: {gpa:.2f})")

        # Test if the student's GPA is 3.5 or greater
        if gpa >= 3.5:
            print(f"Congratulations, {first_name} {last_name}! You have made the Dean's List!")
        # Test if the student's GPA is 3.25 or greater but less than 3.5
        elif gpa >= 3.25:
            print(f"Well done, {first_name} {last_name}! You have made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll at this time.")

if __name__ == "__main__":
    main()
