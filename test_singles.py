import os
import platform
from copy import copy

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.optimize import curve_fit


def exp1(x, a, b, c):
    """Compute the exponential function f(x) = a*exp(b*x) + c for input array x."""
    return a * np.exp(b * x) + c


def calibrate_energy(x):
    """Convert energy from samples to keV using known calibration points and an exponential fitting function."""
    px = np.array([0.0, 150, 173, 207])  # samples
    py = np.array([0.0, 334, 511, 1274])  # keV (344 keV compton edge)

    fit1, cov1 = curve_fit(exp1, px, py, p0=(7.0, 0.03, 0.0))
    # xspan = np.linspace(px.min(), px.max())
    # plt.plot(px, py, '.')
    # plt.plot(xspan, exp1(xspan, *fit1))

    label = "{:.3g} * exp({:.3g} * x) + {:.3g}".format(*tuple(fit1))
    return exp1(x, *fit1).clip(max=2000), label


def test_singles(file="my_data_singles.txt"):
    """Tests single events data from a file, calibrates energy, identifies 511 keV candidates, and generates diagnostic
    plots.
    """
    x = np.loadtxt(file)
    t, e, ch = x.transpose()  # time (ps), energy (samples), channel
    print(f"Read {file}, {x.shape[0]:g} events recorded over {(t.max() - t.min()) / 1e12:g}s")

    # calibrate energy
    e0 = copy(e)
    x[:, 1], efit_label = calibrate_energy(e)  # keV
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
    dt = dt[(np.abs(dt) < maxdt) & (np.diff(ch) != 0)]

    # Plots
    plots(x, e0, ecal, dt, efit_label)


def plots(x, e0, ecal, dt, efit_label):
    """Generate and save various matplotlib and seaborn plots for given energy and time data arrays."""
    # fig, ax = plt.subplots(2, 3, figsize=(9, 6))
    # ax = ax.ravel()
    # ax[0].hist(e0, np.linspace(0, 300, 300))
    # ax[0].set_xlabel('energy (samples)')
    # ax[1].hist(ecal, np.linspace(0, 2000, 300))
    # ax[1].set_xlabel('energy (keV)')
    # ax[2].hist(dt, np.linspace(-400, 600, 50))
    # ax[2].set_xlabel('t (ps)')
    # fig.tight_layout()
    # # for i in range(3):
    # #     ax[i].grid()
    # fig.savefig('results.png', dpi=200)

    # seaborn correlogram
    # import pandas as pd
    # x = pd.DataFrame(x, columns=['time (ps)', 'E (samples)', 'dt'])
    # sns.pairplot(x, corner=True, diag_kind='hist', kind='scatter', markers='o',
    #              plot_kws=dict(s=3, edgecolor=None, linewidth=1, alpha=0.02),
    #              diag_kws=dict(bins=50))
    # plt.savefig('data_correlogram.png', dpi=200)
    # plt.close()

    # seaborn plots
    fig, ax = plt.subplots(1, 3, figsize=(12, 4))
    ax = ax.ravel()
    sns.distplot(e0, np.linspace(0, 300, 300), kde=False, axlabel="energy (samples)", ax=ax[0])
    sns.distplot(ecal, np.linspace(0, 1500, 300), kde=False, axlabel="energy (keV)", ax=ax[1])
    a = sns.distplot(
        dt,
        np.linspace(-400, 600, 50),
        kde=False,
        fit=stats.norm,
        axlabel="time (ps)",
        label="Normal fit $\mu=${:.1f}, $\sigma=${:.2f}".format(*stats.norm.fit(dt)),
        ax=ax[2],
    )
    a.legend()
    fig.tight_layout()
    fig.savefig("time_resolution.png", dpi=200)

    # seaborn energy calibration jointplot
    import pandas as pd

    x = pd.DataFrame(np.stack((e0, ecal)).transpose(), columns=["energy (samples)", "energy (keV)"])
    a = sns.jointplot(
        data=x,
        x="energy (samples)",
        y="energy (keV)",
        xlim=[0, 300],
        ylim=[0, 1500],
        joint_kws=dict(gridsize=50),
        ratio=2,
        kind="hex",
        marginal_kws=dict(bins=500),
    )
    a.ax_joint.text(10, 1400, efit_label)
    plt.savefig("energy_calibration.png", dpi=200)

    # Display to screen
    if platform.system() == "Darwin":  # MacOS
        os.system("open energy_calibration.png")


if __name__ == "__main__":
    test_singles()
