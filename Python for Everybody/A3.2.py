hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')

try :
    fhrs = float(hrs)
    frate = float(rate)
     
except :
    print('Error Please enter numeric input')
    quit()

if fhrs > 40 :
    OtRate = frate * 1.5
    OtHrs = fhrs - 40
    hrs = 40

pay = (fhrs * frate) + (OtHrs * OtRate)

print ('Pay: ', pay)