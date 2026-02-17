# 🛒 E-Commerce Data Engineering & Analytics Pipeline

A structured Python-based data pipeline that validates, cleans, models,
analyzes, and visualizes e-commerce transaction data.

This project demonstrates a full end-to-end workflow --- from raw
transaction logs to business-ready insights --- using **Pandas, NumPy,
OOP principles, and Plotly**.

------------------------------------------------------------------------

## 📌 Overview

Raw e-commerce data is rarely clean. This pipeline simulates a
real-world scenario where transaction logs must be:

1.  Validated
2.  Cleaned
3.  Modeled
4.  Analyzed
5.  Visualized

Each phase is modular and executable independently, following clean
architecture principles.

------------------------------------------------------------------------

## 🗂️ Project Structure

``` text
ecommerce-project/
│
├── data_validator.py          # Phase 1 → Validates raw data integrity
├── data_handler.py            # Phase 2 → Cleans and structures raw logs
├── ecommerce_model.py         # Phase 3 → OOP modeling (Orders & Customers)
├── data_analyzer.py           # Phase 4 → Data analysis with Pandas & NumPy
├── visualization_report.py    # Phase 5 → Static & interactive visualizations
│
├── raw_transactions.txt       # Input: Unstructured transaction logs
├── 9. Sales-Data-Analysis.csv # Input: Raw dataset
│
├── processed_data.txt         # Output: Cleaned structured data
├── analyzed_sales.csv         # Output: Aggregated dataset
│
├── sales_trend.png            # Output: Revenue trend visualization
├── correlation_matrix.png     # Output: Feature correlation heatmap
└── interactive_scatter.html   # Output: Interactive Plotly dashboard
```

------------------------------------------------------------------------

# ⚙️ Pipeline Workflow

## Phase 1 --- Data Validation (`data_validator.py`)

**Objective:** Ensure data integrity before processing.

**Technologies:**\
- `re` (Regular Expressions)\
- File I/O

**Responsibilities:** - Detect invalid emails\
- Identify missing order IDs\
- Flag corrupted or malformed rows

------------------------------------------------------------------------

## Phase 2 --- Data Cleaning (`data_handler.py`)

**Objective:** Convert messy raw logs into structured, analysis-ready
data.

**Technologies:**\
- String manipulation\
- Exception handling

**Responsibilities:** - Standardize date formats\
- Remove unnecessary whitespace\
- Normalize currency formatting\
- Output cleaned dataset

------------------------------------------------------------------------

## Phase 3 --- Object-Oriented Modeling (`ecommerce_model.py`)

**Objective:** Represent business logic using Python classes.

**Concepts Applied:**\
- Encapsulation\
- Inheritance\
- Structured domain modeling

**Responsibilities:** - Create `Order` objects\
- Create `Customer` objects\
- Enable programmatic transaction handling

------------------------------------------------------------------------

## Phase 4 --- Statistical Analysis (`data_analyzer.py`)

**Objective:** Extract business insights using data science libraries.

**Technologies:**\
- `pandas`\
- `numpy`

**Responsibilities:** - Revenue & Profit calculations\
- Missing data handling (imputation)\
- Currency rate merging by city\
- Aggregated sales by Month & City\
- Data export for reporting

------------------------------------------------------------------------

## Phase 5 --- Visualization (`visualization_report.py`)

**Objective:** Present insights visually for business interpretation.

**Technologies:**\
- `matplotlib`\
- `seaborn`\
- `plotly`

### Outputs:

-   📈 **Sales Trend** --- Revenue over time\
-   🔥 **Correlation Matrix** --- Relationships between Price, Quantity
    & Profit\
-   🌍 **Interactive Scatter Plot** --- Profit vs Revenue by City

------------------------------------------------------------------------

# 🛠️ Installation

Make sure Python 3.9+ is installed.

Install dependencies:

``` bash
pip install pandas numpy matplotlib seaborn plotly
```

------------------------------------------------------------------------

# ▶️ How to Run

Execute scripts in order to simulate the complete pipeline:

### 1️⃣ Clean the Data

``` bash
python data_handler.py
```

### 2️⃣ Analyze the Data

``` bash
python data_analyzer.py
```

### 3️⃣ Generate Visualizations

``` bash
python visualization_report.py
```

------------------------------------------------------------------------

# 📊 Output

After execution, the pipeline produces:

-   `analyzed_sales.csv` → Final structured dataset\
-   `sales_trend.png` → Revenue time-series visualization\
-   `correlation_matrix.png` → Feature relationship heatmap\
-   `interactive_scatter.html` → Interactive business dashboard

Open the HTML file in any browser to explore the interactive
visualization.

------------------------------------------------------------------------

# 🎯 Key Skills Demonstrated

-   Data validation & integrity checks\
-   Data cleaning & preprocessing\
-   Object-Oriented Design\
-   Vectorized numerical analysis\
-   Business KPI modeling\
-   Data visualization (static & interactive)\
-   Modular pipeline architecture

------------------------------------------------------------------------

# 📌 Project Context

Built as part of an E-Commerce Python Engineering Sprint to simulate
real-world data engineering and analytics workflows.
