# A program that manages and analyzes student grades
# Main program initialization and welcome
print("Welcome to my Grade Sorter App")
user_grades = []

# Input validation function that ensures grades are numbers between 0-100
# and provides helpful error messages for invalid inputs
def get_valid_grade(prompt):
    while True:
        try:
            grade = int(input(prompt))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

# Collecting four validated grades from the user
user_grades.append(get_valid_grade("What is your first grade (0-100): "))
user_grades.append(get_valid_grade("What is your second grade (0-100): "))
user_grades.append(get_valid_grade("What is your third grade (0-100): "))
user_grades.append(get_valid_grade("What is your fourth grade (0-100): "))

# Displaying the original unsorted grade list
print(f"\nYour grades are {user_grades}")

# Sorting mechanism for organizing grades in descending order
user_grades.sort(reverse=True)
print(f"\nYour grades from highest to lowest are: {user_grades}")

# Grade removal section - eliminates the two lowest scores
print("\nThe lowest two grades will now be dropped")
removed_grade1= user_grades.pop()
print(f"Removed grade: {removed_grade1}" )
removed_grade2= user_grades.pop()
print(f"Removed grade: {removed_grade2}")

# Final results display
print(f"\nYour remaining grades are: {user_grades}")
print(f"Nice work! Your highest grade is {user_grades[0]}")
print("\nThank you for testing my App! ")