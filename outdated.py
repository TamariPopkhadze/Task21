month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
day = ["01","02","03","04","05","06","07","08","09","10",
      "11","12","13","14","15","16","17","18","19","20",
       "21","22","23","24","25","26","27","28","29","30","31"]

monthInNumeric = ["01", "02", "03", "04",
                  "05", "06", "07", "08", 
                  "09", "10", "11", "12"]
date = input()
if date.find("/") != -1:
    date = date.split("/") 
    try:
        finaldate = date[2] + "-" + monthInNumeric[int(date[0])-1] + "-" + day[int(date[1])-1]
        print(finaldate)
    except(NameError,ValueError,IndexError):
        print("something error")
else:
    date = date.replace("," , "")
    date = date.split(" ")
    try:
        finaldate = date[2] + "-" + monthInNumeric[month.index(date[0])]+ "-" + day[int(date[1])-1]
        print(finaldate)

    except (NameError, ValueError, IndexError):
        print("something error")
     
