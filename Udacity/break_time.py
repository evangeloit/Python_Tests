import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on" + time.ctime())

while (break_count < total_breaks):
    print(break_count)
    time.sleep()
    webbrowser.open('https://www.youtube.com/watch?v=1MGVSupOBVg')
    break_count= break_count + 1


