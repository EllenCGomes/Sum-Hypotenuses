def sum_hypotenuses(x):
    opposite = 1 
    adjacent = opposite 
    sum = 0
    while opposite <= x:
        while adjacent <= x:
            n = ((opposite**2) + (adjacent**2))**(1/2) #calculate hypotenuse 
            if n-int(n) == 0 and n <= x: #check if the number is integer and less than x
                sum = sum + n
            adjacent = adjacent + 1
        opposite = opposite + 1
        adjacent = opposite #avoid duplicate (ex: op = 2; ad = 1 e op = 1; ad = 2)
    return (sum)    

        
                    
        
      
        
          

            
