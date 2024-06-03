import winsound 
import time 
 
def play_buzzer_sound(frequency, duration): 
    winsound.Beep(frequency, duration) 
 
# Example usage: 
frequency = 1000  # Frequency of the buzzer sound in Hz 
duration = 1000  # Duration of the sound in milliseconds 
 
play_buzzer_sound(frequency, duration) 
time.sleep(2)  # Add a delay of 2 seconds before ending the program