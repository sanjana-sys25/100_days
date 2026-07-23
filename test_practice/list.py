#This is a Temperature Analyzer
def count_hot_days(temp_list,thres):
    count=0
    for i in temp_list:
        if i>thres:
            count+=1
    return count
day_temp=[]
print("now enter the temperature in celcius for swvwn days")
for i in range(0, 7):
    temp = float(input(f'enter temp of day {i + 1}: '))
    day_temp.append(temp)
hot_days=print("total no. of hot days in the week is",count_hot_days(day_temp,32))