
#O objetivo é aprender a executar em Python as rotinas que aprendi no curso de R

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader.data as web
'''
def getpricehist(stock,start,end):
    yf.pdr_override()
    data = web.get_data_yahoo(stock, start = start, end = end)
    print(data.head())

    #plt.title(stock);plt.xlabel("Tempo (1d)"); plt.ylabel("Valor em R$")
    #plt.show(data['Close'].plot(figsize = (5,5)))


getpricehist('ITSA4.SA',"2018-01-02","2020-07-10")

'''
data = pd.read_csv("downloads/carteira.csv")
print(data.head())
