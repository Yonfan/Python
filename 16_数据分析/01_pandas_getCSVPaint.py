# -*- coding: utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

df1 = pd.read_excel('./dataDir/学生成绩.xlsx', sheetname='一班')
df1.columns = ['学号', '一班']

df2 = pd.read_excel('./dataDir/学生成绩.xlsx', sheetname='二班')
df2.columns = ['学号', '二班']

df = pd.merge(df1, df2, on='学号')

print(df)

myfont = fm.FontProperties(fname=r'E:\python\98_ttf\STKAITI.TTF')

# 柱状图
df.plot(x='学号', kind='bar')
plt.xlabel('学号', fontproperties='stkaiti')
plt.legend(prop=myfont)

# 热力图
plt.figure()
sns.heatmap(df[['一班', '二班']], yticklabels=list(range(1, len(df)+1)))
plt.xticks(fontproperties='STKAITI')

# 显示图形
plt.show()

