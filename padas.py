import pandas as pd
import matplotlib.pyplot as plt

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
	(12, 4.25)
]


df = pd.DataFrame(prices, columns=['miesiac','priceUSD'])
df = df.set_index("miesiac")


miesiac = list(map(lambda tup:tup[0], prices))
wartosc = list(map(lambda tup:tup[1], prices))


plt.plot(wartosc ,'r1:', color='red')