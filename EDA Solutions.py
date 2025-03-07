### Python project EDA and Data visulazation of Airbnb(2024)
import numpy as num
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sb

data= pd.read_csv('datasets.csv' ,encoding_errors='ignore')
print(data.head())  # it retrun first five rows in table
print(data.tail())  # it retrun last Five rows in table
print(data.shape)   # it retrun numbers of columns and rows
print(data.info())  # it retrun Column Names and Datatypes
#****statistical summary******

print(data.describe()) # it retrun only Numerical columns 

## ****data cleaning****


#data.fillna()
print(data.isnull().sum()) # it retrun null values from each column and adding up
data.dropna(inplace= True) # it delete the null values
print(data.isnull().sum()) # to see null values in each column
#print(data.shape)

print(data.duplicated().sum()) # to see dulpicate rows in number 

print(data[data.duplicated()])## to see duplicate rows in data Form

## to delete duplicate rows ####

print(data.drop_duplicates(inplace=True))
print(data.duplicated().sum())


print(data.dtypes)# to see datatypes of column

#  to change datatype of column#  #

data['id'] = data['id'].astype('object')
data['host_id']=data['host_id'].astype('object')
print(data.dtypes)

#***Data Analysis********

#------Univariate Analysis--------   #

# ----price distribution-----#
print(data['price'])
sb.histplot(data=data, x='price') ## histogram graph
mp.title('price Distribution')
mp.xlabel('price')
mp.ylabel('Frequency')
mp.show()

## Identifying the outliners in price distribution (finding data points that are different from the rest of the data set.)

sb.boxplot(data=data,x='price')  # this for total price distribution in BoxPlot Graph

df=data[data['price']<1550]  # Remove  data points that are different from the rest of the data set.
sb.boxplot(data=df, x='price')
mp.title('Price Distribution')
mp.ylabel('Frequency')
mp.show()

#   total price distribution for 1550   #

sb.histplot(data=df,x='price',bins=100)
mp.ylabel('Frequency')
mp.show()

#-----Availability_365 Distribution----#

sb.histplot(data=df,x="availability_365")
mp.title('Avaliability_365 Distribution')
mp.ylabel('Frequency')
mp.show()

#---Avg"price"for neighbourhood_group USING "GROUP BY"-----#

print(df.groupby(by='neighbourhood_group',)['price'].mean())

#---- Featuring Engineering -----#

#------ Adding New Column to Orginal dataset-------

df['price per bed']= df['price']/df['beds']
print(df.head())

# ---Average price per bed for neighbourhood_group using"group by" ----#

print(df.groupby(by="neighbourhood_group")['price per bed'].mean())


#*** Bivariante analysis*****

sb.barplot(data=df,x="neighbourhood_group",y='price',hue='room_type'), # bar_graph neighbour v/s price
mp.title("bargraph")
mp.show()


#**Scatterr Plot Graph***

sb.scatterplot(data=df,x="number_of_reviews",y='price',hue='neighbourhood_group') # scatter_polt graph  price v/s number_of_reviws
mp.title('scatter graph')
mp.show()

#*** pair_grpah****

sb.pairplot(data=df,vars=['price','minimum_nights','number_of_reviews','availability_365'],hue="room_type")
mp.show()

#***Geographical Distribution of airbnb******

sb.scatterplot(data=df,x="longitude",y='latitude',hue='room_type')
mp.title('geographical Distribbution of Airbnb')
mp.show()

#***heat map correlation with one variable to another vairable****

corr=df[["latitude","longitude",'beds','number_of_reviews','minimum_nights','reviews_per_month','availability_365']].corr() # Correlation
sb.heatmap(data=corr,annot=True)
mp.figure(figsize=(6,5))
mp.show()