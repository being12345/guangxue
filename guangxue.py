import matplotlib.pyplot as plt
import numpy as np


def fresnel(theta, n1, n2):
    theta = theta * np.pi / 180
    xTheta = np.cos(theta)
    mid = np.sqrt(1 - (n1 / n2 * np.sin(theta)) ** 2)  # 中间变量
    rp = (n2 * xTheta - n1 * mid) / (n2 * xTheta + n1 * mid)  # p分量振幅反射率
    rs = (n1 * xTheta - n2 * mid) / (n1 * xTheta + n2 * mid)
    tp = 2 * n1 * xTheta / (n2 * xTheta + n1 * mid)
    ts = 2 * n1 * xTheta / (n1 * xTheta + n2 * mid)
    return rp, rs, tp, ts


def testFres(n1=1, n2=2):
    theta = np.arange(0, 90, 0.1) + 0j
    a = theta * np.pi / 180
    rp, rs, tp, ts = fresnel(theta, n1, n2)
    Rp = np.abs(rp) ** 2
    Rs = np.abs(rs) ** 2
    Rn = (Rp + Rs) / 2
    Tp = n2 * np.sqrt(1 - (n1 / n2 * np.sin(a)) ** 2) / (n1 * np.cos(a)) * np.abs(tp) ** 2
    Ts = n2 * np.sqrt(1 - (n1 / n2 * np.sin(a)) ** 2) / (n1 * np.cos(a)) * np.abs(ts) ** 2
    Tn = (Tp + Ts) / 2

    plt.subplot(1, 1, 1)
    plt.plot(theta, Rp, '-', label='R_p')
    plt.plot(theta, Rs, '-.', label='R_s')
    plt.plot(theta, Rn, '-', label='R_n')
    plt.plot(theta, Tp, '-', label='T_p')
    plt.plot(theta, Ts, '-.', label='T_s')
    plt.plot(theta, Tn, '--', label='T_n')
    plt.xlabel("theta")

    plt.legend()
    plt.show()

    fig = plt.figure(1)
    plt.subplot(1, 1, 1)
    plt.plot(theta, rp, '-', label='rp')
    plt.plot(theta, rs, '-.', label='rs')
    plt.plot(theta, tp, '-', label='tp')
    plt.plot(theta, ts, '-.', label='ts')
    plt.xlabel("theta")
    plt.legend()
    plt.show()




# while (1):
#     n1 = float(input("输入n1的值:\n"))
#     n2 = float(input("输入n2的值:\n"))
#     if (n1 == -1 or n2 == -1):
#         break
testFres()



