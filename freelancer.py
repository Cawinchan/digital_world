import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('table_1.csv')
print(df.columns)
#df.columns = ['id','0','1']



m, c = np.polyfit(df['0'], df['1'], 1)

plt.scatter(df['0'], df['1'], alpha=0.5)

plt.plot(df['0'], m*df['0'] + c)

for i, txt in enumerate(list(df.index.values)):
    plt.annotate(txt, (df['0'][i], df['1'][i]))

plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

df['2'] = df['1'] - ((m*df['0']) + c)

df.sort_values(by=['2'], ascending=False,inplace=True)
print(df)

high_score = df.loc[df['2'] >= 0]
low_score = df.loc[df['2'] < 0]

print('hs',high_score)
print('ls',low_score)

a = low_score['0'].sum()
b = low_score['1'].sum()
c = high_score['0'].sum()
d = high_score['1'].sum()

print(low_score['0'].sum(),low_score['1'].sum(),high_score['0'].sum(),high_score['1'].sum())

print(a/(a+c), b/(b+d), c/(a+c), d/(b+d))


#
#
# df['score'] = (df['1']/ df['0']) *10**2
#
# plt.scatter(list(df.index.values),df['score'], alpha=0.5)
#
# m, b = np.polyfit(list(df.index.values), df['score'], 1)
#
# plt.scatter(list(df.index.values), df['score'], alpha=0.5)
#
# plt.plot(list(df.index.values), m*df['score'] + b)
#
# plt.show()
#
#
#
#
# df.sort_values(by=['score'], ascending=False,inplace=True)
# print(len(df))
# high_score = df[0:math.ceil(len(df))]
# low_score = df[math.ceil(len(df)):-1]
# print(high_score)
#
# a = low_score['0'].sum()
# b = low_score['1'].sum()
# c = high_score['0'].sum()
# d = high_score['1'].sum()

