import numpy as np
import matplotlib.pyplot as pyplot

def distribution(file_string):
    data = []  # create empty list to append data to

    input = open(file_string, 'rU')  # open data

    for line in input:
        line = line.strip('\n').split(',')  # split data at commas
        data.append(line)  # append list with split data

    input.close()  # close file

    #make an array from this data
    arraydata = np.array(data)
    print arraydata

    #initialize two empty lists to store data to
    interact15 = []
    interact45 = []

    #add all items from column 15 to a list and all items from column 45 to another list
    for entry in data:
        interact15.append(float(entry[14]))
        interact45.append(float(entry[44]))

    print interact15
    print interact45

    #plot histogram (frequency distribution) of column 15
    pyplot.figure()
    pyplot.hist(interact15, bins = 50, color = 'm')
    pyplot.xlabel('Column 15 Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Column 15 Interaction Frequency Distribution')
    pyplot.show()

    #plot histogram (frequency distribution) of column 45
    pyplot.figure()
    pyplot.hist(interact45, bins = 50, color = 'c')
    pyplot.xlabel('Column 45 Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Column 45 Interaction Frequency Distribution')
    pyplot.show()

    #calculate means and medians for both sets of data and report
    mean15 = np.mean(interact15)
    mean45 = np.mean(interact45)
    med15 = np.median(interact15)
    med45 = np.median(interact45)
    print "The mean of the column 15 interaction data is: ", mean15
    print "The median of the column 15 interaction data is: ", med15
    print "The mean of the column 45 interaction data is: ", mean45
    print "The median of the column 45 interaction data is: ", med45