def bank(money,year):
    rate=1.1
    result= money

    for n in range(year):
        result=result*1.1 

    return round(result)

print(bank(1000,5))
   
