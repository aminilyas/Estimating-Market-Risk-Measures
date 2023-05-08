# -*- coding: utf-8 -*-
"""
@author: Six/
@edited by: Krati Sharma

"""

#Retrieve the L/P data of the gold portfolio of section 1.2 
#Python

#P1) Compute m_L/P  and s_L/P;
#P2) Compute z_α for α = 95%, 99% and 90% using the inverse of the standard cumulative normal distribution;
#P3) deduce from questions 1 and 2 the values of 95%VaR, 99%VaR and 90%VaR;

#importing libraries 
import pandas as pd 
import scipy.stats as sp 
data=pd.read_excel('SP500Data.xlsx',sheet_name= 'Sheet1')
data['L&P']=-data['Prix'].diff(periods=1)
LP= data['L&P'].dropna()
print(LP)

mLP=LP.mean()
sLP=LP.std()
print(mLP)
print(sLP)
#Compute the values of zalpha
z90=sp.norm.ppf(0.90)
z95=sp.norm.ppf(0.95)
z99=sp.norm.ppf(0.99)

#Compute the parametric VaR
parametric_var95 = mLP+sLP*z95
print('The parametric VaR of the S&P portfolio at 95% is:', parametric_var95)
parametric_var99 = mLP+sLP*z99
print('The parametric VaR of the S&P portfolio at 99% is:', parametric_var99)
parametric_var90 = mLP+sLP*z90
print('The parametric VaR of the S&P portfolio at 90% is:', parametric_var90)


#%%
#P4) Compute the arithmetic returns
#P5) Deduce m_r and s_r
#P6) Deduce m_L/P and s_L/P - use the mean of the price as Pt-1
#P7) Compute the VaR for the three usual levels of confidence

#import file
data=pd.read_excel('SP500Data.xlsx',sheet_name='Sheet1') #read the data into a panda DataFrame

#Compute the arithmetic returns
nM=len(data)
dataVec1=data.iloc[1:nM,1]
dataVec1= dataVec1.reset_index(drop=True)
dataVec2=data.iloc[0:nM-1,1]
dataVec2= dataVec2.reset_index(drop=True)
arithm=dataVec1/dataVec2-1

#Compute the holding value
Pt_1=data['Prix'].mean()

#Compute the empirical moments for arithm
mr=arithm.mean()
sr=arithm.std()
mla=-mr
sla=sr
mLPar=mla*Pt_1
sLPar=sla*Pt_1
# print(mLPar)
# print(sLPar)

#Compute the values of zalpha
z90=sp.norm.ppf(0.90)
z95=sp.norm.ppf(0.95)
z99=sp.norm.ppf(0.99)
#Compute the parametric VaR from arithmetic returns
parametricAr_var95 = mLPar+sLPar*z95
print('The parametric VaR of the s&p portfolio at 95% (relative arithmetic Loss normal) is:', parametricAr_var95)
parametricAr_var99 = mLPar+sLPar*z99
print('The parametric VaR of the s&p portfolio at 99% (relative arithmetic Loss normal) is:', parametricAr_var99)
parametricAr_var90 = mLPar+sLPar*z90
print('The parametric VaR of the s&p portfolio at 90% (relative arithmetic Loss normal) is:', parametricAr_var90)


#%% 3.c
#importing libraries 
import pandas as pd 
import scipy.stats as sp 
import numpy as np


#importe file
data=pd.read_excel('SP500Data.xlsx',sheet_name='Sheet1') #read the data into a panda DataFrame


#Compute the arithmetic returns
nM=len(data)
dataVec1=data.iloc[1:nM,1]
dataVec1= dataVec1.reset_index(drop=True)
dataVec2=data.iloc[0:nM-1,1]
dataVec2= dataVec2.reset_index(drop=True)
geom=np.log(dataVec1/dataVec2)

#Compute the values of zalpha
z90=sp.norm.ppf(0.90)
z95=sp.norm.ppf(0.95)
z99=sp.norm.ppf(0.99) 


#Compute the empirical moments for geom
mR=geom.mean()
sR=geom.std()
mlg=-mR
slg=sR
# print(mR)
# print(sR)
#Compute the holding value
Pt_1=data['Prix'].mean()

#Compute the parametric VaR from arithmetic returns
parametricGo_var95 = Pt_1*(1-np.exp(-mlg-slg*z95))
print('The parametric VaR of the S&P portfolio at 95% (relative geometric Loss normal) is:', parametricGo_var95)
parametricGo_var99 = Pt_1*(1-np.exp(-mlg-slg*z99))
print('The parametric VaR of the S&P portfolio at (relative geometric Loss normal) 99% is:', parametricGo_var99)
parametricGo_var90 = Pt_1*(1-np.exp(-mlg-slg*z90))
print('The parametric VaR of the S&P portfolio at (relative geometric Loss normal) 90% is:', parametricGo_var90)


