
"""
Cluster para datos flor iris.
"""

# Import helpful packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import zipfile as zp

from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import pdist

# Read the zip file and import the iris dataset.
iris = zp.ZipFile('Datos/8836201-6f9306ad21398ea43cba4f7d537619d0e07d5ae3.zip')
iris = pd.read_csv(iris.open('8836201-6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'))
iris = iris.rename(columns={"sepal.length": "s_length", "sepal.width": "s_width", "petal.length":"p_length", "petal.width":"p_width"})

###############################################################################
#                            1.- Knowing the data                             #

# Information about the iris dataframe (column names, dtypes, etc): 
iris.info()

# See what's in the iris data (first 5 rows)
iris.head()

# Let's see how many samples we have of each variety
iris["variety"].value_counts()

# Show some descriptive statistics for numeric columns:
print("Descriptive Statistic:")
print(iris.describe())
# iris.isnull().sum()  #t here is no null values

###############################################################################
#                           2.- Data visualization                            #

# Univariate analysis

# Detecting outliers (by variable) with BoxPlot
iris.boxplot(figsize=(10, 4))
plt.show()

# Histogram
sns.set_style("white")
fig, axs = plt.subplots(1, 4, figsize=(10,4), tight_layout=True)
axs[0].hist(iris['s_length'], bins=15, density=True)
axs[1].hist(iris['s_width'], bins=15, density=True)
axs[2].hist(iris['p_length'], bins=15, density=True)
axs[3].hist(iris['p_width'], bins=15, density=True)
axs[0].set_title('sepal_length')
axs[1].set_title('sepal_width')
axs[2].set_title('petal_length')
axs[3].set_title('petal_width')
plt.show()

#plt.close(fig)
fig, axs = plt.subplots(1, 4, figsize=(10,4), tight_layout=True)
axs[0].hist(iris['s_length'], bins=15, density=True)
axs[1].hist(iris['s_width'], bins=15, density=True)
axs[2].hist(iris['p_length'], bins=15, density=True)
axs[3].hist(iris['p_width'], bins=15, density=True)
axs[0].set_title('sepal_length')
axs[1].set_title('sepal_width')
axs[2].set_title('petal_length')
axs[3].set_title('petal_width')
plt.show()

# Plotting the probability density function and the histogram
fig, axs = plt.subplots(1, 4, figsize=(10,4), tight_layout=True)
sns.FacetGrid(iris, hue="variety").map(sns.distplot, "s_length", ax=axs[0]).add_legend();
sns.FacetGrid(iris, hue="variety").map(sns.distplot, "s_width", ax=axs[1]).add_legend();
sns.FacetGrid(iris, hue="variety").map(sns.distplot, "p_length", ax=axs[2]).add_legend();
sns.FacetGrid(iris, hue="variety").map(sns.distplot, "p_width", ax=axs[3]).add_legend();
plt.show()

# Bivariate analysis

# scatter plot
sns.pairplot(iris, hue="variety", height=3)
plt.show()

plt.close('all')
###############################################################################
#                      3.-  Hierarchical clustering                           #

def clus_agglome(dat, meth, order): 
    # Generate the linkage matrix using the (Ward, ) algorithm
    Z = linkage(dat['x'].values, method=meth)   #'ward', 'complete', single'
    
    # Generate the dendrogram (and save)

    #plt.ioff()     # Turn interactive plotting off
    f = plt.figure(figsize=(12, 5))
    plt.title('Hierarchical Clustering Dendrogram with link=' +meth)
    plt.ylabel('Distance in the space four dimensions')
    dendrogram( 
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,) # font size for the x axis labels
    plt.savefig('dendogram_'+meth+'.png')
    plt.show()
    plt.close(f)

    # ============
    # Create cluster objects
    clus_obj = AgglomerativeClustering(n_clusters=3, linkage=meth)

    # Assign the elements to groups
    group = clus_obj.fit_predict(dat['x'])
  
    # Evaluate the success ratio of the clustering
    d = pd.crosstab(dat['vari'].variety, group, margins=True, margins_name="Total")
    d = d.reindex(order)
    truth = sum(np.diag(d))
    success = 100*truth/(np.shape(dat['x'])[0])

    # Check the Cophenetic Correlation Coefficient to assess quality of clusters:
    c, coph_dists = cophenet(Z, pdist(dat['x']))
    
    #  Let's plot our clusters    
    plt.figure()
    plt.subplot(121)
    plt.scatter(dat['x'].s_length, dat['x'].s_width, s=10, c=vari.variety_num)
    plt.title("Real groups")
    plt.xticks(())
    plt.yticks(())

    plt.subplot(122)
    plt.scatter(dat['x'].s_length, dat['x'].s_width, s=10, c=group)           # predicted
    plt.title('Predicted groups ' +meth)
    plt.xticks(())
    plt.yticks(())
    plt.show()
    
    resul=dict();
    resul['accuracy'] = success 
    resul['cophe'] = c
    
    return resul

## ============ 

# Assign a numerical value to the variety
def set_value(row_number, assigned_value): 
    return assigned_value[row_number] 
## ============ 
print("Hierarchical clustering...")
    
order1 = ["Versicolor", "Setosa", "Virginica"]
order2 = ["Virginica", "Setosa", "Versicolor"]
variety_dict ={'Versicolor' : 0, 'Setosa' : 1, 'Virginica' : 2} # Create a dictionary

vari = pd.DataFrame({'variety': iris.variety})   # We recover the original variety
vari['variety_num'] = vari['variety'].apply(set_value, args =(variety_dict, )) 
   
dat_en2 = dict()
dat_en2['vari'] = vari
dat_en2['x'] = iris.drop('variety', axis=1)
 
Result = pd.DataFrame([clus_agglome(dat_en2, 'ward', order1),
                       clus_agglome(dat_en2, 'complete', order2),
                       clus_agglome(dat_en2, 'single', order1)
                      ])
Result.rename(index={0:'Ward Linkage',1:'Complete Linkage',2:'Single Linkage'}, inplace=True)
  
print ("Success ratio and cophenetic correlation:")
print(Result)

## =========
print("Hierarchical clustering without outliers...")
# Detecting outliers (by variable) with the Interquartile Range (IQR)
q1 = iris.quantile(0.25)
q3  = iris.quantile(0.75)
iqr = q3 - q1
((iris < (q1-(1.5*iqr)))|(iris > (q3+(1.5*iqr)))).sum()
# As we can see: there are 4 outliers in s_width

# Treating outliers: Remove the 4 outliers from iris data
iris = iris[((iris < (q1-(1.5*iqr)))|(iris > (q3+(1.5*iqr))))['s_width']==False]
print("Descriptive Statistic:")
print(iris.describe())
iris["variety"].value_counts()  
# aquí se observa que los ouliers corresponden 3 a Setosa y 1 a Versicolor

vari = pd.DataFrame({'variety': iris.variety})   # We recover the original variety
vari['variety_num'] = vari['variety'].apply(set_value, args =(variety_dict, )) 
   
dat_en = dict()
dat_en['vari'] = vari
dat_en['x'] = iris.drop('variety', axis=1)
 
Result2 = pd.DataFrame([clus_agglome(dat_en, 'ward', order1),
                       clus_agglome(dat_en, 'complete', order2),
                       clus_agglome(dat_en, 'single', order1)
                      ])
Result2.rename(index={0:'Ward Linkage',1:'Complete Linkage',2:'Single Linkage'}, inplace=True)
  
print ("Success ratio and cophenetic correlation without outliers:")
print(Result2)
