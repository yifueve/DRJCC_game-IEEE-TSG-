import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scenario = ['c1', 'c2', 'c3']
dayhour = 48

player_range = [2, 4, 6, 8, 10, 12, 14]
lower      = np.zeros(len(player_range))
upper      = np.zeros(len(player_range))
mean       = np.zeros(len(player_range))

lower_1      = np.zeros(len(player_range))
upper_1      = np.zeros(len(player_range))
mean_1       = np.zeros(len(player_range))

lower_2      = np.zeros(len(player_range))
upper_2      = np.zeros(len(player_range))
mean_2       = np.zeros(len(player_range))

iso_profit_1    = np.zeros(len(player_range))
iso_profit_2    = np.zeros(len(player_range))
iso_profit_3    = np.zeros(len(player_range))

player_profit_1 = np.zeros(len(player_range))
player_profit_2 = np.zeros(len(player_range))
player_profit_3 = np.zeros(len(player_range))

sys_profit_1 = np.zeros(len(player_range))
sys_profit_2 = np.zeros(len(player_range))
sys_profit_3 = np.zeros(len(player_range))

vr_1 = np.zeros(len(player_range))
vr_2 = np.zeros(len(player_range))
vr_3 = np.zeros(len(player_range))

total_energy  = np.zeros(len(player_range))
total_reserve = np.zeros(len(player_range))

avg_energy  = np.zeros(len(player_range))
avg_reserve = np.zeros(len(player_range))

#### Reserve and profits ####

result1 = np.zeros(150)
for e in range(len(player_range)):
    cost1 = pd.read_csv('profit' + str(player_range[e]) + scenario[0]+'.csv')
    cost2 = pd.read_csv('profit' + str(player_range[e]) + scenario[1]+'.csv')
    cost3 = pd.read_csv('profit' + str(player_range[e]) + scenario[2]+'.csv')

    data1 = pd.read_csv('reserve' + str(player_range[e]) + scenario[0]+'.csv')
    data2 = pd.read_csv('reserve' + str(player_range[e]) + scenario[1]+'.csv')
    data3 = pd.read_csv('reserve' + str(player_range[e]) + scenario[2]+'.csv')

    vio1 = pd.read_csv('violation' + str(player_range[e]) + scenario[0]+'.csv')
    vio2 = pd.read_csv('violation' + str(player_range[e]) + scenario[1]+'.csv')
    vio3 = pd.read_csv('violation' + str(player_range[e]) + scenario[2]+'.csv')

    res1 = pd.read_csv('optimization' + str(player_range[e]) + scenario[0]+'.csv')
    res2 = pd.read_csv('optimization' + str(player_range[e]) + scenario[1]+'.csv')
    res3 = pd.read_csv('optimization' + str(player_range[e]) + scenario[2]+'.csv')

    sum  = data1.iloc[:, 1:].sum(axis=1)
    sum1 = data2.iloc[:, 1:].sum(axis=1)
    sum2 = data3.iloc[:, 1:].sum(axis=1)

    total_reserve[e]  = np.sum(res1['reserve'])
    total_energy[e] = np.sum(res1['energy'])

    avg_reserve[e]  = np.average(res1['reserve'])
    avg_energy[e]   = np.average(res1['energy'])

    lower[e] = np.quantile(sum, 0.2)/2
    upper[e] = np.quantile(sum, 0.8)/2
    mean[e]  = np.mean(sum)/2

    lower_1[e] = np.quantile(sum1, 0.2)/2
    upper_1[e] = np.quantile(sum1, 0.8)/2
    mean_1[e]  = np.mean(sum1)/2

    lower_2[e] = np.quantile(sum2, 0.2)/2
    upper_2[e] = np.quantile(sum2, 0.8)/2
    mean_2[e]  = np.mean(sum2)/2

    iso_profit_1[e] = cost1['0'][len(cost3)-1]
    iso_profit_2[e] = cost2['0'][len(cost3)-1]
    iso_profit_3[e] = cost3['0'][len(cost3)-1]

    player_profit_1[e] = np.average(cost1['0'][0:len(cost1)-1])
    player_profit_2[e] = np.average(cost2['0'][0:len(cost2)-1])
    player_profit_3[e] = np.average(cost3['0'][0:len(cost3)-1])

    sys_profit_1[e] = np.sum(cost1['0'][0:len(cost1)])
    sys_profit_2[e] = np.sum(cost2['0'][0:len(cost2)])
    sys_profit_3[e] = np.sum(cost3['0'][0:len(cost3)])

    vr_1[e] = np.average(vio1['0'][0:len(vio1)])
    vr_2[e] = np.average(vio2['0'][0:len(vio2)])
    vr_3[e] = np.average(vio3['0'][0:len(vio3)])

    result1 = np.vstack((result1, sum))

barWidth = 0.5


plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.size'] = 15
plt.rcParams['text.color'] = 'black'


fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()
ax2.plot(player_range, player_profit_1, lw=2, color='tab:blue',  label='Avg. cost (C1)')
ax2.scatter(player_range, player_profit_1, marker='^', color='tab:blue')
# ax2.plot(player_range, player_profit_2, lw=2, color='tab:orange', label='Avg. cost (C2)')
# ax2.scatter(player_range, player_profit_2, marker='o', color='tab:orange')
# ax2.plot(player_range, player_profit_3, lw=2, color='tab:blue', label='Avg. cost (C3)')
# ax2.scatter(player_range, player_profit_3, marker='*', color='tab:blue')

ax1.plot(2, 0, lw=2, color='tab:blue',  label='Avg. cost')
#ax1.plot(2, 0,  lw=2, color='tab:orange',  label='Avg. cost (C2)')
#ax1.plot(2, 0,  lw=2, color='tab:blue', label='Avg. cost (C3)')
ax1.bar([x - 0.5* barWidth for x in player_range], avg_energy, alpha=0.6,
        color='tab:blue', width = barWidth, label='Energy offer')
ax1.bar([x + 0.5* barWidth for x in player_range], avg_reserve, alpha=0.6,
        color='tab:orange', width = barWidth, label='Reserve offer')

ax1.set_xlabel('Number of microgrids')
ax2.set_ylabel('Average cost of microgrids ($)')
ax1.set_ylabel('Average capacity of energy & reserve \noffers from microgrids (MWh)')
ax1.legend(ncol=3, loc='upper left',
           fancybox=True, shadow=True, bbox_to_anchor=(-0.05, -0.15))
plt.gca()
plt.grid(which='major', linestyle='--', axis='y')
plt.savefig('players_results_conf.png', bbox_inches='tight')

fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()
ax2.plot(player_range, iso_profit_1, lw=2, color='tab:blue', label='Avg. cost')
ax2.scatter(player_range, iso_profit_1, marker='^',  color='tab:blue')
# ax2.plot(player_range, iso_profit_2, lw=2, color='tab:orange', label='Avg. cost (C2)')
# ax2.scatter(player_range, iso_profit_2, marker='o', color='tab:orange')
# ax2.plot(player_range, iso_profit_3, lw=2, color='tab:blue', label='Avg. cost (C3)')
# ax2.scatter(player_range, iso_profit_3, marker='*', color='tab:blue')
ax2.bar(2, 0, alpha=0.6, color='tab:blue', width = barWidth, label='Energy offer')
ax2.bar(2, 0, alpha=0.6, color='tab:orange', width = barWidth, label='Reserve offer')

ax1.bar([x - 0.5* barWidth for x in player_range], total_energy, alpha=0.6,
        color='tab:blue', width = barWidth, label='Energy')
ax1.bar([x + 0.5* barWidth for x in player_range], total_reserve, alpha=0.6,
        color='tab:orange', width = barWidth, label='Reserve')

ax1.set_xlabel('Number of microgrids')
ax2.set_ylabel('Average cost of ISO ($)')
ax1.set_ylabel('Total capacity of energy & reserve \noffers (MWh)')
plt.legend(ncol=3, loc='upper left',
           fancybox=True, shadow=True, bbox_to_anchor=(-0.05, -0.15))
plt.gca()
plt.grid(which='major', linestyle='--', axis='y')
plt.savefig('iso_results_conf.png', bbox_inches='tight')


