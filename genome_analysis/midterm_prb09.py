import numpy as np
import matplotlib.pyplot as pyplot

def error(file_string):
    data = np.genfromtxt(file_string, delimiter = ',')  #create array from file

    data15 = []   #create empty list to store data from column 15

    #sort out the data in column 15 and add to the list
    for entry in data:
        data15.append(float(entry[14]))

    mean15 = np.mean(data15)    #calculate the mean
    stdev = np.std(data15)      #calculate the standard deviation
    sterr = stdev / np.sqrt(len(data15))    #calculate the standard error

    #initialize the x positions for the plot
    randomrange = np.random.uniform(0.65, 1.35, size = 51)  #create a range for the x values to be plotted over
    x_col15 = randomrange
    x_meanonese = [2]
    x_meantwose = [3]
    x_meanonesd = [4]

    #initialize the strip chart
    pyplot.figure()

    #plot the points
    pyplot.plot(x_col15, data15, marker = 'o', linestyle = 'None')
    pyplot.plot(x_meanonese, mean15, marker = 'o', linestyle = 'None')
    pyplot.plot(x_meantwose, mean15, marker = 'o', linestyle = 'None')
    pyplot.plot(x_meanonesd, mean15, marker = 'o', linestyle = 'None')

    #plot the error bars
    pyplot.errorbar(x_meanonese, mean15, yerr = sterr)
    pyplot.errorbar(x_meantwose, mean15, yerr = 2*sterr)
    pyplot.errorbar(x_meanonesd, mean15, yerr = stdev)

    #change the range axes
    pyplot.xticks(range(1,5,1), ['Column 15', 'Mean +- 1 SE', 'Mean +- 2 SE', 'Mean +- 1 SD'])
    pyplot.xlim(0,5)
    pyplot.ylim(-20, 60)  #remove one outlier

    #add labels
    pyplot.ylabel('Bin Interactions')
    pyplot.title('Error in Mean Column 15 Interactions')
    pyplot.show()