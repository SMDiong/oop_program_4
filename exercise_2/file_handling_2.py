# Diong, Shan Marc C.
# BSCPE 1-2

# Create a text file that contains the name of 20 students with their GWA then read it
with open('student_name_gwa.txt', 'r') as student_file:
    lines = student_file.readlines()

# Determine the highest GWA value
    highest_gwa = 5.0
    highest_gwa_student = ""

# Separate the student's name and the GWA
for line in lines:
    student_name, student_gwa = line.strip().split(" - GWA: ")
    student_gwa = float(student_gwa)

# Check the highest GWA of all the students
    if student_gwa < highest_gwa:
        highest_gwa = student_gwa
        highest_gwa_student = student_name

# Output the name and GWA of the student who got the highest GWA
print(f"The student with the highest GWA is {highest_gwa_student} with a GWA of {highest_gwa}.")
