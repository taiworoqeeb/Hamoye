#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


mydata = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv', error_bad_lines=False)
mydata.to_csv('myfueldata.csv', index=False)


# In[12]:


A = [1,2,3,4,5,6]
B = [13, 21, 34]
A.extend(B)
print(A)


# In[13]:


np.identity(3)


# In[21]:


mydata.fuel_type_code_pudl.describe(include='all')


# In[22]:


mydata.fuel_mmbtu_per_unit.std()


# In[26]:


mydata.fuel_mmbtu_per_unit.quantile(0.75)


# In[43]:


plt.figure(figsize=(7,4))#describing the dimesnsion of the figure
plt.xticks(rotation=90)
mydata.fuel_cost_per_unit_delivered.value_counts().nlargest(6).plot(kind='bar')
plt.title("Fuel data by unit")
plt.ylabel('report_year')
plt.ylim(1994, 2015)
plt.xlabel('fuel_cost_per_unit_delivered');


# In[30]:


mydata


# In[33]:


d = mydata[['report_year', 'fuel_cost_per_unit_delivered']]
print(d)


# In[35]:


plt.scatter(d.report_year, d.fuel_cost_per_unit_delivered)
plt.show()


# In[36]:


plt.scatter(mydata.report_year, mydata.fuel_type_code_pudl)
plt.show()


# In[47]:


mydata.skew()


# In[48]:


mydata.kurtosis()


# In[49]:


mydata.isnull().sum()


# In[50]:


mydata.info()


# In[56]:


mydata.fuel_unit.describe(include='all')


# In[ ]:




