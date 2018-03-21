import h5py
import numpy
import matplotlib.pyplot as plt
numpy.set_printoptions(precision=3, threshold=numpy.nan)

f = h5py.File('BJ15_M32x32_T30_InOut.h5', 'r')
dset = f['data']

def weeklyTotal(list, numVal, numpyArr):
    arr = []
    for i in range (0, numVal, 2):
        arr.append(numpy.sum(numpyArr[list[i]:list[i+1]], axis=0)[0])
    return arr;

def graph(numVal, data, title, xlabel):
    ind = numpy.arange(numVal)
    plt.bar(ind, data)
    #plt.xaxis.set_major_locator(md.MinuteLocator(byminute=[0,30], interval = 1))

    #plt.xticks(ind, xticks)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.show()
    plt.savefig(title)

def dailyGraph(index1, index2, title):
    days = byDate[index1:index2:]
    result = days[:,0]
    graph(48, result, title, '30 Minute Intervals')

regionSum = numpy.sum(dset, axis=3)
byDate = numpy.sum(regionSum, axis=2)

# Mondays of March
mondayIndex = [48, 95, 384, 431, 720, 767, 1032, 1079]
mondayInflow = weeklyTotal(mondayIndex, 7, byDate)
graph(4, mondayInflow, 'Mondays - March 2015', 'March, 2015') #('2nd', '9th', '16th', '23rd')

# Sundays of March
sundayIndex = [0, 47, 336, 383, 672, 719, 984, 1031, 1320, 1367]
sundayFlow = weeklyTotal(sundayIndex, 9, byDate)
graph(5, sundayFlow, 'Sundays - March 2015', 'March, 2015') #('1st', '8th', '15th', '22nd', '29th')

# Graphs of throughout the Day
dailyGraph(48, 96, 'Monday, March 2nd 2015') # Monday Mar 2nd
dailyGraph(384, 432, 'Monday, March 9th 2015') # Monday Mar 9th
dailyGraph(0, 48, 'Monday, March 1st 2015') # Sunday Mar 1
dailyGraph(336, 384, 'Monday, March 8th 2015') # Sunday Mar 8