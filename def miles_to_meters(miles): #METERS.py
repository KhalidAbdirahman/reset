def miles_to_meters(miles):         #METERS
    return miles * 1609.34

def minutes_to_seconds(minute):       #SECONDS
    return minute * 60

dist = float(input("Enter the distance traveled in miles"))    # DISTANCE IN MILES
time = float(input("Enter the time elapsed in minutes"))      # TIME IN MINUTES
speed_mps = (miles_to_meters(dist) / minutes_to_seconds(time))
print("The speed in meters per second is", speed_mps)