import pandas as pd
import numpy as np

def analyze_sales_data(input_file, output_file):
    
    print("Loading Data")
    
    try:
        df = pd.read_csv(input_file)
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
        
        print(f"Data has been successfully loaded with {df.shape[0]} rows and {df.shape[1]} columns")
        
    except FileNotFoundError:
        print("The file was not found")
        return

    # Create (Amount) Column using vectorized operation
    df['Amount'] = df['Price'] * df['Quantity']

    # Setting 5% of (Amount) column to NaN randomly 
    rows_to_modify = int(len(df) * 0.05)
    nan_indices = np.random.choice(df.index, rows_to_modify, replace=False)
    df.loc[nan_indices, 'Amount'] = np.nan
    
    print(f"Number of NaN rows created in Amoun column is {rows_to_modify}")
    
    # Handle missing values
    amount_mean = df['Amount'].mean()
    df['Amount'] = df['Amount'].fillna(amount_mean)
    print(f"Filled the {rows_to_modify} missing rows with the average amount: ${amount_mean:.2f}")

    # Calculate Profit Margin (15% of Amount)
    df['Profit_Margin'] = df['Amount'] * 0.15

    # Conversion rate per city
    conversion_data = {
        'City': ['London', 'Lisbon', 'Madrid', 'Berlin', 'Paris'], 
        'Conversion_Factor': [0.85, 0.95, 1.10, 1.05, 0.98] 
    }
    conversion_df = pd.DataFrame(conversion_data)
    
    # Mergeing on City column
    df = pd.merge(df, conversion_df, on='City', how='left')
    
    # Calculate USD Amount
    df['USD_Amount'] = df['Amount'] * df['Conversion_Factor']

    # Using Aggregations for Reporting
    print("\n Sales by City")
    city_sales = df.groupby('City')['Amount'].sum()
    print(city_sales)

    print("\n Average Profit Margin per Month")
    monthly_profit = df.set_index('Date').resample('ME')['Profit_Margin'].mean()
    print(monthly_profit)

    # Saving Final Data
    df.to_csv(output_file, index=False)
    print(f"\n Analysis complete. Processed data saved to '{output_file}'")

if __name__ == "__main__":
    analyze_sales_data('9. Sales-Data-Analysis.csv', 'analyzed_sales.csv')