import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv("test.csv")

set_sample = a.sample(1000, replace=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax2.boxplot(set_sample['Square'])
ax2.set_title('Ящик с усами')
ax2.set_ylabel('Значение')

ax1.hist(set_sample['Square'], bins=30, log=True)
ax1.set_title('Логарифмическая гистограмма')
ax1.set_xlabel('Значение')
ax1.set_ylabel('Частота (логарифмическая шкала)')

plt.show()