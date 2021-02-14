#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates


# In[5]:


WBI = pd.read_csv('../Data/WBI.csv') 
WBI = WBI.dropna()
WBI


# In[6]:


GDP = WBI['GDP']
Close = WBI['Close']
WBI


# In[7]:


WBI['WBII'] = (Close / GDP)*100
WBI


# In[8]:


WBI['WBIAV'] = WBI['WBII'].mean()
WBIAV = WBI['WBIAV']
WBI


# In[9]:


WBI['SDIFF'] = WBI['WBII'] - WBI['WBIAV']
WBI


# In[10]:


fig, ax = plt.subplots(figsize=(18, 10))
ax.tick_params(axis='x', colors='navy')
ax.tick_params(axis='y', colors='navy')

plt.annotate('Program by: Taylor Bommarito', xy=(0.85, 0.08), xycoords='axes fraction', color='navy')

plt.rc('axes',edgecolor='navy')
plt.rc('xtick',labelsize=18)
plt.rc('ytick',labelsize=18)
WBI['Date'] = pd.to_datetime(WBI['Date'])
WBI.sort_values('Date', inplace=True)
Date = WBI['Date']
plt.plot_date(Date, Close, color='green', label='Annual W5000 Close Price', linestyle='solid')
plt.plot_date(Date, GDP, color='blue', label='Annual GDP', linestyle='solid')
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.legend( loc='upper left')
plt.xlabel('Date', color = 'navy', fontsize=18, weight='bold')
plt.ylabel('(%)', color = 'navy', fontsize=18, weight='bold')
#plt.title('Warren Buffet Indicator', color='navy', fontsize=18, weight='bold')
plt.title('Warren Buffett Indicator : {:.2f}%'.format(WBI.loc[WBI.index[-1],'WBII']), color = 'navy', fontsize=18, weight='bold')
plt.show()


# In[11]:


fig, ax = plt.subplots(figsize=(18, 10))
ax.tick_params(axis='x', colors='navy')
ax.tick_params(axis='y', colors='navy')

plt.annotate('Program by: Taylor Bommarito', xy=(0.85, 0.08), xycoords='axes fraction', color='navy')

plt.rc('axes',edgecolor='navy')
plt.rc('xtick',labelsize=18)
plt.rc('ytick',labelsize=18)
WBI['Date'] = pd.to_datetime(WBI['Date'])
WBI.sort_values('Date', inplace=True)
Date = WBI['Date']
plt.plot_date(Date, WBI['WBII'], color='red', label='Warren Buffett Indicator in %', linestyle='solid')
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.legend( loc='upper left')
plt.xlabel('Date', color = 'navy', fontsize=18, weight='bold')
plt.ylabel('(%)', color = 'navy', fontsize=18, weight='bold')
#plt.title('Warren Buffet Indicator', color='navy', fontsize=18, weight='bold')
plt.title('Warren Buffett Indicator : {:.2f}%'.format(WBI.loc[WBI.index[-1],'WBII']), color = 'navy', fontsize=18, weight='bold')
plt.show()


# In[22]:


from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters ()

fig, ax = plt.subplots(figsize=(18, 10))
ax.tick_params(axis='x', colors='navy')
ax.tick_params(axis='y', colors='blue')

plt.annotate('Program by: Taylor Bommarito', xy=(0.035, 0.86), xycoords='axes fraction', color='navy', fontsize=12)
plt.annotate('Warren Buffett Indicator Average (Starting in 1990) : {:.2f}%'.format(WBI.loc[WBI.index[-1], 'WBIAV']), color = 'navy', fontsize=24, weight='bold', xy=(0.16, 1.106), xycoords='axes fraction')
plt.annotate('Amount Above Average : {:.2f}%'.format(WBI.loc[WBI.index[-1], 'SDIFF']), color = 'navy', fontsize=24, weight='bold', xy=(0.33, 1.03), xycoords='axes fraction')

plt.rc('axes',edgecolor='navy')
plt.rc('xtick',labelsize=18)
plt.rc('ytick',labelsize=18)
WBI['Date'] = pd.to_datetime(WBI['Date'])
WBI.sort_values('Date', inplace=True)
Date = WBI['Date']

plt.plot_date(Date, Close, color='green', label='Annual W5000 Close Price $', linestyle=(0,(5, 10)), markersize=0)
plt.plot_date(Date, GDP, color='blue', label='Annual GDP (In Billions) $', linestyle=(0, (5, 10)), markersize=0)
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.legend( loc='upper left', prop={"size":15})
plt.xlabel('Annual Date', color = 'navy', fontsize=20, weight='bold')
plt.ylabel('$ for W5000 Index & GDP (dashed lines)', color = 'green', fontsize=20, weight='bold')

ax1 = ax.twinx()
curve1 = plt.plot_date(Date, WBI['WBII'], label='Annual Warren Buffett Indicator in %', color='red', linestyle= 'solid', markersize=0)
curve1 = plt.plot_date(Date, WBI['WBIAV'], label='Average Warren Buffett Indicator in % (Benchmark)', color='black', linestyle= 'solid', markersize=0)
plt.ylabel('% for Indicator (solid line)', color = 'red', fontsize=20, weight='bold')
ax1.tick_params(axis='y', colors='red')
plt.legend(loc='lower right', prop={"size":15})

plt.title('Current 2021 Warren Buffett Indicator : {:.2f}%'.format(WBI.loc[WBI.index[-1],'WBII']), color = 'navy', fontsize=24, weight='bold', pad=100)
plt.show()


# In[ ]:




