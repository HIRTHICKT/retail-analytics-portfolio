# Retail Analytics — Project Findings

## 1. Project Objective

Analyze Brazilian e-commerce order data to understand order-status distribution and evaluate delivery performance and operational efficiency.

## 2. Dataset Overview

- **Total order records:** 99,441
- **Unique order IDs:** 99,441
- **Data source:** Brazilian E-Commerce Public Dataset by Olist

## 3. Key Findings

| Metric | Result |
|---|---:|
| Total orders | 99,441 |
| Delivered orders | 96,478 |
| Delivered share of all orders | 97.02% |
| Average delivery duration | 12.56 days |
| Late delivered orders | 7,826 |
| Late-delivery rate | 8.11% |
| Average delivery delay | -11.18 days |

## 4. Interpretation

- Delivered orders account for approximately **97.02% of all recorded orders**.
- The average delivery duration is approximately **12.56 days**, calculated using orders with valid purchase and delivery timestamps.
- A total of **7,826 delivered orders** were delivered after their estimated delivery dates.
- The late-delivery rate is **8.11%**, calculated by dividing late delivered orders by all delivered orders (96,478).
- The average delivery delay is **-11.18 days**, indicating that orders were delivered earlier than their estimated dates on average.

## 5. Data Quality

- The dataset contains 99,441 unique order IDs, with no duplicate order IDs.
- Some records have missing approval and delivery timestamps.
- Missing delivery durations and delay values were preserved as missing values rather than replaced with zero.
- Delivery duration is calculated as the time between purchase and actual customer delivery.
- Delivery delay is calculated as the difference between actual customer delivery and estimated delivery dates. Positive values indicate late delivery; negative values indicate early delivery.

## 6. Tools and Technologies Used

- **Python:** Data processing and cleaning
- **pandas:** Data manipulation and analysis
- **MySQL:** Data storage
- **SQL:** Data validation, aggregation, and KPI calculations
- **Tableau:** Dashboard development and visualization

## 7. Recommended Next Steps

Future enhancements could include:

- Analyzing sales revenue and payment methods.
- Identifying top-performing product categories.
- Comparing delivery performance across customer regions.
- Analyzing monthly order and delivery trends.
- Adding interactive dashboard filters and additional business KPIs.

---

**Dashboard Preview**

![Retail Analytics Dashboard](dashboard_screenshot.png)
