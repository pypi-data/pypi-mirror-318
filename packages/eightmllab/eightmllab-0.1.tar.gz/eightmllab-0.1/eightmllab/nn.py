import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

dataset = load_iris()
X = pd.DataFrame(dataset.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
y = dataset.target

colormap = np.array(['red', 'lime', 'black'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3).fit(X)
gmm = GaussianMixture(n_components=3).fit(X_scaled)

plt.figure(figsize=(14, 7))

plt.subplot(1, 3, 1)
plt.scatter(X['Petal_Length'], X['Petal_Width'], c=colormap[y], s=40)
plt.title('Real')

plt.subplot(1, 3, 2)
plt.scatter(X['Petal_Length'], X['Petal_Width'], c=colormap[kmeans.labels_], s=40)
plt.title('KMeans')

plt.subplot(1, 3, 3)
plt.scatter(X['Petal_Length'], X['Petal_Width'], c=colormap[gmm.predict(X_scaled)], s=40)
plt.title('GMM Classification')

plt.show()
