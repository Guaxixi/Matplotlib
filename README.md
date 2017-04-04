# Matplotlib tips

First, you need to install python on your computer. And you might find useful tutorials on Matplotlib website: 

http://matplotlib.org/index.html

Where you can find examples/galleries to look at figures of your interests. 

For example, in http://matplotlib.org/examples/statistics/errorbar_limits.html, you can take a look at how it is coded to make this plot with error bar. 
You need two modules called `numpy` and `matplolib.pyplot` to complete your tasks, the former handles the data, and the latter does the actual plot. 
The code usually consists of a few sections:
* define your data, either by feeding external file or putting in numbers directly 
* set upper and lower plotting limits
* do the plotting with specific requirements: axis, font, marker, color etc.. 

You might not need all the command. Here is a super simplified version:
http://matplotlib.org/examples/statistics/errorbar_demo.html

To import external data file to plot in your script, you need to prepare your data file in required formality, and specify in your code where to look for it. Sometimes extra care might be needed to treat the comma or space that is used to separate the numbers. 

Usually I export my excel sheet into comma separated file 'csv', and then import it with the python module called `csv`. In this case you need to import the module `csv` in your code to deal with such form of data. Here is an example:
https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/

Further genral imformation: 
https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python#gs.35NGb=8 
Datacamp is very neat! 

That is a simple introduction, but enough for you to start playing with it. Hope you find it useful! 
