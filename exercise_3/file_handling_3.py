# Diong, Shan Marc C.
# BSCPE 1-2

# Create a function to make a text file, name it mylife.txt. Open and write the text file
def text_to_file():
    with open("mylife.txt", "w") as mylife_file:

# Ask the user what to write in the text file, then press ENTER when they are finished.
        while True:
            user_input = input("\nEnter a line of text or just press ENTER to finish: ")
            if user_input == "":
                break
            mylife_file.write(user_input + "\n")


# Transfer the lines and make the text file
text_to_file()
print("Lines written in 'myfile.txt' has been added succesfully")

