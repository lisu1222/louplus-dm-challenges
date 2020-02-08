import pandas as pd
import numpy as np

def caculate_w():
    df = pd.read_csv('nyc-east-river-bicycle-counts.csv')
    
    bb = df['Brooklyn Bridge'].values
    mb = df['Manhattan Bridge'].values
    
    x = [[1, i] for i in bb]
    x = np.matrix(x)
    y = np.matrix(mb.reshape(len(mb), 1))
    
    W = (x.T * x).I * x.T * y
    w = round(float(W[0]),2)
    b = round(float(W[1]),2)
    
    return w, b