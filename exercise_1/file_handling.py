# Diong, Shan Marc C.
# BSCPE 1-2

# Word Format and Text to Speech
import pyttsx3
text_to_speech = pyttsx3.init()
voices = text_to_speech.getProperty('voices')
text_to_speech.setProperty('voice', voices[1].id)
text_to_speech.setProperty('rate', 150)
green = "\033[0;32m"
blue = "\033[0;34m"

# Create a text file that contains 20 integers, name it numbers.txt then read it
with open('numbers.txt', 'r') as numbers_file:
    integer = [int(line.strip()) for line in numbers_file]

# Separate even and odd numbers
even_numbers = [num for num in integer if num % 2 == 0]
odd_numbers = [num for num in integer if num % 2 != 0]

# Create a code which create a text file that contains all even numbers extracted from number.txt, name it even.txt
with open('even.txt', 'w') as even_file:
    for num in even_numbers:
        even_file.write(str(num) + '\n')

# Create a code which create a text file that contains all odd numbers extracted from number.txt, name it odd.txt
with open('odd.txt', 'w') as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + '\n')

# Output Text
output_speech = "Text files 'even.txt' and 'odd.txt' have been created successfully."
print(green + f"\n Text files {blue + 'even.txt' + green} and {blue + 'odd.txt' + green} have been created successfully.")
text_to_speech.say(output_speech)
text_to_speech.runAndWait()

# End