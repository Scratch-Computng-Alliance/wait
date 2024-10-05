import time
from datetime import datetime

def scenario():
    print("your stuck at a crosswalk and it keeps making you wait when will you be able to go?")
    
    while True:
        # time
        current_time = datetime.now()
        
        # check time
        if current_time.hour == 12 and current_time.minute == 0 and current_time.second == 0:
            print("you waited!")
            print("if you can cross the whole thing in the next minute then do so! else, come back and WAIT.")
            time.sleep(10)
            break
        
        # wait another second.
        time.sleep(1)
