# ecommerce-data-pipeline
A Python-based data engineering pipeline that validates, cleans, models, and visualizes e-commerce transaction data using Pandas, OOP, and Plotly.

# 🛒 E-Commerce Data Analysis Pipeline

A complete Python-based data engineering and analysis pipeline designed to process raw e-commerce transaction logs. This project demonstrates a full workflow: from data validation and cleaning to object-oriented modeling, statistical analysis, and interactive visualization.

## 📂 Project Structure

```text
ecommerce-project/
├── data_validator.py              # Phase 1: Validates raw data integrity
├── data_handler.py                # Phase 2: Cleans and processes raw text files
├── ecommerce_model.py             # Phase 3: OOP modeling (Orders & Customers)
├── data_analyzer.py               # Phase 4: Pandas & NumPy analysis
├── visualization_report.py        # Phase 5: Generates static & interactive charts
├── raw_transactions.txt           # Input: Raw messy data
├── 9. Sales-Data-Analysis.csv     # Input: Raw dataset 
├── processed_data.txt             # Output: Cleaned data from Phase 2
├── analyzed_sales.csv             # Output: Aggregated data from Phase 4
├── sales_trend.png                # Output: Visual of sales over time
├── correlation_matrix.png         # Output: Heatmap of financial metrics
└── interactive_scatter.html       # Output: Interactive Plotly visualization

🚀 Features & Workflow
Phase 1: Data Validation (data_validator.py)
Goal: Ensure input data follows correct formats before processing.

Key Tech: Regular Expressions (re), File I/O.

Functionality: detect invalid emails, missing order IDs, or corrupt lines.

Phase 2: Data Cleaning (data_handler.py)
Goal: Convert messy raw logs into structured text.

Key Tech: String manipulation, Exception Handling.

Functionality: Standardizes dates, removes whitespace, and formats currency.

Phase 3: Object-Oriented Modeling (ecommerce_model.py)
Goal: Represent business logic using Python Classes.

Key Tech: OOP (Inheritance, Encapsulation).

Functionality: Creates Order and Customer objects to manage transaction data programmatically.

Phase 4: Statistical Analysis (data_analyzer.py)
**Goal:**derive insights using Data Science libraries.

Key Tech: pandas, numpy.

Functionality:

Vectorized calculations for Revenue and Profit.

Handling missing data (imputation).

Merging currency conversion rates by City.

Aggregating sales by Month and City.

Phase 5: Visualization (visualization_report.py)
Goal: Present findings through professional charts.

Key Tech: matplotlib, seaborn, plotly.

Outputs:

📈 Sales Trend: Line chart of revenue over time.

🔥 Correlation Matrix: Heatmap showing relationships between Price, Quantity, and Profit.

🌍 Interactive Scatter: A dynamic Plotly HTML file to explore Profit vs. Revenue by City.

🛠️ Installation & Requirements
Ensure you have Python installed. Install the required libraries using pip:

Bash
pip install pandas numpy matplotlib seaborn plotly
🏃‍♂️ How to Run
Execute the scripts in the following order to simulate the full pipeline:

Clean the Data:

Bash
python data_handler.py
Analyze the Data:

Bash
python data_analyzer.py
Generate Visualizations:

Bash
python visualization_report.py
📊 Results Preview
After running the pipeline, you will find:

analyzed_sales.csv: The final dataset used for reporting.

interactive_scatter.html: Open this file in any web browser to interact with the sales data.

Created as part of the E-Commerce Python Engineering Sprint.
