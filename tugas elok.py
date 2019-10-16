hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
sisajam = (mins+dura)//60
sisamenit = (mins+dura)%60
jam = (hour+sisajam)%12
print(str(jam)+":"+str(sisamenit))
