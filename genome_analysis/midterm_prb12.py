import numpy as np
import matplotlib.pyplot as pyplot
from midterm_prb01 import *

def distdensity(file_string):

    data = np.genfromtxt(file_string, delimiter=',') #make data into array

    #retrieve sorted bed file and assign resulting list to a variable
    coordinates = sort_bed('Ascl12MbcortexMergedICED40kbbinsENM001.bed.txt')

    #extract midpoints
    midpoints = []
    for entry in coordinates:
            midpoints.append(entry['bin_midpoint'])

    #initialize empty lists to append bins that fall within ranges to
    kb80 = []
    kb160 = []
    kb240 = []
    kb320 = []

    #sort bins by the calculating the distances away from each other (based on midpoints)
    #append the ordered pair of the bins that fall within each range of distances apart to the corresponding list
    for i in range(0, len(midpoints)):
        for j in range(0, len(midpoints)):
            if midpoints[i]-midpoints[j] >= 0 and midpoints[i]-midpoints[j] <= 80000:
                kb80.append([i,j])
            elif midpoints[i]-midpoints[j] >= 81000 and midpoints[i]-midpoints[j] <= 160000:
                kb160.append([i,j])
            elif midpoints[i]-midpoints[j] >= 161000 and midpoints[i]-midpoints[j] <= 240000:
                kb240.append([i,j])
            elif midpoints[i]-midpoints[j] >= 241000 and midpoints[i]-midpoints[j] <= 320000:
                kb320.append([i,j])

    #initialize empty lists to append bin interactions to
    binint80 = []
    binint160 = []
    binint240 = []
    binint320 = []

    #append the above lists with the interaction frequency values from the .csv file at the coordinates of each of the ordered pairs found above
    for [i,j] in kb80:
        binint80.append(data[i,j])

    for [i,j] in kb160:
        binint160.append(data[i,j])

    for [i, j] in kb240:
        binint240.append(data[i, j])

    for [i, j] in kb320:
        binint320.append(data[i, j])

    #plot the histogram for interactions 0-80000 bp apart
    pyplot.figure()
    pyplot.hist(binint80, bins = 30, color = 'g')
    pyplot.xlabel('Interactions Between 0-80 kb')
    pyplot.ylabel('Frequency')
    pyplot.title('Density of Bin Interactions 0-80 kb Apart')
    pyplot.show()

    #plot the histogram for interactions 81000-160000 bp apart
    pyplot.figure()
    pyplot.hist(binint160, bins=30, color='r')
    pyplot.xlabel('Interactions Between 81-160 kb')
    pyplot.ylabel('Frequency')
    pyplot.title('Density of Bin Interactions 81-160 kb Apart')
    pyplot.show()

    #plot the histogram for interactions 161000-240000 bp apart
    pyplot.figure()
    pyplot.hist(binint240, bins=30, color='y')
    pyplot.xlabel('Interactions Between 161-240 kb')
    pyplot.ylabel('Frequency')
    pyplot.title('Density of Bin Interactions 161-240 kb Apart')
    pyplot.show()

    #plot the histogram for interactions 241000-320000 bp apart
    pyplot.figure()
    pyplot.hist(binint320, bins=30, color='m')
    pyplot.xlabel('Interactions Between 241-320 kb')
    pyplot.ylabel('Frequency')
    pyplot.title('Density of Bin Interactions 241-320 kb Apart')
    pyplot.show()

    #calculate the means of each of the lists of interactions
    mean80 = np.mean(binint80)
    mean160 = np.mean(binint160)
    mean240 = np.mean(binint240)
    mean320 = np.mean(binint320)
    print mean80, mean160, mean240, mean320

    #the test statistic is still 15.8482
    #determined in last question
    print "Test statistic:", data[26,21]

    #by looking at the lists, we know this value falls in the 241-320 kb range
    #compute the pvalue by determining which values in the list are above the test statistic
    pvaluelist = []
    for entry in binint320:
        if entry >= 15.8482:
            pvaluelist.append(entry)

    #calculate the pvalue by finding the probability that a value will be greater than or equal to the test statistic
    pvalue = float(len(pvaluelist))/float(len(binint320))
    print "The pvalue is", pvalue
    print "Since P > a, accept the null hypothesis."

    #plot the histogram of 241000-320000 bp with a red line at the test statistic
    pyplot.figure()
    pyplot.hist(binint320, bins=30, color='m')
    pyplot.axvline(x = 15.8482, color = 'r')
    pyplot.xlabel('Interactions Between 241-320 kb')
    pyplot.ylabel('Frequency')
    pyplot.title('Density of Bin Interactions 241-320 kb Apart')
    pyplot.show()