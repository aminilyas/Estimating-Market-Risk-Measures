# -*- coding: utf-8 -*-
"""
@author: Six
@edited by: Amin Ilyas

"""

import numpy as np
import scipy.stats as sp 
import pandas as pd 

data=pd.read_excel('SP500Data.xlsx',sheet_name='Sheet1') #read the data into a panda DataFrame
data['L&P']=-data['Prix'].diff(periods=1)
LP=data['L&P'].dropna() 
mLP=LP.mean()
sLP=LP.std()

N1=10**4 
step=(1-0.95)/N1
alpha=np.linspace(0.95+step, 1-step, N1-1) 
VaR=mLP+sLP*sp.norm.ppf(alpha) 
ES=VaR.mean()
print('The Expected Shortfall for a confidence level of 95% and for N =', N1,', is', ES)

#Comparsion Using Excel Steps
N2=10 
step2=0.005
alpha2=np.linspace(0.95+step2, 1-step, N2-1) 
VaR2=mLP+sLP*sp.norm.ppf(alpha) 
ES2=VaR2.mean()
print('The Expected Shortfall for a confidence level of 95% and for N =', N2,', is', ES2)


