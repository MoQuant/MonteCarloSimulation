import numpy as np
import random as rd
import matplotlib.pyplot as plt

def dWT():
    return rd.randint(-10,10)/100

def MC(S, r, q, iv, dt):
    return (r - q)*S*dt + iv*S*dWT()

S = 519.28
K = 524.28
r = 0.0548
q = 0.00307
iv = 0.167182
t = 100.22/365.0

trinomial_price = 16.64

N = 60
dt = t/N

simulations = 3000

fig = plt.figure()
ax = fig.add_subplot(111)

payoff = 0
for sim in range(1, simulations+1):
    S0 = S
    X = []
    Y = []
    for i in range(1, N+1):
        X.append(i)
        Y.append(S0)
        S0 += MC(S0, r, q, iv, dt)
    payoff += np.max([S0 - K, 0.0])
    option_price = np.exp(-r*t)*(payoff/sim)

    ax.set_title(f'Option Price: {round(option_price, 2)} | Error: {round(abs(trinomial_price - option_price),2)} | Steps Left: {simulations - sim}')
    ax.plot(X, Y, color='blue', linewidth=0.3)
    plt.pause(0.1)

plt.show()

