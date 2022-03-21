count = 0
tot = 0.0

while True :
        
        nmber = input('Enter a Number : ')
        
        if nmber == 'done' :
                break
        try :
            fnmber = float(nmber)

        except :
            print('Invalid Input')
            continue

        tot = tot + fnmber
        count = count + 1

print('All Done!')
print(tot, count, tot / count)


    
   
    

