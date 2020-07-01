import numpy as np
import u1 as use
import pandas as pd
from sklearn.neighbors import kde

l = list()
# l1 = list()
for i in range(1,21):
    # 连续数据提取
    nyse2 = pd.read_excel("relative_psd.xlsx", usecols=[i])
    a = use.dTl(nyse2)
    # 分母提取
    # fenmu = 0
    ny = pd.read_excel("reP.xlsx", usecols=[i])
    nyy = ny.values
    nn = use.dTl(ny)
    fenmu = nn * len(nn)
    l2 = list()
    for j in range(21,22):
        # 标签数据提取
        nyse1 = pd.read_excel("relative_psd.xlsx", usecols=[j])
        d = use.dTl(nyse1)
        dd = np.round(d, 1)  # 标签离散化
        h = use.condition_HXD(dd, a, fenmu)
        print(i, " re&lab ", j, " c_h:", h)
        l2.append(h)
    l.append(l2)
wb = use.format_excel("r&l_h", np.array(l))
wb.save("re$lab_condition_h.xlsx")




l = list()
# l1 = list()
for i in range(1,8):
    # 标签数据提取
    nyse1 = pd.read_excel("ab.xlsx", usecols=[i])
    d = use.dTl(nyse1)
    dd = np.round(d, 2)  # 标签离散化
    l2 = list()
    for j in range(1,3):
        # 连续数据提取
        nyse2 = pd.read_excel("re.xlsx", usecols=[j])
        a = use.dTl(nyse2)
        # 分母提取
        # fenmu = 0
        ny = pd.read_excel("log_rep.xlsx", usecols=[j])
        nyy = ny.values
        nn = use.dTl(ny)
        fenmu = np.exp(nn) * len(nn)

        print("szfenmu: ",len(fenmu))
        h = use.condition_HXD(dd, a, fenmu)
        print(i, " re&ab ", j, " c_h:", h)
        l2.append(h)
        # l2.append(h)
        # print("l",l)
        # print("l2",l2)
    l.append(l2)
    # print("l1",l1)
# wb = use.format_excel("ra",np.array(l))
# wb.save("eeee.xlsx")
pd.DataFrame(l).to_excel("testre$ab_condition_h.xlsx")






# 0 fenzi 9991819159.158573
# 1 fenzi 1717206096.4330335
# 2 fenzi 2832637551.9952707
# 3 fenzi 1674158319.0540047
# 4 fenzi 712228796.6522425