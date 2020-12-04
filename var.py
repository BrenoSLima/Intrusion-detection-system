#---Modules---
import pandas as pd
import matplotlib.pyplot as plt


# Reading the data
no_attack = pd.read_csv('Desktop/Python/ids/trafego_sem_ataque.csv')
attack = pd.read_csv('Desktop/Python/ids/trafego_ataque.csv')

# Plotting data
boxplot = sns.boxplot(data=attack)

fig, axs = plt.subplots(2, sharey=True, figsize=(8, 6))

axs[0].set_title('No attack')
axs[0].plot(no_attack['bytes'], label="bytes")
axs[0].plot(no_attack['pacotes'], label='pacotes')
axs[0].legend()

axs[1].set_title('attack')
axs[1].plot(attack['bytes'], label="bytes")
axs[1].plot(attack['pacotes'], label='pacotes')
axs[1].legend()
plt.plot()

# Starting the challenge
q1 = no_attack['bytes'].quantile(q=0.25)
q2 = no_attack['bytes'].quantile(q=0.50)
q3 = no_attack['bytes'].quantile(q=0.75)
amp = q3 - q1

quart_noattack = q3 + 1.5 * amp
ids_index = [i for i, (j, k) in enumerate(zip(attack['bytes'], no_attack['bytes'])) if j > quart_noattack]

fig, axs = plt.subplots(figsize=(8, 6))
axs.set_title('Detecção DDoS')

axs.annotate('Começo', 
            xy=(ids_index[0] * 0.95, attack['bytes'][ids_index[0]] * 1.05),                                           
            xytext=(ids_index[0] - 30000, attack['bytes'][ids_index[-1]] + 70000),                                    
            arrowprops=dict(facecolor='black', headwidth=9, width=3, headlength=13), 
            fontsize=20)

axs.annotate('Término', 
            xy=(ids_index[-1] * 1.05, attack['bytes'][ids_index[-1]] * 1.05),                                           
            xytext=(ids_index[-1] + 10000, attack['bytes'][ids_index[-1]] + 70000),                                    
            arrowprops=dict(facecolor='black', headwidth=9, width=3, headlength=13), 
            fontsize=20)

axs.plot(attack['bytes'], '--b', label="DDoS")
axs.plot(ids_index, attack['bytes'][ids_index], c='r', label="DDoS")
axs.legend()

print(f"""
Hora que começou: {(ids_index[0] / 60) / 60:.2f} Horas a partir das meia noite
Hora que Terminou: {(ids_index[-1] / 60) / 60:.2f} Horas a partir das meia noite""")