hrs = float(input('Enter Hours: '))
rate = float(input('Enter the Hourly Rate: '))

def computepay():
    
    if hrs > 40 :
        OtRate = rate * 1.5
        OtHrs = hrs - 40
        hrs = 40
        

    pay = (hrs * rate) + (OtHrs * OtRate)
    return pay

x = computepay()
print ('Pay: ', x)