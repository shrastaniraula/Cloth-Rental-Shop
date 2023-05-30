import datetime

def getDateTime():
    datime = datetime.datetime.now()
    years = str(datime.year)
    months = str(datime.month)
    days = str(datime.day)
    hours = str(datime.hour)
    minutes = str(datime.minute)
    seconds = str(datime.second)
    datee = years + "-" + months + "-" + days + "-" + hours + "-" + minutes + "-" + seconds
    return datee