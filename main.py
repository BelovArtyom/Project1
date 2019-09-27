#Code below checks for float/integer/string of user input
def askfunc(questiontext):
    user_in = input(questiontext)
    try:
        #when a "." is detected, tries to turn it into a float
        if "." in user_in :
            return float(user_in)
        #else tries to turn the string input into an integer
        else:
            return int(user_in)
    #if input is not float or int compatible, ValueError will appear. Expection recurses the function in the event of an incorrect answer.
    except ValueError:
        print("ERROR: Input supposed to be a number, please try again.")
        #function recurses onto itself, reusing the input it was originally called with until a satisfactory answer is received.
        return askfunc(questiontext)

#values are given zeroes.
distance = 0
hrsperday = 0
speedoftravelkm = 0

#distance has to be a positive number greater than 0
while distance <= 0:
    distance = askfunc("Input the distance of your travel in kilometers.")
#hours per day have to be not only greater than 0, but also less or equal to 24 hours
while hrsperday <= 0:
    hrsperday = askfunc("Input amount of hours you will be travelling a day.")
    if hrsperday > 24:
        print("ERROR: A day is not more than 24 hours.")
        hrsperday = askfunc("Input amount of hours you will be travelling a day.")
#speedoftravel has to be a positive number greater than 0
while speedoftravelkm <= 0:
    speedoftravelkm = askfunc("Input the speed of your travel in kilometers per hour.")

print("You're trying to travel", distance, "kilometers spending", hrsperday, "hours per day with speed of", speedoftravelkm, "kilometers per hour or", speedoftravelkm*0.6213712, "miles per hour.")
print("This will take you", distance/speedoftravelkm, "hours, meaning no less than", distance/speedoftravelkm/hrsperday, "days of travel.")