import matplotlib.pyplot as plt
import numpy as np
import math



def fresnel(theta, n1, n2):
    theta = theta * np.pi / 180
    xTheta = np.cos(theta)
    mid = np.sqrt(1 - (n1 / n2 * np.sin(theta)) ** 2)  # 中间变量
    rp = (n2 * xTheta - n1 * mid) / (n2 * xTheta + n1 * mid)  # p分量振幅反射率
    rs = (n1 * xTheta - n2 * mid) / (n1 * xTheta + n2 * mid)
    tp = 2 * n1 * xTheta / (n2 * xTheta + n1 * mid)
    ts = 2 * n1 * xTheta / (n1 * xTheta + n2 * mid)
    return rp, rs, tp, ts


def testFres(n1, n2):
    if (n1 > n2):
        theta = np.arange(0, math.asin(n2 / n1)*180/math.pi, 0.001)
        theta1 = np.arange(math.asin(n2 / n1)*180/math.pi,90, 0.001)
        theta2 = np.arange(0, 90, 0.1)
    else:
        theta = np.arange(0, 90, 0.1) + 0j
    a = theta * np.pi / 180
    rp, rs, tp, ts = fresnel(theta, n1, n2)
    Rp = np.abs(rp) ** 2
    Rs = np.abs(rs) ** 2
    Rn = (Rp + Rs) / 2
    Tp = n2 * np.sqrt(1 - (n1 / n2 * np.sin(a)) ** 2) / (n1 * np.cos(a)) * np.abs(tp) ** 2
    Ts = n2 * np.sqrt(1 - (n1 / n2 * np.sin(a)) ** 2) / (n1 * np.cos(a)) * np.abs(ts) ** 2
    Tn = (Tp + Ts) / 2

    ax1 = plt.subplot(122)
    ax1.plot(theta, Rp, '-', label='R_p')
    ax1.plot(theta, Rs, '-.', label='R_s')
    ax1.plot(theta, Rn, '-', label='R_n')
    ax1.plot(theta, Tp, '-', label='T_p')
    ax1.plot(theta, Ts, '-.', label='T_s')
    ax1.plot(theta, Tn, '--', label='T_n')

    ax2 = plt.subplot(121)
    if (n1 > n2) :
        y1 = [1 for i in theta1]
        ax2.plot(theta1, y1, '-', label='rp')
        ax2.plot(theta, rp,'-')
    else :
        ax2.plot(theta, rp, '-', label='rp')
    ax2.plot(theta, rs, '-.', label='rs')
    ax2.plot(theta, tp, '-', label='tp')
    ax2.plot(theta, ts, '-.', label='ts')
    ax2.set_xlabel('theta')
    ax1.set_xlabel('theta')
    ax1.set_title('R,T')
    ax2.set_title('r,t')
    ax1.legend()
    ax2.legend()
    plt.show()



testFres(1, 1.3)