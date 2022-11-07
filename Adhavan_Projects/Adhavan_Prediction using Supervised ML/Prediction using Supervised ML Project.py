#!/usr/bin/env python
# coding: utf-8

# # Prediction using Supervised ML
# Aim :To Predict the percentage of student based on the number of hours ofstudy
# and to predicted score if a student studies for 9.25hours/day
# Author:P.Adhavan

# In[1]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression


# In[3]:




data = pd.read_csv('C:/Users/Aadhavan/Downloads/student_scores - student_scores.csv')# importing our data set to pandas
data.head()  # check top 5 rows 


# In[5]:



data.shape  # to get number of rows and columns


# In[6]:


data.describe()# to get the description of data


# In[7]:


sns.scatterplot(x=data['Hours'], y=data['Scores']);   # plot the data


# In[8]:


sns.regplot(x=data['Hours'], y=data['Scores']);  # regression plot gives a better and clear visualization for such data


# In[9]:


X = data[['Hours']]
y = data['Scores'] 


# In[82]:




train_X, val_X, train_y, val_y = train_test_split(X, y,random_state =0) #splitting x and y for ML as these percentages with the help of train_test_split 

print("78%",train_X.shape,"100%", X.shape,"28%",val_X.shape)


# In[83]:


regressor = LinearRegression()  


# In[84]:


regressor.fit(train_X, train_y)   ## training the model


# In[85]:


pred_y = regressor.predict(val_X) ## prediction


# In[86]:


pd.DataFrame({'Actual': val_y, 'Predicted': pred_y})  ## view actual and predicted on test set side-by-side


# In[87]:


## Actual vs Predicted distribution plot 

sns.kdeplot(pred_y,label="Predicted", shade=True);

sns.kdeplot(data=val_y, label="Actual", shade=True);


# In[89]:



print('Train accuracy: ', regressor.score(train_X, train_y),'\nTest accuracy : ', regressor.score(val_X, val_y) )


# In[93]:


# Predict percent for custom input value for hours
# Q. What will be predicted score if a student studies for 9.25 hrs/ day? 

h = [[9.25]]

s = regressor.predict(h)# predict is used to predict the value for paticular variable
print('A student who studies ', h[0][0] , ' hours is estimated to score ', s[0])


# In[ ]:





# In[ ]:




