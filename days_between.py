initial_value = 68450
rate = 0.019
initial_date = "December 28, 2019"
final_date = "January 2, 2021"
initial_date = initial_date.split()
initial_date[1] = int(initial_date[1][:-1])
initial_date[2] = int(initial_date[2])
final_date = final_date.split()
final_date[1] = int(final_date[1][:-1])
final_date[2] = int(final_date[2])
n_year = [0,31,28,31,30,31,30,31,31,30,31,30,31,0]
l_year = [0,31,29,31,30,31,30,31,31,30,31,30,31,0]
months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
total = 0
print(initial_date)
print(final_date)

initial_month = months.index(initial_date[0])+1
final_month = months.index(final_date[0])+1

for i in range(initial_date[2],final_date[2]+1):
    
    if i!=initial_date[2] and i != final_date[2]:
        if (initial_date-2000)%4 == 0:
            total += 366
        else:
            total += 365
    elif i==initial_date[2]: 
        total += sum(n_year[:initial_month])+initial_date[1]
    else:
        total += sum(n_year[final_month:])+initial_date[1]


    