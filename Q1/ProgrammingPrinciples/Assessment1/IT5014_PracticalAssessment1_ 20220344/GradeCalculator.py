'''
Task 2: Grade calculator

Takes two scores: one for a project, and one for an exam. Each contributes 50%
to the final grade. Grade boundaries are as shown in the following table:

+---------------+-------+
|  Percentage   | Score |
+---------------+-------+
| 80 or above   |   A   |
| 70 to 79      |   B   |
| 60 to 69      |   C   |
| 50 to 59      |   D   |
| 49 and below  | Fail  |
+---------------+-------+
'''

# Print welcome message and ask for two scores; cast them to integers
print("\nWelcome to the Grade Calculator. Please enter your grades.")
project_score = int(input("What did you receieve on the project? "))
exam_score = int(input("What did you receive on the exam? "))

# Calculate the total grade percentage; each mark is worth 50%
percentage = (project_score + exam_score) * .5

# Work out corresponding letter grade, starting with Fail (less than 50)
if percentage < 50:
    grade = "fail"
elif percentage >= 50 and percentage < 60:
    grade = "D"
elif percentage >= 60 and percentage < 70:
    grade = "C"
elif percentage >= 70 and percentage < 80:
    grade = "B"
elif percentage >= 80:
    grade = "A"

# Concatenate grade into report string and print out
print("You received a " + grade + " grade.\n")

# This program fulfils the following test-case assertion:
#
# Given input of "78" for the project, and "65" for the exam (71.5%),
# the program calculates a "B" grade.

# NB: The program assumes the user enters two positive integers; simple error-
# handling could be added in an `else` block after the last `elif` to deal
# with the entry of the numeral `0`, negative integers, and text strings.
