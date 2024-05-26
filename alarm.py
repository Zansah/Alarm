import datetime
from playsound import playsound
import time

def set_alarm(alarm_time, sound_file):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up")
            while True:
                playsound(sound_file)
                time.sleep(2)  
                stop = input("To stop the alarm, type 'True': ")
                if stop.lower() == "true":
                    print("Alarm stopped.")
                    return

        time.sleep(1)

alarm_time = input("Please set the alarm time in 24 hour format (e.g., 09:00:00): ")
sound_file = "Coming soon"
set_alarm(alarm_time, sound_file)
