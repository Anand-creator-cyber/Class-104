

import csv
with open(r'C:\Users\91814\OneDrive\Desktop\Whitehat\Class 104\SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(float(n_num))



n = len(new_data)
total =0
for x in new_data:
    total += x

median = n // 2
#
print("Median is: " + str(median))

mean = n/2 
print("Mean is: " + str(mean)        

mode = 2*mean - 3*median
print(mode)