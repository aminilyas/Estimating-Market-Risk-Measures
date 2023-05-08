# -*- coding: utf-8 -*-
"""
%matplotlib

@author: Six
@edited by: Esteban Lopez
"""

#importing libraries 
import pandas as pd 
import scipy.stats as sp 
import matplotlib.pyplot as plt


#importe file
data=pd.read_excel('SP500Data.xlsx',sheet_name='Sheet1') #read the data into a panda DataFrame

#Compute L&P
data['L&P']=data['Prix'].diff(periods=-1) #compute the L&P of gold
LP=data['L&P'].dropna() #supress the NaN of the L&P
#print(LP) #print the L&P on the screen to chek and compare with Excel

mLP=LP.mean()
sLP=LP.std()

sp.probplot(LP, dist=sp.norm(loc=mLP, scale=sLP), fit=False, plot=plt)
