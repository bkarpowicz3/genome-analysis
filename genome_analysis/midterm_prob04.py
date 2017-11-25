from midterm_prb01 import *
import numpy as np
import matplotlib.pyplot as pyplot

def scatter(file_string):

    #retrieve sorted bed file and assign resulting list to a variable
    Ascl12Mbcortex = sort_bed('Ascl12MbcortexMergedICED40kbbinsENM001.bed.txt')

    data = np.genfromtxt(file_string, delimiter=',')  # automatically makes array from file of bin interactions

    #retrieve the midpoint of bin 26 (the midpoint of the strand) from the list
    for dict in Ascl12Mbcortex:
        for key in dict:
            if dict['bin_index'] == 26:
                mdpt26 = dict['bin_midpoint']

    print mdpt26

    group1 = []

    #for the 0-199000 bp range, identify bins
    #add to corresponding lists as kbp values by dividing by 1000
    for dict in Ascl12Mbcortex:
        for key in dict:
            if abs(dict['bin_midpoint']-mdpt26) <= 199000:
                group1.append(dict['bin_index'])

    print group1

    group2 = []

    # for the 200000-399000 bp range, identify bins
    # add to corresponding lists as kbp values by dividing by 1000
    for dict in Ascl12Mbcortex:
        for key in dict:
            if abs(dict['bin_midpoint'] - mdpt26) <= 399000 and abs(dict['bin_midpoint'] - mdpt26) >=200000:
                group2.append(dict['bin_index'])

    print group2

    group3 = []

    # for the 600000-799000 bp range, identify bins
    # add to corresponding lists as kbp values by dividing by 1000
    for dict in Ascl12Mbcortex:
        for key in dict:
            if abs(dict['bin_midpoint'] - mdpt26) <= 799000 and abs(dict['bin_midpoint'] - mdpt26) >=600000:
                group3.append(dict['bin_index'])

    print group3

    #establish lists to append data
    interactions1_22 = []
    interactions2_22 = []
    interactions3_22 = []

    #append qualifying interactions values to above lists
    for i in range(0,51):
        for bin in group1:
            if i == bin:
                interactions1_22.append(data[i,22])
        for bin in group2:
            if i == bin:
                interactions2_22.append(data[i,22])
        for bin in group3:
            if i == bin:
                interactions3_22.append(data[i,22])

    # establish lists to append data
    interactions1_26 = []
    interactions2_26 = []
    interactions3_26 = []

    # append qualifying interactions values to above lists
    for i in range(0,51):
        for bin in group1:
            if i == bin:
                interactions1_26.append(data[i,26])
        for bin in group2:
            if i == bin:
                interactions2_26.append(data[i,26])
        for bin in group3:
            if i == bin:
                interactions3_26.append(data[i,26])

    #plot the group1 graph
    pyplot.figure()
    pyplot.scatter(interactions1_22, interactions1_26)
    pyplot.xlabel('Bin 22 Interaction Frequencies')
    pyplot.ylabel('Bin 26 Interaction Frequencies')
    pyplot.title('Interactions within 0-199000 bp')
    pyplot.show()

    # plot the group2 graph
    pyplot.figure()
    pyplot.scatter(interactions2_22, interactions2_26)
    pyplot.xlabel('Bin 22 Interaction Frequencies')
    pyplot.ylabel('Bin 26 Interaction Frequencies')
    pyplot.xlim(-1, 200)
    pyplot.title('Interactions within 200000-399000 bp')
    pyplot.show()

    # plot the group3 graph
    pyplot.figure()
    pyplot.scatter(interactions3_22, interactions3_26)
    pyplot.xlabel('Bin 22 Interaction Frequencies')
    pyplot.ylabel('Bin 26 Interaction Frequencies')
    pyplot.title('Interactions within 600000-799000 bp')
    pyplot.xlim(0, 16)
    pyplot.show()