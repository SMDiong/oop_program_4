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

# Create a function to make a text file, name it mylife.txt. Open and write the text file
def text_to_file():
    with open("mylife.txt", "w") as mylife_file:

        # Ask the user what to write in the text file, then press ENTER when they are finished.
        input_speech = "Enter a line of text or press ENTER to finish"
        text_to_speech.say(input_speech)
        text_to_speech.runAndWait()
        while True:
            user_input = input(blue + "\nEnter a line of text or press ENTER to finish: ")
            if user_input == "":
                break
            mylife_file.write(user_input + "\n")

# Transfer the lines and make the text file
text_to_file()
output_speech = "Lines written in 'mylife.txt' has been added succesfully. The lines are..."
print(green + f"\nLines written in {blue + 'mylife.txt' + green} has been added succesfully. The lines are...")
text_to_speech.say(output_speech)
text_to_speech.runAndWait()

# Open and read the file by Text to Speech
with open("mylife.txt", "r") as speech_file:
    lines = speech_file.readlines()

# Also output the text written
for line in lines:
    print("\n" + blue + line.strip())
    text_to_speech.say(line)
    text_to_speech.runAndWait()

# End