# /usr/bin/python

import matplotlib.pyplot as plt
import csv
import numpy


x = []
y = []

with open('./test.csv','r') as csvfile:
	lines = csv.reader(csvfile,delimiter=',')  
	for row in lines:
		x.append(float(row[0]))      ## here the data type should be float instead of int(integral), since it contains decimal potins.
		y.append(float(row[1]))
csvfile.close()     ### you need to close the file after you open it. 

#### PS, you need to make sure there's no empty lines at the end of your data file, other wise the code get confused when searching for the data. and might show error message like : " IndexError: list index out of range"

plt.plot(x,y,label='Cu foam')
plt.xlabel('x')      ## xlabel could be more elegant than this
plt.ylabel('y')
plt.title('E vs. I')        
plt.show()
plt.savefig('./test.pdf')  ## also you need to save your figure, not just show it. 



