#!/usr/bin/env python
# coding: utf-8

# # Exploratory data analysis on SuperStore Dataset Using Python
# 
# Aim :Performing an EDA and find the number of profits and losses in the business and depict them in 
# form of different visualizations                                                              
# Author:Adhavan
# 

# In[59]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import superstore dataset as pandas dataframe
data=pd.read_csv('C:/Users/Aadhavan/Downloads/SampleSuperstore.csv')


# In[11]:


data.info()
# to check infos of the data got here for analysis


# In[13]:


data.head() #to view the first five rows of our data set


# In[12]:


data.tail() #to view the last five rows of our data set


# In[14]:


data.columns #for viewing all columns


# In[15]:


data.shape #In this Dataframe, there are 9994 rows and 13 columns


# In[16]:


data.isnull().sum()# to check null values or missing values


# In[25]:


#There are no null values over the entire data
print(data['Category'].unique())
#to view the unique categories in the data frame
print(data['State'].unique())
#to view the unique stares in the data frame


# In[23]:


no_of_states=data['State'].nunique() 
print("There are %d states in this dataframe."%no_of_states)


# In[27]:


print(data['Sub-Category'].unique())
#to view the unique sub-catagory in data frame


# In[28]:


no_of_subcategory=data['Sub-Category'].nunique()
print("Categories are divided into %d subcategories"%no_of_subcategory)


# In[29]:


#to get the count of features, mean of them, Standard deviation, minimum and maximum values in that particular attribute, 25%, 50%, 75% of the values in the dataset
data.describe()


# In[31]:


data['Segment'].value_counts() #to get any specific counts


# In[34]:


loss=data[data['Profit'] < 0] #for creating loss dataset were profits were less than zero


# In[35]:


loss


# In[37]:


loss.describe()



# In[39]:


Total_loss=np.negative(loss['Profit'].sum()) #to get totall loss we were adding the profit column
print("Total loss = %.2f" %Total_loss)


# In[40]:


loss.groupby(by='Segment').sum() 


# In[41]:


#try reducing the dicounts to get more profit ,because more the discount more the loss
loss.groupby(by='Sub-Category').sum()


# In[42]:


#binders are getting more sold because of that ging discounts may lead to loss,better to give discounts on less sold products
#Binders category, machines category, and tables category were to top 3 lossed catogory
loss['Sub-Category'].value_counts()


# In[44]:


loss.groupby(by='City').sum().sort_values('Profit',ascending=True).head(10) #Top 10 lossed cities


# In[46]:


data.groupby(['State']).sum()['Sales'].nsmallest(10) #Top 10 states were sales were less


# In[47]:


data.groupby(by='Region').sum()


# In[48]:


# sales were les in south so better focus on that area


# In[52]:


plt.rcParams['figure.figsize']=(15,3) # to get fig size 4x16
plt.bar(loss['Sub-Category'],loss['Sales']);#bargraph made with x axis as subcategory and y axis as sales in top lossed
plt.rcParams.update({'font.size':10});
plt.xlabel('Sub_Category');
plt.ylabel('Sales');


# In[53]:


# we can observe the Sales of Fasteners, Appliances, Furnishings, and Accessories are very low


# In[54]:


plt.rcParams['figure.figsize']=(28,8)
plt.bar(data['Sub-Category'],data['Sales']);# bargraph made with x axis as subcategory and y axis as sales
plt.rcParams.update({'font.size':14});
plt.xlabel('Sub_Category');
plt.ylabel('Sales');


# In[55]:


# here we can observe the overall supermarket data, Fasteners, Labels, Furnishings, Art, paper, Envelopes, etc., sub-categories have very fewer sales, that’s why it needs to be improved


# In[56]:


plt.rcParams['figure.figsize']=(28,8)
plt.bar(data['Sub-Category'],data['Discount']);# bargraph made with x axis as subcategory and y axis as discounts
plt.rcParams.update({'font.size':14});
plt.xlabel('Sub_Category');
plt.ylabel('Discount');


# In[58]:


plt.rcParams['figure.figsize']=(10,8)
plt.bar(data['Ship Mode'],data['Sales']);# bargraph made with x (axis as ship modes) and y axis as sales
plt.rcParams.update({'font.size':14});
plt.xlabel('Ship Mode');
plt.ylabel('Sales');


# In[61]:


plt.rcParams['figure.figsize']=(10,5)
sns.countplot(x=data.Segment)
plt.show();


# In[62]:


# bargraph made with x axis segement's catogories with count of the therir catogories as y axis
# and the Home Office Segment, we observe that the count is less so it has to be improved


# In[66]:


plt.rcParams['figure.figsize']=(20,5)
plt.rcParams.update({'font.size':12})
sns.countplot(x='Sub-Category',data=data)# bargraph made with x subcategory's each unique and y axis as counts of the uniques
plt.show()


# In[ ]:


#it’s very much clear that the Copiers and Machines Subcategory needs improvement


# In[68]:


plt.rcParams['figure.figsize']=(20,5)
plt.rcParams.update({'font.size':12})
sns.countplot(x='Region',data=data)# bargraph made with x regions each unique and y axis as counts of the uniques
plt.show()


# In[80]:


data.corr() #method calculates the relationship between each column in your data set
sns.heatmap(data.corr(),cmap='Oranges',annot=True);#heat map is made with dataset in seaborn,
plt.rcParams['figure.figsize']=(10,5) 


# In[82]:


# with the help of this heat map
#Sales and Profit are Moderately Correlated
#Discount and Profit are Negatively Correlated
#Explorary Data Analysis done by Adhavan 


# In[ ]:




