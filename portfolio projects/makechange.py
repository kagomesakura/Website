make_change = input("How many pennies do you have? ")
make_change = int(make_change)
#Then break that into quarters, dimes, nickles, and pennies.
# input divide by 100 for dollars - quarters divide by 25 - 10 for dimes - 5 for nickles

dollars = 100
dimes = 10
nickels = 5
pennies = 1

#if dollars >= 100:
#    dollars = make_change // dollars

quarters = make_change // 25
make_change = make_change % 25

dimes = make_change // 10
make_change = make_change % 10

nickels = make_change // 5
make_change = make_change % 5


pennies = make_change // 1
make_change = make_change % 1

print ('You have:', quarters, 'quarters,', dimes, 'dimes,', nickels, ' nickels and ,', pennies,'pennies.')
