# Retail Analytics Portfolio Project

## Project Overview

This project analyzes Brazilian e-commerce order data to understand order fulfillment, delivery performance, and operational efficiency. It uses Python for data cleaning and ETL, MySQL for data storage and SQL analysis, and Tableau for interactive visualization.

## Business Objectives

- Analyze the distribution of e-commerce order statuses.
- Measure average delivery duration.
- Identify late deliveries and calculate the late-delivery rate.
- Prepare reusable SQL views for dashboard reporting.
- Present business metrics in a Tableau dashboard.

## Technology Stack

- **Python:** pandas, pathlib, SQLAlchemy, PyMySQL
- **Database:** MySQL 8.0
- **SQL:** Aggregations, filtering, grouping, validation, and views
- **Visualization:** Tableau
- **Dataset:** Brazilian E-Commerce Public Dataset by Olist

## Project Workflow

1. Load and inspect raw order data.
2. Convert timestamp columns into appropriate datetime types.
3. Validate order identifiers and required purchase timestamps.
4. Calculate delivery duration and delivery delay.
5. Save the cleaned dataset as a CSV file.
6. Load the processed data into MySQL.
7. Create SQL views for delivery KPIs and order-status analysis.
8. Build a Tableau dashboard to visualize the results.

## Key Results

The analysis covers 99,441 recorded orders.

| Metric | Result |
|---|---:|
| Total orders | 99,441 |
| Delivered orders | 96,478 |
| Delivered share of all orders | 97.02% |
| Average delivery duration | 12.56 days |
| Late delivered orders | 7,826 |
| Late-delivery rate | 8.11% |
| Average delivery delay | -11.18 days |

A negative average delivery delay indicates that orders arrived earlier than their estimated delivery dates on average.

## SQL Views

### `delivery_kpis`

Summarizes delivered orders, available delay records, late orders, late-delivery rate, average delivery duration, and average delay.

### `order_status_summary`

Summarizes order counts and the percentage represented by each order status.

## Project Structure

```text
retail-analytics-portfolio/
├── data/
│   ├── raw/
│   │   └── olist/
│   └── processed/
│       └── orders_clean.csv
├── notebooks/
│   └── 01_data_understanding.ipynb
├── src/
│   └── etl/
│       ├── clean_orders.py
│       └── load_orders_to_mysql.py
├── sql/
├── reports/
├── dashboard/
│   └── Retail_Analytics_Dashboard.twbx
└── README.md
```

## How to Run

### 1. Install Python dependencies

```bash
python -m pip install pandas sqlalchemy pymysql
```

### 2. Clean the orders dataset

```bash
python src/etl/clean_orders.py
```

### 3. Load the cleaned data into MySQL

Ensure MySQL Server is running and the `retail_analytics` database and `orders` table have been created.

```bash
python src/etl/load_orders_to_mysql.py
```

The loading script prompts for the MySQL password.

### 4. Explore the SQL analysis

Connect to MySQL and run:

```sql
USE retail_analytics;

SELECT * FROM delivery_kpis;

SELECT *
FROM order_status_summary
ORDER BY order_count DESC;
```

### 5. Open the Tableau dashboard

Open `dashboard/Retail_Analytics_Dashboard.twbx` in a compatible Tableau application.

## Data Quality Notes

- The source contains 99,441 order records and 99,441 unique order IDs.
- Some orders have missing approval or delivery timestamps.
- Missing delivery durations are preserved rather than treated as zero.
- Late delivery is defined as actual customer delivery occurring after the estimated delivery timestamp.
- The late-delivery rate is calculated using delivered orders as the denominator.

## Limitations

This project currently focuses on order status and delivery performance. It does not yet provide a complete sales, profit, customer, product-category, or geographic-market analysis.

## Future Improvements

- Analyze sales, payments, products, and customer behavior.
- Add regional and time-based delivery analysis.
- Improve dashboard interactivity and filtering.
- Add automated data-quality tests.
- Publish project documentation and dashboard screenshots.

## Author

Data Analytics Portfolio Project — Python, MySQL, SQL, and Tableau.
