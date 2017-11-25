import numpy as np

def interactions_array(file_string):
    data = []   #create empty list to append data to

    input = open(file_string, 'rU')     #open data

    for line in input:
        line = line.strip('\n').split('\t')     #split data at tabs
        data.append(line)   #append list with split data

    input.close()   #close file
    print data

    interactions = [[0 for i in range(51)] for j in range(51)]   #create empty 51x51 array to append values to

    # associate each ordered pair of interactions with its frequency in an array
    for entry in data:
        bin_1 = int(entry[0].split('_')[2])     #define first bin coordinate as number associated with column 1 data
        bin_2 = int(entry[1].split('_')[2])     #define second bin coordinate as number associated with column 2 data
        num_int = float(entry[2])               #define number of interactions as float value in column 3
        interactions[bin_1][bin_2]=num_int      #assign coordinates of array to each value
        interactions[bin_2][bin_1]=num_int      #assign reverse coordinates of array to same values (symmetric matrix)

    array = np.array(interactions)      #turn array into numpy array

    inter_dict = {'Ascl12Mbcortex': np.array(interactions)}      #define array as dictionary

    print interactions
    print inter_dict

    np.savetxt('bin_interactions.csv',array, delimiter = ',')       #save array as csv with commas between values





