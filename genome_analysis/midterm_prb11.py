import numpy as np
import matplotlib.pyplot as pyplot

def hyptest(file_string):
    data = np.genfromtxt(file_string, delimiter=',')

    #establish the test statistic
    print "The strength of communication between bins 26 & 21 is", data[26,21]

    #create an array that contains only the upper triangle of the array of data
    upper_triangle = data[np.triu_indices(51)]

    #plot the distribution of interactions for all pairs of bins
    pyplot.figure()
    pyplot.hist(upper_triangle, bins = 50, color = '#FF9900')
    pyplot.xlabel('Number of Bin Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Bin Interaction Frequency for Ascl12Mbcortex')
    pyplot.show()

    pvaluelist = []

    #estimate the p value for obtaining a value greater than 15.8482
    for entry in upper_triangle:
        if entry >= 15.8482:
            pvaluelist.append(entry)

    pvalue = float(len(pvaluelist))/float(len(upper_triangle))
    print "The pvalue is", pvalue
    print "Since P > a, do not reject the null hypothesis."

    #plot the distribution of interactions with a red line at the test stat
    pyplot.figure()
    pyplot.hist(upper_triangle, bins = 50, color = 'b')
    pyplot.axvline(x = 15.8482, color = 'r')
    pyplot.xlabel('Number of Bin Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Bin Interaction Frequency for Ascl12Mbcortex')
    pyplot.show()