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

N2=10**5
step=1/N2
alpha2=np.linspace(step, 1-step, N2-1)
VaR2=mLP+sLP*sp.norm.ppf(alpha2)
phi=1/0.05*(np.exp(-(1-alpha2)/0.05))/(1-np.exp(-1/0.05))
Mphi=VaR2*phi
Mphi=Mphi.mean()
print('The Spectral Measure Mphi N =', N2,', is', Mphi)

#Comparison Data (With Excel)
N3=100
step3=0.01
alpha3=np.linspace(step3, 1-step3, N3-1)
VaR3=mLP+sLP*sp.norm.ppf(alpha3)
phi=1/0.05*(np.exp(-(1-alpha3)/0.05))/(1-np.exp(-1/0.05))
Mphi2=VaR3*phi
Mphi2=Mphi2.mean()
print('The Spectral Measure Mphi N =', N3,', is', Mphi2)