#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['figure.figsize']=(20.0,10.0)
data=pd.read_csv("headbrain.csv")
print(data.shape)
data.head()


# In[23]:


x=data["Head Size(cm^3)"].values


# In[24]:


y=data["Brain Weight(grams)"].values


# In[25]:


#mean x and y
mean_x=np.mean(x)
mean_y=np.mean(y)


# In[26]:


#total no of values
n=len(x)


# In[27]:


#use the formula to calculate b1 and b2
numer=0
denom=0
for i in range(n):
    numer+=(x[i]-mean_x)*(y[i]-mean_y)
    denom+=(x[i]-mean_x)**2
b1=numer/denom
b0=mean_y-(b1*mean_x)
print(b1,b0)


# In[28]:


max_x=np.max(x)+100
min_x=np.min(x)-100
X=np.linspace(min_x,max_x,1000)
Y=b0+b1*X
plt.plot(X,Y,color='#58b970',label="regression_line")
plt.scatter(x,y,c='#ef5423',label="scatter plot")
plt.xlabel("head size in cm^3")
plt.ylabel("brain weight in grams")
plt.legend()
plt.show()


# In[30]:


ss_t=0
ss_r=0
for i in range(n):
    y_pred=b0+b1*x[i]
    ss_t+=(y[i]-mean_y)**2
    ss_r+=(y_pred-y[i])**2
r2=1-(ss_r/ss_t)
print(r2)


# In[ ]:





# In[ ]:





# In[ ]:




