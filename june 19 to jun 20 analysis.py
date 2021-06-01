import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel(r'01.06.19 to 01.06.20.xlsx')


df = df[df['PO Line Status'] != 'Canceled']
df['Extended Cost'] = df["Extended Cost"].str.replace("AED", "")
df['Unit Cost'] = df["Unit Cost"].str.replace("AED", "")
df['Item Description'] = df['Item Description'].str.lower()


x = input("Type to search for item : ")
x = x.lower()
words = x.split(' ')
submasks = [df['Item Description'].str.contains(s) for s in words]
combined = np.vstack(submasks).all(axis=0)
print(df[combined])

q= df[combined]

ax = plt.gca()

q.plot(kind='line',x='Document Date',y='Unit Cost', ax=ax)
q.plot(kind='line',x='Document Date',y='QTY Ordered', color='red', ax=ax)
