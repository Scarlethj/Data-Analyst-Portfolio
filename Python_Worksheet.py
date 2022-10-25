#!/usr/bin/env python
# coding: utf-8

# <H2> Python Interview Test Practice </H2>

# This preparation exercise will have you use the **USA_cars_datasets.csv** file to reinforce your understanding of the following functions:
# 
# <ol> Boolean Filtering </ol>
# <ol> GROUP BY / Average Functions in Python </ol>
# <ol> Matplotlib </ol>
# 
# Once you complete the exercise, you can use the **Answer key** file to check your answers. If you get stuck, please reach out to your mentor or reach out and ask the question on #Slack!

# In[46]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
carsdata = pd.read_csv("USA_cars_datasets.csv")


# In[45]:


carsdata.head()


# <b>Q1. In the US, what is the average price per car in each state? Order this in descending order.<b>

# In[47]:


USA=carsdata.loc[(carsdata['country'] == ' usa')].groupby('state')["price"].mean().sort_values(ascending=False) 
pd.DataFrame(USA)


# <b> Q2. What is the average price per car brand within the US? Plot this out in a Bar Plot in descending order.</b>

# In[55]:


avg_price_car= carsdata.loc[(carsdata['country'] == ' usa')].groupby('brand')['price'].mean().sort_values(ascending=False)
avg_price_car.plot(kind="bar", title= "Average Price per car brand in USA ", figsize=(10,6))
plt.show()
                                      
                   


# <b> Q3. In Canada, what is the most popular brand and color of the cars that are listed for sale? </b>

# In[62]:



canadabrand = carsdata[["brand", "country"]].loc[(carsdata['country'] == ' canada')].groupby('brand').count()
print(canadabrand)
canadacolor = carsdata[["color", "country"]].loc[(carsdata['country'] == ' canada')].groupby('color').count()
print(canadacolor)


# <b> Q4. Is there a substantial price difference between the average price for a clean car in the US vs. a clean car in Canada? If yes, what is the difference? </b> 

# In[63]:


usaprice = carsdata.loc[(carsdata['country'] == ' usa')].groupby('title_status')['price'].mean()
canadaprice = carsdata.loc[(carsdata['country'] == ' canada')].groupby('title_status')['price'].mean()
print(usaprice)
print(canadaprice)


# In[67]:


pricediff = carsdata[["country", "title_status", "price"]].loc[(carsdata['title_status'] == 'clean vehicle')].groupby('country')['price'].mean()
canadaprice = float(pricediff[pricediff.index == ' canada'])
usaprice = float(pricediff[pricediff.index == ' usa'])
print("The price difference between a clean car in the US vs a clean car in Canada is ")
print(canadaprice - usaprice)


# <b> Q5. In the US / Canada - which car, brand and model is sold at the highest average price? </b>

# In[82]:


USApopularity = carsdata[["country","brand", "model", "price"]].loc[(carsdata["country"] == ' usa')].groupby(["country","brand","model"]).price.mean().sort_values(ascending=False).head(1)
Canadapopularity = carsdata[["country","brand", "model", "price"]].loc[(carsdata["country"] == ' canada')].groupby(["country","brand","model"]).price.mean().sort_values(ascending=False).head(1)
print(USApopularity)

print(Canadapopularity)


# In[ ]:




