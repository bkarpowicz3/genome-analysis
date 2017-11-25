import numpy as np
import matplotlib.pyplot as pyplot

def histogram(file_string):
    data = np.genfromtxt(file_string, delimiter=',')     #automatically makes array from file

    #add all items in sublists to list
    intfreq = []
    for entry in data:
        for i in entry:
            intfreq.append(i)

    #plot the first histogram with 10 intervals
    pyplot.figure()     #initialize figure
    pyplot.hist(intfreq, bins = 10)     #plot histogram with data in list and 10 bins
    pyplot.xlabel('Number of Interactions')     #add x label
    pyplot.ylabel('Frequency')      #add y label
    pyplot.title('Interactions Between Bins of Ascl12Mbcortex')     #add title
    pyplot.xlim(0,300)      #set x-axis limit to 300, since none of the interactions exceed that value
    pyplot.show()       #display the plot

    #plot the second histogram with 50 intervals
    pyplot.figure()
    pyplot.hist(intfreq, bins=50, color = 'r')
    pyplot.xlabel('Number of Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Interactions Between Bins of Ascl12Mbcortex')
    pyplot.xlim(0, 300)
    pyplot.show()

    # plot the third histogram with 200 intervals
    pyplot.figure()
    pyplot.hist(intfreq, bins=200, color = 'g')
    pyplot.xlabel('Number of Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Interactions Between Bins of Ascl12Mbcortex')
    pyplot.xlim(0, 300)
    pyplot.show()