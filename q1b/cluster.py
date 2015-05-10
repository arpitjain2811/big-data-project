#!/usr/bin/python
import pandas as pd
import sys
from collections import defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans

print "Reading file..."
train = pd.read_csv(sys.argv[1],header=0, delimiter="\t",quoting=3)
vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000)
X = vectorizer.fit_transform(train["hoods"])
km = KMeans(init='k-means++', max_iter=10000, n_clusters=5000, verbose=1)
print "Training Kmeans"
km.fit(X)
k=0
y = km.predict(X)
H = defaultdict(list)
for i in y:
	H[i].append(k)
	k += 1
for keys in H.keys():
	print ",".join(str(H[keys]))