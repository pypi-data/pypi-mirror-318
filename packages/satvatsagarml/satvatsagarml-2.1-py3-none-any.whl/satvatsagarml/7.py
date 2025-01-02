#also import 13 change file to .csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
df=pd.read_csv("13.csv")
kmeans=KMeans(n_clusters=3)
labels=kmeans.fit_predict(df)
plt.scatter(df.iloc[:,0],df.iloc[:,1],c=labels,cmap='rainbow')
plt.xlabel("feature1")
plt.ylabel("feature2")
plt.legend()
plt.show()