#!/usr/bin/python

#Here are 3 ways to use "for loops" in python to do something to each element
#in an array.

#First, import relevant modules: numpy for arrays and matplotlib for plotting
import numpy as np
import matplotlib.pyplot as plt

########################     For Loop 1.     ################################

#I'm going to make two lists that are 50 elements long
#Then, I will populate these lists with some simple trig

points = 50 #length of lists

sinwave = np.empty(points) #np.empty creates empty arrays
coswave = np.empty(points) #the only argument I am using is the array length
x = np.empty(points)       #x will be the x-value, cos and sin will by y's

#range(points) will return the list: (0,1,2,3,4...47,48,49). It's 50 #'s long

for i in range(points):     #"For each element, i, in range(points)..."
	percent = float(i)/points #find the fraction of points we've gone through
	#since i changes every time through the loop, each value in these arrays
	#    will be used. x[i] represents the current x value.
	x[i] = 2.0*np.pi*percent  #x is scaled: it will be a uniform list from 0-2pi
	sinwave[i] = np.sin(x[i]) #the sine value of the current x is stored in the
	coswave[i] = np.cos(x[i]) #   current sinwave. same with cos and coswave.

#Lets plot what we got!
plt.plot(x, sinwave, label="sine(x)")   #x-values = x, y-values = sinwave. by
plt.plot(x, coswave, label="cosine(x)") #adding labels, we can have a legend.
plt.legend() #this line adds a standard legend.
plt.show()   #this line displays the two plots above.

########################     For Loop 2.     ################################
#In For Loop 1, we had to follow three arrays syncronously, so we had to
#iterate through the variable "i". Now we'll iterate through just one array,
#which is simpler in python.
#
#Let's say I only wanted the caps of the sine wave, and I didn't care about
#the x values.

#This time, I'll make an empty array, because I don't know its ultimate length
sinwaveCaps = [] 

for value in sinwave:  #"For each element, value, in the array sinwave..."
	if abs(value)>=0.5:  #if the sinwave value's amplitude is larger than 0.5...
		sinwaveCaps.append(value) #apend the value to the sinwaveCaps array.

#Let's plot just the caps!
plt.plot(sinwaveCaps) #If I only use one argument here, the x-value will be
                      #The index of the argument. (It'll be a line chart)
plt.show()

#Notice that the X-values are NOT preserved, so the caps don't have blank
#space between them! This is useful for some problems but not others.


########################     For Loop 3.     ################################
#90% of Geoscience is doing math on a grid (like a map). Thankfully, if we
#nest For Loops, we can iterate through x and y values (or P and T values, e.g.)

#I want to calculate the sum of my sine and cosine waves and store those values
sumSC = []

for s in sinwave:     #For each element, s, in sinwave..."
	for c in coswave:   #For each element, c, in coswave..."
		sumSC.append(s+c) #Append the elements together.

#WARNING! The order that the above for loop adds the elements together might
#         be non-intuitive for beginner programmers. Go through the for-loop
#         a few times in your head to conceptualize it. Here's the order the
#         computer uses:
#  1. s=1       <-------outside for-loop
#  | 1. c=1     <-------inside  for-loop
#  | | 1. s+c=2 <-------operation done inside both loops
#  | 2. c=2
#  | | 1. s+c=3
#  2. s=2
#  | 1. c=1
#  | | 1. s+c=3
#  | 2. c=2
#  | | 1. s+c=4

#Because of this loop, the values (in the example: 2,3,3,4) correspond to the
#coordinates (1,1),(1,2),(2,1),(2,2). So if we want to plot them on a map,
#the order of the values is (2,3,3,4), the x-coordinates (1,1,2,2), and the
#y-coordinates (1,2,1,2). If the x and y values are (1,2), we have to TILE
#or REPEAT these arrays. Numpy has the solution:
xsin = np.repeat(sinwave,len(coswave)) #(1,2) -> (1,1,2,2)
ycos = np.tile(coswave,len(sinwave))   #(1,2) -> (1,2,1,2)
#note I repeated the sinwave array by the length of the coswave 
#    (50 of the first value, 50 of the second, ... 50 of the last value)
#Since both arrays are the same length I could have just used 50. But I'm
#playing it safe here, assuming all I know is that sumSC was calculated
#len(sinwave)xlen(coswave) times.

#Let's plot this!!
#I'm using a scatter plot since the data aren't in a perfect grid.
#x = the repeated "xsin" array
#y = the tiled "ycos" array
#color value = sumSC values
#color map = matplotlib's blue-to-white-to-red
plt.scatter(xsin,ycos,c=sumSC,cmap=plt.cm.get_cmap('bwr'))
plt.colorbar() #this line adds a color bar using the color map and c values
plt.show()     #this line shows us our last figure.

#Created by Jacob


