# generate a alarm clock time string.
# using datetime module and python language features.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time =  datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{current_time}")
        if current_time == alarm_time:
            print("\nWake Up! Alarm Time Reached!")

            #Play alarm sound
            pygame.mixer.init()
            pygame.mixer.music.load("alarm.mp3")  # Ensure you have an alarm_sound.mp3 file
            pygame.mixer.music.play(-1)  # Play the sound in a loop

            input("Press Enter to stop the alarm...")  # Wait for user input
            pygame.mixer.music.stop()

            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    
    set_alarm(alarm_time)