import h5py
import numpy
import matplotlib.pyplot as plt

numpy.set_printoptions(precision=3, threshold=numpy.nan)

# for inOut: 0 is inflow, 1 is outflow
def heatmap(dataArray, inOut, title):
    # sum for each area
    regionSum = numpy.sum(dataArray, axis=0)

    # find total inflow and outflow
    partialSum = numpy.sum(regionSum, axis=2)
    totalSum = numpy.sum(partialSum, axis=1)
    percentInflow = numpy.true_divide(regionSum[inOut], totalSum[inOut])
    plt.imshow(percentInflow, cmap='hot', interpolation='nearest')
    plt.title(title)
    plt.colorbar()
    plt.show()
    plt.savefig(title)


# BJ16 data
f16 = h5py.File('BJ16_M32x32_T30_InOut.h5', 'r')
dset = f16['data']
heatmap(dset, 0, "BJ16_Inflow")
heatmap(dset, 1, "BJ16_Outflow")

# BJ15 data
f15 = h5py.File('BJ15_M32x32_T30_InOut.h5', 'r')
dset15 = f15['data']
heatmap(dset15, 0, "BJ15_Inflow")
heatmap(dset15, 1, "BJ15_Outflow")

# BJ14 data
f14 = h5py.File('BJ14_M32x32_T30_InOut.h5', 'r')
dset14 = f14['data']
heatmap(dset14, 0, "BJ14_Inflow")
heatmap(dset14, 1, "BJ14_Outflow")

# BJ13 data
f13 = h5py.File('BJ13_M32x32_T30_InOut.h5', 'r')
dset13 = f13['data']
heatmap(dset13, 0, "BJ13_Inflow")
heatmap(dset13, 1, "BJ13_Outflow")