import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_path = "data/commodity_prices.csv"
df = pd.read_csv(data_path)

# Group data by commodity
commodities = df["Commodity"].unique()

# Plot trends for each commodity
plt.figure(figsize=(12, 6))
for commodity in commodities:
    subset = df[df["Commodity"] == commodity]
    plt.plot(
        subset["Month"] + " " + subset["Year"].astype(str),
        subset["Price (USD/ton)"],
        marker="o",
        label=commodity,
    )

# Add labels and legend
plt.title("Agricultural Commodity Prices (2020-2021)", fontsize=16)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Price (USD/ton)", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Commodity", fontsize=10)
plt.tight_layout()

# Save the plot
output_path = "commodity_price_trends.png"
plt.savefig(output_path)
print(f"Plot saved as {output_path}")
plt.show()
