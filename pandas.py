import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

pd.__version__

prices = [
	(1, 2.12),
	(2, 2.56),
	(3, 3.10),
	(4, 3.16),
	(5, 3.58),
	(6, 5.12),
	(7, 5.16),
	(8, 5.20),
	(9, 4.12),
	(10, 4.10),
	(11, 3.65),
	(12, 4.25),

]
df = pd.DataFrame(prices)
print(df)

df = pd.DataFrame(prices, columns=["month", "price"])
df = df.set_index("month")
print(df)

kurs = 4
price_USD = df['price'].apply(lambda price: price/kurs)
df["price"] = price_USD
print(df)

plt.plot(df.index, df["price"])

plt.plot(df.index, df["price"])
fig, ax = plt.subplots(figsize=(10,8))
res = ax.plot(df.index, df["price"])
line = res[0]
line.set_c('#d1371f')
line.set_linestyle('dashed')