import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load analyzed data from phase 4
df= pd.read_csv("analyzed_sales.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
print("--- Data loaded ---")

# Group by Date and sum the USD_Amount
daily_sales = df.groupby('Date')['USD_Amount'].sum().reset_index()

# Sort by Date to ensure the line plot connects points in order
daily_sales = daily_sales.sort_values('Date')

# Plotting Sales_trend 'USD_Amount' over time 
print("--- Plotting Sales over time ---")
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['Date'], daily_sales['USD_Amount'], label='Total Sales (USD)')
plt.xlabel("Date")
plt.ylabel("Sales in USD")
plt.title("Sales over time")
plt.legend()

print("--- Saving Line plot ---")
# Saving figure
plt.savefig("sales_trend.png", format= "png", dpi= 300)
plt.show()
plt.close()

print("--- Plotting heatmap for correlation matrix ---")
numerical_cols= ["Amount", "Profit_Margin", "Conversion_Factor"]
numerical_df= df[numerical_cols]
# Calculating correlation for numerical values
num_corr= numerical_df.corr()
# Plotting correlation matrix using Seaborn heatmap
sns.heatmap(num_corr, annot= True, cmap="coolwarm", linewidths= 0.5)

print("--- Saving Correlation matrix ---")
plt.savefig("correlation_matrix.png", format= "png", dpi= 300)
plt.show()
plt.close()

print("--- Interactive scatter plot ---")
# Interactive scatter plot using Plotly Express
fig = px.scatter(
    df,
    x="USD_Amount", 
    y="Profit_Margin", 
    title="USD Amount vs Profit Margin by City",
    labels={"USD_Amount": "Total Sales (USD)", "Profit_Margin": "Profit"},
    color="City",
    hover_data=["Order ID"],
    template="plotly_white"
)

fig.update_traces(marker=dict(size=12, opacity=0.8, line=dict(width=1, color='White')))
fig.update_layout(title_font_size= 26)

print("--- Saving interactive plot ---")
# Save and Show
fig.write_html("interactive_scatter.html")
fig.show()