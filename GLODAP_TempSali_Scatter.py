#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 05:25:33 2020

@author: Tina-CTH
"""

import numpy as np
import matplotlib.tri as tri
import matplotlib.gridspec
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt
import pandas as pd

glodap = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv')

j_1980s = glodap[glodap['Year']==1988]
j_1990s = glodap[glodap['Year'].between(1990,2000, inclusive= False)]
j_2000s = glodap[glodap['Year'].between(2000,2010, inclusive= False)]
j_2010s = glodap[glodap['Year'].between(2010,2020, inclusive= False)]

#%% 
#Create grid values first.
xi = np.linspace(-75, 63, 139)
yi = np.linspace(-1100, 0, 11)          
Xi, Yi = np.meshgrid(xi, yi)

#00s
x_2000s = j_2000s['Latitude']
y_2000s = (-j_2000s['Depth'])
t_2000s = j_2000s['Temperature']
s_2000s = j_2000s['Salinity']

triang_00 = tri.Triangulation(x_2000s, y_2000s)
interpolatort_00 = tri.LinearTriInterpolator(triang_00, t_2000s)
interpolators_00 = tri.LinearTriInterpolator(triang_00, s_2000s)

ti_00_1 = interpolatort_00(Xi, Yi)
si_00_1 = interpolators_00(Xi, Yi)

#10s
x_2010s = j_2010s['Latitude']
y_2010s = (-j_2010s['Depth'])
t_2010s = j_2010s['Temperature']
s_2010s = j_2010s['Salinity']

triang_10 = tri.Triangulation(x_2010s, y_2010s)
interpolatort_10 = tri.LinearTriInterpolator(triang_10, t_2010s)
interpolators_10 = tri.LinearTriInterpolator(triang_10, s_2010s)

ti_10_1 = interpolatort_10(Xi, Yi)
si_10_1 = interpolators_10(Xi, Yi)

t1_1 = (ti_10_1-ti_00_1)
s1_1 = (si_10_1-si_00_1)

#%%

xi = np.linspace(-75, 63, 139)
yi = np.linspace(-2000, 0, 11)
             
Xi, Yi = np.meshgrid(xi, yi)

#00s
x_2000s = j_2000s['Latitude']
y_2000s = (-j_2000s['Depth'])
t_2000s = j_2000s['Temperature']
s_2000s = j_2000s['Salinity']

triang_00 = tri.Triangulation(x_2000s, y_2000s)
interpolatort_00 = tri.LinearTriInterpolator(triang_00, t_2000s)
interpolators_00 = tri.LinearTriInterpolator(triang_00, s_2000s)

ti_00_2 = interpolatort_00(Xi, Yi)
si_00_2 = interpolators_00(Xi, Yi)

#10s
x_2010s = j_2010s['Latitude']
y_2010s = (-j_2010s['Depth'])
t_2010s = j_2010s['Temperature']
s_2010s = j_2010s['Salinity']

triang_10 = tri.Triangulation(x_2010s, y_2010s)
interpolatort_10 = tri.LinearTriInterpolator(triang_10, t_2010s)
interpolators_10 = tri.LinearTriInterpolator(triang_10, s_2010s)

ti_10_2 = interpolatort_10(Xi, Yi)
si_10_2 = interpolators_10(Xi, Yi)

t1_2 = (ti_10_2-ti_00_2)
s1_2 = (si_10_2-si_00_2)

#%%
#Create grid values first.
xi = np.linspace(-75, 63, 139)
yi = np.linspace(-4100, -1900, 21)
             
Xi, Yi = np.meshgrid(xi, yi)
#00s
x_2000s = j_2000s['Latitude']
y_2000s = (-j_2000s['Depth'])
t_2000s = j_2000s['Temperature']
s_2000s = j_2000s['Salinity']

triang_00 = tri.Triangulation(x_2000s, y_2000s)
interpolatort_00 = tri.LinearTriInterpolator(triang_00, t_2000s)
interpolators_00 = tri.LinearTriInterpolator(triang_00, s_2000s)

ti_00_4 = interpolatort_00(Xi, Yi)
si_00_4 = interpolators_00(Xi, Yi)

#10s
x_2010s = j_2010s['Latitude']
y_2010s = (-j_2010s['Depth'])
t_2010s = j_2010s['Temperature']
s_2010s = j_2010s['Salinity']

triang_10 = tri.Triangulation(x_2010s, y_2010s)
interpolatort_10 = tri.LinearTriInterpolator(triang_10, t_2010s)
interpolators_10 = tri.LinearTriInterpolator(triang_10, s_2010s)

ti_10_4 = interpolatort_10(Xi, Yi)
si_10_4 = interpolators_10(Xi, Yi)

t1_4 = (ti_10_4-ti_00_4)
s1_4 = (si_10_4-si_00_4)

#%%
# Create grid values first.
xi = np.linspace(-75, 63, 139)
yi = np.linspace(-6100, -3900, 11)
             
Xi, Yi = np.meshgrid(xi, yi)

#00s
x_2000s = j_2000s['Latitude']
y_2000s = (-j_2000s['Depth'])
t_2000s = j_2000s['Temperature']
s_2000s = j_2000s['Salinity']

triang_00 = tri.Triangulation(x_2000s, y_2000s)
interpolatort_00 = tri.LinearTriInterpolator(triang_00, t_2000s)
interpolators_00 = tri.LinearTriInterpolator(triang_00, s_2000s)

ti_00_6 = interpolatort_00(Xi, Yi)
si_00_6 = interpolators_00(Xi, Yi)

#10s
x_2010s = j_2010s['Latitude']
y_2010s = (-j_2010s['Depth'])
t_2010s = j_2010s['Temperature']
s_2010s = j_2010s['Salinity']

triang_10 = tri.Triangulation(x_2010s, y_2010s)
interpolatort_10 = tri.LinearTriInterpolator(triang_10, t_2010s)
interpolators_10 = tri.LinearTriInterpolator(triang_10, s_2010s)

ti_10_6 = interpolatort_10(Xi, Yi)
si_10_6 = interpolators_10(Xi, Yi)


t1_6 = (ti_10_6-ti_00_6)
s1_6 = (si_10_6-si_00_6)

#%%
from scipy.stats import spearmanr

params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 20, # fontsize for x and y labels (was 10)
    'axes.titlesize': 20,
    'font.size': 20, # was 10
    'legend.fontsize': 15, # was 10
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'figure.figsize': [5, 5],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)

fig,ax=plt.subplots()
plt.suptitle('GLODAP 2010 VS 2000 interpoaltion scatterplot')
plt.scatter(x=t1_1,y=s1_1, marker='x', color='blue', label='1000m')
plt.scatter(x=t1_2,y=s1_2, marker='x', color='purple',label='2000m')
plt.scatter(x=t1_4,y=s1_4, marker='x', color='yellow',label='4000m')
plt.scatter(x=t1_6,y=s1_6, marker='x', color='red',label='6000m')

comb_x=np.ma.concatenate((t1_1,t1_2,t1_4,t1_6))
comb_y=np.ma.concatenate((s1_1,s1_2,s1_4,s1_6))
fit, cov=np.polyfit(comb_x,comb_y, 1, cov=True)

plt.legend()
ax.set_ylabel('Salinity')
ax.set_xlabel('Temperature')
fig.show()