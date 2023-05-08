# -*- coding: utf-8 -*-
"""
@author: Six/
@edited by: Tengku Muhammad Elzafir Habsjah
"""

#importing libraries 
import pandas as pd 

#importe file
data=pd.read_excel('SP500Data.xlsx', sheet_name='Sheet1') #read the data into a panda DataFrame

#Compute L&P
data['L&P']=-data['Prix'].diff(periods=1) #compute the L&P of gold
LP=data['L&P'].dropna() #supress the NaN of the L&P
print(LP) #print the L&P on the screen to chek and compare with Excel

#Compute the Value at Risk for different confidence level
historic_var95 = LP.quantile(.95)
print('The historical VaR of the S&P500 portfolio at 95% is:', historic_var95)

historic_var99 = LP.quantile(.99)
print('The historical VaR of the S&P500 portfolio at 99% is:', historic_var99)

historic_var90 = LP.quantile(.90)
print('The historical VaR of the S&P500 portfolio at 90% is:', historic_var90)
