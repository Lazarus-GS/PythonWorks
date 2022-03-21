count = 0
tot = 0.0
avg = 0.0
while True :
        
        nmber = input('Enter a Number : ')
        
        if nmber.casefold() == 'done' : #or 'Done' or 'DONE' :
                break
        try :
            fnmber = float(nmber)

        except :
            print('Invalid Input')
            continue

        tot = tot + fnmber
        count = count + 1
        avg = tot / count

#print('All Done!')
print(tot, count, avg)

 
   
    

