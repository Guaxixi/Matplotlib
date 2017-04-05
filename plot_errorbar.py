#/usr/bin/python

import matplotlib.pyplot as plt
import csv
import numpy

#### Define x and y as array
x_1 = []
y_1 = []
xerror_1 = []
yerror_1 = []

x_2 = []
y_2 = []
xerror_2 = []
yerror_2 = []


#### Open csv file and import data into defined arrays
with open('./test_errorbar.csv','r') as csvfile:
	lines = csv.reader(csvfile,delimiter=',')  
	for row in lines:
		x_1.append(float(row[0]))      
		y_1.append(float(row[1]))
		yerror_1.append(float(row[2]))
		xerror_1.append(float(row[3]))
csvfile.close()    

#### You can define x_2, y_2, xerror_2, yerror_2 and so on in same manner as above, provided similar data layout.  
with open('./test_errorbar_2.csv','r') as csvfile:
	lines = csv.reader(csvfile,delimiter=',')  
	for row in lines:
		x_2.append(float(row[0]))      
		y_2.append(float(row[1]))
		yerror_2.append(float(row[2]))
		xerror_2.append(float(row[3]))
csvfile.close()    


#### Defile line style and 
ls = 'solid'  ## define line style, can be 'dashed', 'dashdot', 'dotted' etc. 

fig, ax = plt.subplots(figsize=(10,5))  

plt.ylim(0,100)

#### Start plotting! You can repeat this comman multiple times, feeding different x and y and errors 
ax.errorbar(x_1, y_1, xerr=xerror_1, yerr=yerror_1, linestyle=ls, color = 'orange', marker= 'o', label='Hydrogen')
		#For example:  ax.errorbar(x_2, y_2, xerr=xerror_2, yerr=yerror_2, linestyle=ls, color = 'orange', marker= 'o', label='Cu foam')
plt.legend() # define legend location

ax.errorbar(x_2, y_2, xerr=xerror_2, yerr=yerror_2, linestyle=ls, color = 'blue', marker= '^', label='Methane')
plt.legend()

#### Add axis name and title and save figure
plt.xlabel('Current efficiency (%)')      
plt.ylabel('Voltage (V)')
plt.title('Voltage vs. Current effiency')  

plt.tight_layout()
plt.savefig('./test_errorbar.png', format = 'png', dpi=300)  # change format into your preferred one, dpi is preferrably at least 300 for journals. 
plt.show()