# Diong, Shan Marc C.
# BSCPE 1-2

# Word Format and Text to Speech
import pyttsx3
text_to_speech = pyttsx3.init()
text_to_speech.setProperty('rate', 150)
green = "\033[0;32m"
blue = "\033[0;34m"

# Create a text file that contains the name of 20 students with their GWA then open and read it
with open('student_name_gwa.txt', 'r') as student_file:
    lines = student_file.readlines()

# Determine the highest GWA value
    highest_gwa = 5.0
    highest_gwa_student = ""

# Separate the student's name and their GWA
for line in lines:
    student_name, student_gwa = line.strip().split(" - GWA: ")
    student_gwa = float(student_gwa)

# Check the highest GWA of all the students
    if student_gwa < highest_gwa:
        highest_gwa = student_gwa
        highest_gwa_student = student_name

# Output the name and GWA of the student who got the highest GWA
output_speech = f"The student with the highest GWA is {highest_gwa_student} with a GWA of {highest_gwa}."
print(green + f"\nThe student with the highest GWA is {blue + highest_gwa_student + green} with a GWA of {blue + str(highest_gwa) + green}.")
text_to_speech.say(output_speech)
text_to_speech.runAndWait()

# End