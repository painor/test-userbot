def add_mins(Time, Minutes):
    hour, minute = Time.split(":")
    hour = int(hour)
    minute = int(minute)
    m = minute + int(Minutes)
    if m >= 60:
        add_to_hours = m / 60
        last_minute = m % 60
        hour = hour + add_to_hours
        hour = int(hour)
    if len(str(last_minute)) == 1:
        last_minute = f"0{last_minute}"
    if len(str(hour)) == 1:
        hour = f"0{str(hour)}"
    
    return f"{str(hour)}:{str(last_minute)}"



def Bytes(kilobytes) :  
    Bytes = kilobytes / 1024
    return Bytes