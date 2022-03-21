maxNmber = None
minNmber = None

while True :
    data = input('Enter a Number: ')

    if data.casefold() == 'done' :
        break
    
    try :
        fdata = int(data)

    except :
        print('Invalid Input')
        continue

#Finding the maxmimum number
    if maxNmber is None :
        maxNmber = fdata
    elif fdata > maxNmber :
        maxNmber = fdata

#Finding the minimum number 
    if minNmber is None :
        minNmber = fdata
    elif fdata < minNmber :
        minNmber = fdata

print('Maximum is ', maxNmber)
print('Minimum is ', minNmber)


