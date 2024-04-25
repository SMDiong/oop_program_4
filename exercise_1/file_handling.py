# Diong, Shan Marc C.
# BSCPE 1-2

# Word Format and Text to Speech
green = "\033[0;32m"

# Create a text file that contain 20 integers, name it numbers.txt
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
print(green + "Files 'even.txt' and 'odd.txt' have been created successfully.")