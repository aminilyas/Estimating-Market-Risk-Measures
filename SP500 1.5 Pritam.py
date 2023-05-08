# -*- coding: utf-8 -*-
"""
@author: Six
@edited by: Pritam Ritu Raj

"""


import scipy.stats as sp 

n=1000
alpha=0.95
VaR95=sp.norm.ppf(alpha)

alphaI=0.90
beta=1/2+alphaI/2
zBeta=sp.norm.ppf(beta)

eps=0.1
Ieps_inf=VaR95-eps/2*VaR95
Ieps_sup=VaR95+eps/2*VaR95
P_Ieps=sp.norm.cdf(Ieps_sup)-sp.norm.cdf(Ieps_inf)
p=1-sp.norm.cdf(Ieps_sup)

se=(p*(1-p)/n)**0.5/P_Ieps

CI_inf=VaR95-se*zBeta
CI_sup=VaR95+se*zBeta

print('The condidence interval is [', CI_inf,';',CI_sup,']')
