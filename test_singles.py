import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from copy import copy


def exp1(x, a, b, c):
    # f(x) = a*exp(b*x)+c
    return a * np.exp(b * x) + c


def calibrate_energy(x):
    # convert energy from samples to keV using known calibration points px, py
    px = np.array([0., 150, 173, 207])  # samples
    py = np.array([0., 334, 511, 1274])  # keV (344 keV compton edge)

    fit1, cov1 = curve_fit(exp1, px, py, p0=(7.0, 0.03, 0.0))
    # xspan = np.linspace(px.min(), px.max())
    # plt.plot(px, py, '.')
    # plt.plot(xspan, exp1(xspan, *fit1))
    return exp1(x, *fit1).clip(max=2000)


def test_singles(file='my_data_singles.txt'):
    x = np.loadtxt(file)
    t, e, ch = x.transpose()  # time (ps), energy (samples), channel
    print('Read %s, %g events recorded over %gs' % (file, x.shape[0], (t.max() - t.min()) / 1e12))

    # calibrate energy
    e0 = copy(e)
    x[:, 1] = calibrate_energy(e)  # keV
    t, e, ch = x.transpose()  # time (ps), energy (samples), channel
    ecal = copy(e)

    # 511 keV candidates
    x = x[(e > 400) & (e < 600)]  # 400 keV < e_val < 600 keV

    # sort by time
    x = x[np.argsort(x[:, 0])]
    t, e, ch = x.transpose()  # time (ps), energy (keV), channel

    # find pairs
    maxdt = 1000  # (ps)
    dt = np.diff(t)
    a = ch[1:] == 309
    dt[a] = -dt[a]
    dt = dt[(np.abs(dt) < maxdt) & (np.diff(ch) != 0) & (dt != 0)]

    # plots
    # import pandas as pd
    # import seaborn as sns
    # x = pd.DataFrame(x, columns=['time (ps)', 'E (samples)', 'channel'])
    # sns.pairplot(x, corner=True, diag_kind='hist', kind='scatter', markers='o',
    #              plot_kws=dict(s=3, edgecolor=None, linewidth=1, alpha=0.02),
    #              diag_kws=dict(bins=50))
    # plt.savefig('data_correlogram.png', dpi=200)
    # plt.close()

    fig, ax = plt.subplots(2, 3, figsize=(9, 6))
    ax = ax.ravel()
    ax[0].hist(e0, np.linspace(0, 300, 300))
    ax[0].set_xlabel('energy (samples)')
    ax[1].hist(ecal, np.linspace(0, 2000, 300))
    ax[1].set_xlabel('energy (keV)')
    ax[2].hist(dt, np.linspace(-400, 600, 50))
    ax[2].set_xlabel('t (ps)')
    fig.tight_layout()
    # for i in range(3):
    #     ax[i].grid()
    fig.savefig('results.png', dpi=200)


if __name__ == '__main__':
    test_singles()
