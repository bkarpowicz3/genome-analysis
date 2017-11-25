import numpy as np

def probability(file_string):
    data = np.genfromtxt(file_string, delimiter = ',')  #create array from file
    upper_triangle = data[np.triu_indices(51)]  #isolate upper triangle of matrix

    #create two empty lists to sort data into
    btw200_275 = []
    btw0_25 = []

    #append lists with data falling into the two ranges
    for i in upper_triangle:
        if i >= 200 and i <= 275:
            btw200_275.append(i)
        elif i >= 0 and i <= 25:
            btw0_25.append(i)

    #calculate the probability as the number of entries in the range
    #divided by the total number of entries
    #must convert length to float to ensure probability is not returned as integer (0)
    prob200 = float(len(btw200_275))/len(upper_triangle)
    prob0 = float(len(btw0_25))/len(upper_triangle)

    #print the probabilities
    print "The probability that an interaction frequency is between 200 and 275 is", prob200
    print "The probability that an interaction frequency is between 0 and 25 is", prob0