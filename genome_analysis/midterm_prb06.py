import numpy as np
import matplotlib.pyplot as pyplot

def meanvar(file_string):
    data = np.genfromtxt(file_string, delimiter=',')  # automatically makes array from file

    # take an average of each row (equivalent to column since symmetric matrix) of interaction frequencies and append to list
    means = []
    for entry in data:
        means.append(np.mean(entry))

    #plot histogram of means
    pyplot.figure()
    pyplot.hist(means, bins = 10, color = 'r')
    pyplot.ylim(0,12)
    pyplot.xlim(0,25)
    pyplot.xlabel('Mean Bin Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Histogram of the Means')
    pyplot.show()

    # compute variance of each row of interaction frequencies and append to list
    variances = []
    for entry in data:
        variances.append(np.var(entry))

    #plot histogram of variances
    #needs to have more bins because the values span a much larger scale
    pyplot.figure()
    pyplot.hist(variances, bins = 20, color = 'c')
    pyplot.ylim(0,16)
    pyplot.xlim(0,2000)
    pyplot.xlabel('Variance in Bin Interactions')
    pyplot.ylabel('Frequency')
    pyplot.title('Histogram of the Variances')
    pyplot.show()

    # compute coefficients of variations for each row and append to list
    # coefficient of variation is equal to standard deviation/mean
    coefficients = []
    for entry in data:
        coefficients.append((np.std(entry)/np.mean(entry)*100))

    # plot histogram of coefficients of variations
    pyplot.figure()
    pyplot.hist(coefficients, bins=10, color='#cd33ff')
    pyplot.ylim(0, 17)
    pyplot.xlabel('Coefficients of Variation of Bin Interactions (% of the mean)')
    pyplot.ylabel('Frequency')
    pyplot.title('Histogram of the Coefficients of Variation')
    pyplot.show()