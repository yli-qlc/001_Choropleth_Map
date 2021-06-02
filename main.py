#Prerequisites
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd


#pd.set_option('display.max_columns', None)

#Read the shape file
df1 = gpd.read_file(r"...\chn_admbnda_adm1_ocha_2020.shp")
print(list(df1))
print(df1.head)

#Read the file with the target variable
df2 = pd.read_csv(r"...\Age.csv")

#Merge the two files
merged=pd.merge(df1, df2, on='ADM1_PCODE')
merged = df1.merge(df2, left_on = 'ADM1_PCODE', right_on = 'ADM1_PCODE',how = 'outer')
merged.fillna(0, inplace=True)
print(merged.head)
print (merged.dtypes)

#Create the map
fig, ax = plt.subplots(1, figsize=(10,6))
merged.plot(column='Dependency_Ratio', cmap='Reds',  linewidth=1, ax=ax, edgecolor='0.9', legend=True)
ax.axis('off')
plt.show()