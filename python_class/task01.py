def calculate_percentage(total_marks, num_subj):
    return total_marks / num_subj

def calculate_grade(percentage):

#     if percentage >= 90:
#         print("A+")
#     elif percentage >= 80:
#         print("A")
#     elif percentage >= 70:
#         print("B")
#     elif percentage >= 60:
#         print("C")      
#     elif percentage >= 50:
#         print("D")
#     else:
#         print("F")

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Student Grade Calculator

name = input("Enter your Name: ")

m1 = float (input("Enter marks for subj 01: "))
m2 = float (input("Enter marks for subj 02: "))
m3 = float (input("Enter marks for subj 03: ")) 
m4 = float (input("Enter marks for subj 04: "))
m5 = float (input("Enter marks for subj 05: "))

total = m1 + m2 + m3 + m4 + m5

percentage = calculate_percentage(total, 5)
grade = calculate_grade(percentage)

# Result

print ("Name: ", name)
print ("Total_marks: ", total)
print ("Percentage: ", percentage)
print ("Grade: ", grade)