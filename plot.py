# /usr/bin/python

import matplotlib.pyplot as plt
import csv
import numpy


x = []
y = []

with open('./test.csv','r') as csvfile:
	lines = csv.reader(csvfile,delimiter=',')
	for row in lines:
		x.append(float(row[0]))
		y.append(float(row[1]))
csvfile.close()

plt.plot(x,y,label='Cu foam')
plt.xlabel('x')
plt.ylabel('y')
plt.title('E vs. I')
plt.show()
plt.savefig('./test.pdf')



