def sort_bed(file_string):
    data = []   #create empty list to append data to

    input = open(file_string, 'rU')     #open data

    for line in input:
        line = line.strip('\n').split('\t')     #split data at tabs
        data.append(line)   #append list with split data

    input.close()   #close file

    print data

    Ascl12Mbcortex = [] #create empty list to append dictionaries to
    bin_info = {}   #create empty dictionary to be filled in

    #divide entries into dictionaries and append list with each dictionary
    for entry in data:
        bin_info.update({'chrom': entry[0],
                    'start': int(entry[1]),
                    'end': int(entry[2]),
                    'name': entry[3],
                    'bin_index': int(entry[3].split('_')[2]),
                    'bin_midpoint': (int(entry[2]) + int(entry[1])/2)})
        Ascl12Mbcortex.append(bin_info.copy())

    print Ascl12Mbcortex
    return Ascl12Mbcortex

