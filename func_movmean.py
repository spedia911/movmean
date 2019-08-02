# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:10:23 2019

@author: nklee
"""

def movmean  (values, window):
    weights = np.ones(window)
    sma = np.convolve(values, weights, 'valid')/window
    left = np.floor(window/2).astype(int)    
    sma_left = []
    for i in range(left):
        sma_left = np.append(sma_left, np.mean(values[0:window-left+i]))
    sma = np.append(sma_left, sma)
    right = np.floor((window-1)/2).astype(int)    
    for i in range(right):
        sma = np.append(sma, np.mean(values[-window+i+1:]))
    return sma

def movmean2d(values, window):
#    weights = np.ones((np.shape(xTest)[0], window))
    nFeat = np.shape(values)[1]
    weights = np.ones((window,1))
    sma = convolve2d(values, weights, mode='valid')/window
    left = np.floor(window/2).astype(int)    
    sma_left = np.empty((0,nFeat))
    for i in range(left):
        temp = np.mean(values[0:window-left+i,:], axis=0)
        sma_left = np.append(sma_left, np.reshape(temp,(1,-1)), axis=0)
    sma = np.append(sma_left, sma, axis=0)
    right = np.floor((window-1)/2).astype(int)    
    for i in range(right):
        temp = np.mean(values[-window+i+1:,:], axis=0)
        sma = np.append(sma, np.reshape(temp,(1,-1)), axis=0)
    return sma