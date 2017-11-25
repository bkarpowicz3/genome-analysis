import numpy as np
import matplotlib.pyplot as pyplot

def sampling(file_string):
    data = np.genfromtxt(file_string, delimiter=',')  # automatically makes array from file

    #create an array that contains only the upper triangle of the array of data
    #the function np.triu_indices(51) returns the indices of the upper triangle of a 51x51 matrix
    #use this function as an index to extract the upper triangular values
    upper_triangle = data[np.triu_indices(51)]
    print upper_triangle

    #make a frequency distribution of this data
    pyplot.figure()
    pyplot.hist(upper_triangle, bins=50, color='#9999FF')
    pyplot.xlabel('Ascl12Mbcortex Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Bin Interaction Frequency Distribution')
    pyplot.show()

    #extract 2 random samples of 100 values
    rand1 = np.random.choice(upper_triangle, 100)
    rand2 = np.random.choice(upper_triangle, 100)

    print rand1
    print rand2

    # make distributions of this data
    pyplot.figure()
    pyplot.hist(rand1, bins=50, color='#CCFF00')
    pyplot.xlabel('Random Sample 1 Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Bin Interaction Sampling Distribution')
    pyplot.show()

    pyplot.figure()
    pyplot.hist(rand2, bins=50, color='#CC0066')
    pyplot.xlabel('Random Sample 2 Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Bin Interaction Sampling Distribution')
    pyplot.show()