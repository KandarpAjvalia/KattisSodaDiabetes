start = int(input("# of empty bottles at the start of the day: "))
found = int(input("# of bottles found during the day: "))
emptyRequired = int(input("# of empty bottles required: "))
start += found
full = 0
drank = 0
trade = 0
while(start>=emptyRequired):
    full = start//emptyRequired
    trade = start%emptyRequired
    drank += full
    start = full + trade
    
print(drank)
