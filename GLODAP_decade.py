import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
import matplotlib
from scipy.interpolate import griddata

glodap = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv') 

j_1980s = glodap[glodap['Year']==1988]
j_1990s = glodap[glodap['Year'].between(1990,2000, inclusive= False)]
j_2000s = glodap[glodap['Year'].between(2000,2010, inclusive= False)]
j_2010s = glodap[glodap['Year'].between(2010,2020, inclusive= False)]


dsTempA=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
dsSaliA=xr.open_dataset('Salinity_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
TempA=dsTempA.THETAO
SaliA=dsSaliA.SALINITY
xi = np.array(TempA.LAT.data)
yi = np.array(TempA.DEPTHT.data)


x_1990s = j_1990s['Latitude']
y_1990s = j_1990s['Depth']
t_1990s = j_1990s['Temperature']
s_1990s = j_1990s['Salinity']

ti_90 = griddata((x_1990s, y_1990s), t_1990s, (xi[None,:], yi[:,None]), method='linear',rescale=True)
si_90 = griddata((x_1990s, y_1990s), s_1990s, (xi[None,:], yi[:,None]), method='linear',rescale=True)

x_2000s = j_2000s['Latitude']
y_2000s = j_2000s['Depth']
t_2000s = j_2000s['Temperature']
s_2000s = j_2000s['Salinity']

ti_00 = griddata((x_2000s, y_2000s), t_2000s, (xi[None,:], yi[:,None]), method='linear',rescale=True)
si_00 = griddata((x_2000s, y_2000s), s_2000s, (xi[None,:], yi[:,None]), method='linear',rescale=True)

params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 25, # fontsize for x and y labels (was 10)
    'axes.titlesize': 25,
    'font.size': 20, # was 10
    'legend.fontsize': 20, # was 10
    'xtick.labelsize': 20,
    'ytick.labelsize': 20,
    'figure.figsize': [25, 8],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)

fig , (ax1,ax2) = plt.subplots(ncols=2)
#plt.suptitle('2000s vs 1990s Atlantic')

t2=(ti_90)-(ti_00)
s2=(si_90)-(si_00)

levels2=np.arange(-5,5.5,0.5)
cntr1 = ax1.contourf(xi, yi, t2, levels=levels2, cmap="Spectral")
levels1=np.arange(-1,1.1,0.1)
cntr2 = ax2.contourf(xi, yi, s2, levels=levels1, cmap="Spectral")

cbar1=fig.colorbar(cntr1, ax=ax1)
cbar1.ax.set_ylabel('Temperature (°C)')
ax1.set(xlim=(-80, 80), ylim=(6100, 0))
# ax1.plot(x_1990s, y_1990s, 'ko', ms=0.75, color='purple')
# ax1.plot(x_2000s, y_2000s, 'ko', ms=0.75, color='green')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Latitude (degrees)')

cbar2=fig.colorbar(cntr2, ax=ax2)
cbar2.ax.set_ylabel('Salinity (ppt)')
ax2.set(xlim=(-80, 80), ylim=(6100, 0))
# ax2.plot(x_1990s, y_1990s, 'ko', ms=0.75, color='purple')
# ax2.plot(x_2000s, y_2000s, 'ko', ms=0.75, color='green')
ax2.set_ylabel('Depth (m)')
ax2.set_xlabel('Latitude (degrees)')

#%%
glodap = pd.read_csv('GLODAPv2_2020_A16_Atlantic.csv') 

j_1980s = glodap[glodap['Year']==1988]
j_1990s = glodap[glodap['Year'].between(1990,2000, inclusive= False)]
j_2000s = glodap[glodap['Year'].between(2000,2010, inclusive= False)]
j_2010s = glodap[glodap['Year'].between(2010,2020, inclusive= False)]


dsTempA=xr.open_dataset('Temperature_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
dsSaliA=xr.open_dataset('Salinity_NEMO-C14a_Hist_1m_1981-2017_Atlantic_A16.nc')
TempA=dsTempA.THETAO
SaliA=dsSaliA.SALINITY
xi = np.array(TempA.LAT.data)
yi = np.array(TempA.DEPTHT.data)


x_1990s = j_2010s['Latitude']
y_1990s = j_2010s['Depth']
t_1990s = j_2010s['Temperature']
s_1990s = j_2010s['Salinity']

ti_90 = griddata((x_1990s, y_1990s), t_1990s, (xi[None,:], yi[:,None]), method='linear',rescale=True)
si_90 = griddata((x_1990s, y_1990s), s_1990s, (xi[None,:], yi[:,None]), method='linear',rescale=True)

x_2000s = j_2000s['Latitude']
y_2000s = j_2000s['Depth']
t_2000s = j_2000s['Temperature']
s_2000s = j_2000s['Salinity']

ti_00 = griddata((x_2000s, y_2000s), t_2000s, (xi[None,:], yi[:,None]), method='linear',rescale=True)
si_00 = griddata((x_2000s, y_2000s), s_2000s, (xi[None,:], yi[:,None]), method='linear',rescale=True)

params = {
    'image.cmap': 'Blues',
    'axes.labelsize': 20, # fontsize for x and y labels (was 10)
    'axes.titlesize': 20,
    'font.size': 20, # was 10
    'legend.fontsize': 15, # was 10
    'xtick.labelsize': 15,
    'ytick.labelsize': 15,
    'figure.figsize': [25, 8],
    'font.family': 'serif',
}

#updating parameters for plotting
matplotlib.rcParams.update(params)

fig , (ax1,ax2) = plt.subplots(ncols=2)
#plt.suptitle('2000s vs 1990s Atlantic')

t2=(ti_00)-(ti_90)
s2=(si_00)-(si_90)

levels2=np.arange(-5,5.5,0.5)
cntr1 = ax1.contourf(xi, yi, t2, levels=levels2, cmap="Spectral")
levels1=np.arange(-1,1.1,0.1)
cntr2 = ax2.contourf(xi, yi, s2, levels=levels1, cmap="Spectral")

cbar1=fig.colorbar(cntr1, ax=ax1)
cbar1.ax.set_ylabel('Temperature (°C)')
ax1.set(xlim=(-80, 80), ylim=(6100, 0))
# ax1.plot(x_1990s, y_1990s, 'ko', ms=0.75, color='purple')
# ax1.plot(x_2000s, y_2000s, 'ko', ms=0.75, color='green')
ax1.set_ylabel('Depth (m)')
ax1.set_xlabel('Latitude (degrees)')

cbar2=fig.colorbar(cntr2, ax=ax2)
cbar2.ax.set_ylabel('Salinity (ppt)')
ax2.set(xlim=(-80, 80), ylim=(6100, 0))
# ax2.plot(x_1990s, y_1990s, 'ko', ms=0.75, color='purple')
# ax2.plot(x_2000s, y_2000s, 'ko', ms=0.75, color='green')
ax2.set_ylabel('Depth (m)')
ax2.set_xlabel('Latitude (degrees)')