# Diong, Shan Marc C.
# BSCPE 1-2

# Word Format and Text to Speech
import pyttsx3
text_to_speech = pyttsx3.init()
text_to_speech.setProperty('rate', 150)
green = "\033[0;32m"
blue = "\033[0;34m"

# Create the source text file named integers.txt that contains 20 integers

# Create the function that will create two separate text files extracted from integers.txt
def even_odd_integers():
    with open("integers.txt", "r") as source_file:
        integers = [int(line.strip()) for line in source_file]
    even_numbers = []
    odd_numbers = []

# Separate the odd and even numbers
    for numbers in integers:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
        else:
            odd_numbers.append(numbers)

# Calculate the squares of even numbers then create and write it to double.txt
    with open("double.txt", "w") as double_file:
        for num in even_numbers:
            square = num ** 2
            double_file.write(str(square) + "\n")
    print(green + "\nEven numbers extracted and calculated.")

# Calculate the cubes of odd numbers then create and write it to triple.txt
    with open("triple.txt", "w") as triple_file:
        for num in odd_numbers:
            cube = num ** 3
            triple_file.write(str(cube) + "\n")
    print("\nOdd numbers extracted and calculated.")

# Call the function to create the files then an output message
even_odd_integers()
output_speech = "Text files 'double.txt' and 'triple.txt' have been created successfully."
print(f"\nText files {blue + 'double.txt' + green} and {blue + 'triple.txt' + green} have been created successfully.")
text_to_speech.say(output_speech)
text_to_speech.runAndWait()

# End