import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)    # Speed of speech (words per minute )
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
# Prompt the user to enter text
print("|*******************************************************|")
print("|                                                       |")
print("|                                                       |")
print("|     W E L C O M E   T O   T E X T  T O  S P E E C H   |")
print("|                   C O N V E R S I O N                 |")
print("|                                                       |")
print("|                                                       |")
print("|*******************************************************|")
print("\n")
text = input("PLEASE ENTER YOUR TEXT HERE ->")
# Convert text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
