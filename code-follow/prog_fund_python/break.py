import webbrowser
import time

curr_breaks = 0
total_breaks = 3

while (curr_breaks < total_breaks):
    time.sleep(7200)
    webbrowser.open("http://www.google.com")
    curr_breaks += 1

