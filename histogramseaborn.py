import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv(r'C:\Users\AMAN KUMAR SINGH\Downloads\DataFile\Height of Male and Female by Country 2022.csv')
print(df)

# sns.boxplot(x='Male Height in Cm', data=df)
# sns.distplot(df['Male Height in Cm'])

##Conclusion: 
# Graph is left skewed here, and data is continuous here in the graph. It is bimodal.
# Range of height in male varies from 160 to 188cm.
## There are no outliers in the graph here which is proved via boxplot graph.


# sns.distplot(df['Female Height in Cm'])
sns.boxplot(x='Male Height in Cm', data=df)
# Conclusion:
##Graph is rightly skewed and here mean is greater than median. It is a bell curve graph( which means it has single peak at the top) and the graph is unimodal.
##Range of height in female varies from 150 TO 170 cm.
##There are no outliers in the graph here.
plt.show()
