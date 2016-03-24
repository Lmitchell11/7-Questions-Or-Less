# Liam Mitchell (CMU IEEE Club)
# 3/19/2016
# 7 Questions Or Less
# 7QorLess.py

# Will be using sleep
import time
from time import sleep
import re
import Adafruit_CharLCD as LCD


# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()


# Initialize Buttons
buttons = ((LCD.SELECT, 'Start'), (LCD.LEFT,   'Left'), (LCD.RIGHT,  'Right'))


# Questions Loop
def stringSearcher(Answer):
        f = open("QuestionTree.txt", "r")
        currentLine = f.readline()
        for line in f:
                if re.match(Answer, line):      # Uses the match function from re.match(), because of characters in string, and length of string
                        yesnos, answerOrQuestion = line.split(',')
                        return answerOrQuestion, yesnos


# Stop the program using the terminal
print 'Press Ctrl-C to quit.'


# Global variables
counter = 0
delayLong = 2.0  # two seconds
delayShort = 0.1 # one tenth of a second
loopTime =  100  # tenseconds as 100 * 0.1 = 10
selectPressed = lcd.is_pressed(LCD.SELECT) # used incase someone holds their finger for too long
print 'Start Message'   #So you can see that the program has started through the terminal


# Start Message
i = 0                           # initializes Time Counter
while not selectPressed:        # Select will Start the game, might have to hold it for a second, it also ends the game.

	if i == 0:              #
		# display message then sleep
		lcd.clear()
		lcd.message("7 QUESTIONS \n    OR LESS")        # Game Title on LCD Screen
		time.sleep(4)                                   # Sleeps 4 Seconds

		
		# display message then sleep
		lcd.clear()
                print "PRESS SELECT TO START"                   # Lets you know when you can push the SELECT-Button
		lcd.message("Press SELECT \nTo Start")          # Action button to initiate/start the game
		time.sleep(delayShort)

		
	# checking for select pressed, but don't load cpu so sleep
	selectPressed = lcd.is_pressed(LCD.SELECT)
	time.sleep(delayShort)


	# reprompt message over ten seconds
	i = (i + 1)%loopTime


# Start Message over reset selectPressed and clear screen
selectPressed = False           #Initializes selectPressed for the while loop below
lcd.clear()
print "******7 Questions or Less******"        #Says game has Start in the Terminal
Answer = ""     #Initializes answer because it has to be ("Terminal says so")


# 7QorLess Messages
i = 0
curr = 0
while not selectPressed:
        ans = ""        # Clear ans every loop
        answerOrQuestion, yesnos = stringSearcher(Answer) #Must define return variables to use them

	# Display current message
        if i == 0:
                if Answer == yesnos:
                        lcd.clear()
                        lcd.message(answerOrQuestion) 

	# Check for pressed buttons
	if lcd.is_pressed(LCD.LEFT):            # LEFT-Button input
		ans = "Yes"                     # Sets up string for user-answer feedback & also for delay, "to reduce risk of user-mistakes"
		Answer = ''.join((Answer, 'Y'))         # Adds Character/Choice to the end of "Answer" String for next question from file
                print Answer                            # Displays Answer in the terminal

	elif lcd.is_pressed(LCD.RIGHT):         # RIGHT-Button action input
		ans = "No"
		Answer = ''.join((Answer, 'N'))         
		print Answer                            

	
	# If there was an answer display it
	if ans:
		# Display message then sleep
		lcd.clear()
		lcd.message(ans)
		time.sleep(delayLong)

		# Increment the current message and display next question
		curr += 1
		i = loopTime - 1
		

	# Checking for any button pressed, but don't load cpu so sleep
	selectPressed = lcd.is_pressed(LCD.SELECT)
	time.sleep(delayShort)

	# Reprompt message over ten seconds
	i = (i + 1)%loopTime
