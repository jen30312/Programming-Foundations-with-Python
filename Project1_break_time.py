import time
import webbrowser

total_breaks =3
count = 0
print("The break timer started on " + time.ctime())
work_time = float(input("How many hours would you like to work before a 15-minute break?"))
while count <= total_breaks:
    time.sleep(work_time*60*60)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print("The 15-minute break starts now.")
    time.sleep(900)
    count += 1