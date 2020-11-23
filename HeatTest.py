# 상관계수에 따른 heatmap 그리기

import pandas as pand
import matplotlib.pyplot as matlib
import seaborn as sns
from matplotlib import font_manager, rc
import numpy

font_name = font_manager.FontProperties(
    fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# df = pand.read_csv('c:/seoul_bigdata/category_perStore_02.csv', delimiter=',')
df = pand.read_csv('c:/seoul_bigdata/category_category.csv', delimiter=',')

print(len(df.columns))
print(df.shape)

# 18열 부터 32열까지 df로 생성
# 의류점과 패션잡화에 na값이 있는 행을 제거
df = df.iloc[:, numpy.r_[18, 32]]
df = df[df.의류점 != 0]
df = df[df.패션잡화 != 0]

print(len(df))

print(df.head(30))

matlib.figure(figsize=(15, 15))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5,
            cmap=matlib.cm.gist_heat, linecolor='white', annot=True)
matlib.show()
