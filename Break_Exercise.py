import time
import webbrowser

total_breaks = 3
break_counter = 0

print("The program started on "+time.ctime())
while(break_counter < total_breaks):
  #sleeps program for seconds
  time.sleep(2*60*60)
  webbrowser.open("http://www.youtube.com/watch?v=U1oFIsEu40w")
  break_counter = break_counter + 1
