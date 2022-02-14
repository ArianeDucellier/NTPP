"""
File to encode the event sequences and
transform them into a suitable time series
"""
import math
import numpy as np

def temporal_encoding(times, M=512):
    """
    Equation 2 from Zuo et al. (2017)
    """
    L = len(times)
    Z = np.zeros((M, L))
    trig = np.array([math.pow(10000.0, 2.0 * (i // 2) / M) for i in range(M)])
    times = np.reshape(times, (-1, 1))
    expd = np.expand_dims(times ,2)
    tiled = np.tile(expd, trig.shape[0])
    trans = np.transpose(trig)
    ratio = np.transpose(tiled / trans)
    Z[1::2, :] = np.cos(ratio[1::2, 0, :])
    Z[0::2, :] = np.sin(ratio[0::2, 0, :])
    return Z
    