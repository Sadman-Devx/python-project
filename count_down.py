# digital count down 

import time
import winsound
while True:
    try:
        my_time = int(input("Enter the time for countdown: "))

        for i in range(my_time, -1, -1):
            seconds = i % 60 #calculate seconds
            minutes = (i // 60) % 60 #calculate minutes
            hours = (i // 3600) %24 #calculate hours
            print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')
            time.sleep(1)
        print("Countdown finished!            ")
        winsound.Beep(1000, 1000)  # Beep sound for 1 second
        
        break

    except ValueError:
        print("Invalid input. Please enter an integer value.")
    
