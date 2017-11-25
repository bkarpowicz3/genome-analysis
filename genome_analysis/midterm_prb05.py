import numpy as np
import matplotlib.pyplot as pyplot

def boxplot(file_string):
    data = np.genfromtxt(file_string, delimiter=',')   #automatically makes array from file
    print data

    # took an average of each row of interaction frequencies for each bin and appended to list
    means = []
    for entry in data:
        means.append(np.mean(entry))

    # sort the means from low to high and return their indices (in this case, also their bin numbers)
    print np.argsort(means)

    #the results show that bins 25 & 26 have the highest averages, and bins 2 & 38 have the lowest averages

    # extract the information for bin 25 and assign to list
    data25 = [row[25] for row in data]
    print data25

    # extract the information for bin 26 and assign to list
    data26 = [row[26] for row in data]
    print data26

    # extract the information for bin 2 and assign to list
    data2 = [row[2] for row in data]
    print data2

    # extract the information for bin 38 and assign to list
    data38 = [row[38] for row in data]
    print data38

    #add all data to one list to be plotted
    alldata = [data25, data26, data2, data38]

    #make a boxplot
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.boxplot(alldata)
    pyplot.ylim(-1, 55) #allow values on zero to be seen by extending y axis slightly
    ax.set_xticklabels(['Bin 25','Bin 26','Bin 3','Bin 38'])
    pyplot.title('Interaction Frequencies of Bins')
    pyplot.show()