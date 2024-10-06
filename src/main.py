# special imports
import os
import time
# as we make more scenario files add more import's with the file name here!
import sc1
import sc2

print("Welcome to WAIT!")
print("Choose a number between 1-10 and we will navigate you to that scenario (or type 999 to exit)")
num = input("Scenario to execute: ")

# construct module name
module_name = f"sc{num}"

# Get the module from globals
module = globals().get(module_name)

# Check if the module exists
if module:
    # Assuming the module has a function named `scenario` that you want to execute
    module.scenario()
else:
    print(f"Scenario {num} not found.")
    print("please try again!")
    time.sleep(5)
    os._exit
