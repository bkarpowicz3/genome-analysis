import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.cm as cm

def heatmap(file_string):
    data = np.genfromtxt(file_string, delimiter=',')     #automatically makes array from file

    logarray = np.log2(data+0.01)  #calculate the log of the data, eliminating zeros by adding 0.01 to all values

    #plot the heat map
    pyplot.figure()

    #scale the values by 0.6 to intensify differentiation of colors
    pyplot.imshow(logarray, vmin = 0,vmax =0.6*np.max(logarray), cmap='autumn', interpolation='none')
    pyplot.colorbar()

    pyplot.show()


