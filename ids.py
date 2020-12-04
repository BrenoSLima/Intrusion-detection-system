#---Modules---
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#---Model---
from sklearn import svm
from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

#---Tools---
from sklearn.preprocessing import MinMaxScaler
from matplotlib import cm


# Reading the data
no_attack = pd.read_csv('Desktop/Python/ids/trafego_sem_ataque.csv')
attack = pd.read_csv('Desktop/Python/ids/trafego_ataque.csv')

# Plotting data
fig, axs = plt.subplots(2, sharex=True, sharey=True, figsize=(8, 6))

axs[0].set_title('No attack')
axs[0].plot(no_attack['bytes'], label="bytes")
axs[0].plot(no_attack['pacotes'], label='pacotes')
axs[0].legend()

axs[1].set_title('attack')
axs[1].plot(attack['bytes'], label="bytes")
axs[1].plot(attack['pacotes'], label='pacotes')
axs[1].legend()

fig, axs = plt.subplots(2, sharex=True, sharey=True, figsize=(8, 6))

axs[0].set_title('No attack')
axs[0].scatter(no_attack['bytes'], no_attack['pacotes'])

axs[1].set_title('attack')
axs[1].scatter(attack['bytes'], attack['pacotes'])

# Pre-processing
scaler = MinMaxScaler()
attack = pd.DataFrame(scaler.fit_transform(attack), columns = attack.columns)
no_attack = pd.DataFrame(scaler.fit_transform(no_attack), columns = attack.columns)


# Starting the challenge
#---------------------------------------------------------------------------------------

#outlier_detection = DBSCAN()
#clusters = outlier_detection.fit_predict(attack)
#cmap = cm.get_cmap('Set1')
#attack.plot.scatter(x='bytes',y='pacotes', c=clusters, cmap=cmap, colorbar = False)

#---------------------------------------------------------------------------------------

clf = LocalOutlierFactor(n_neighbors=30)
pred = clf.fit_predict(attack)
not_anomalies = attack[pred==1]
anomalies = attack[pred==-1]

fig, axs = plt.subplots()

axs.set_title('Attack?')
axs.plot(not_anomalies['bytes'], label="bytes", c = 'b') 
axs.plot(anomalies['pacotes'], label='pacotes', c = 'r')
axs.legend()

#---------------------------------------------------------------------------------------

clf = svm.OneClassSVM(nu=.2, kernel='rbf', gamma=.1)
clf.fit(attack)
pred=clf.predict(no_attack)

not_anomalies = attack[pred==1]
anomalies = attack[pred==-1]

fig, axs = plt.subplots()

axs.set_title('Attack?')
axs.plot(not_anomalies['bytes'], label="bytes", c = 'b')
axs.plot(anomalies['pacotes'], label='pacotes', c = 'r')
axs.legend()
