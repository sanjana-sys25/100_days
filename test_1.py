#This is a test
def cal_fare(dist,rate,is_rush):
    if is_rush==True:
        FARE=dist*rate*1.5
    else:
        FARE=dist*rate
    return FARE
d=float(input("enter the distance to travel"))
rate=float(input("enter the base rate"))
rush_hour=input("is there is rush : Y/N")
if rush_hour=='Y':
    rush=True
elif rush_hour=='N':
    rush=False
else:
    print("invalid response")
total_fare=cal_fare(d,rate,rush)
print("total fare is",total_fare)