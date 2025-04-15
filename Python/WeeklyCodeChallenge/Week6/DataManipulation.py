'''
Creates a NumPy array and calculates its mean.

Loads a small dataset into a pandas DataFrame and displays stats.

Retrieves Bitcoin price data from the CoinDesk API.

Plots a simple line graph using matplotlib.
'''

# 📌 Importing Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# 1️⃣ NumPy Array from 1 to 10 and Calculate the Mean
array = np.arange(1, 11)  # Numbers from 1 to 10
mean_value = np.mean(array)
print("NumPy Array:", array)
print("Mean of Array:", mean_value)

# 2️⃣ Load a Small Dataset into a Pandas DataFrame
# We'll use a small built-in dataset from seaborn as an example (e.g., 'titanic')
# Alternatively, create a mini dataset manually
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe(include='all'))

# 3️⃣ Fetch Data from a Public API and Print Key Information
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    bitcoin_data = response.json()
    usd_rate = bitcoin_data['bpi']['USD']['rate']
    print("\nCurrent Bitcoin Price in USD:", usd_rate)
else:
    print("\nFailed to fetch data from API")

# 4️⃣ Plot a Simple Line Graph Using Matplotlib
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
plt.plot(x, y, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
