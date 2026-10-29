
from pathlib import Path
import pandas as pd

# 1. Find the project folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# 2. Define input and output files
input_file = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "olist"
    / "olist_orders_dataset.csv"
)

output_file = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "orders_clean.csv"
)

# 3. Load the raw dataset
orders = pd.read_csv(input_file)
print("Raw data loaded:", orders.shape)

# 4. Convert date columns into datetime format
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column], errors="coerce"
    )

# 5. Validate important fields
assert orders["order_id"].is_unique, "Duplicate order IDs found"
assert orders["order_purchase_timestamp"].notna().all(), (
    "Missing purchase timestamps found"
)

# 6. Calculate actual delivery duration
orders["delivery_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.total_seconds() / 86400

# 7. Calculate delay against the estimated delivery date
orders["delivery_delay_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

# 8. Create the output folder if needed
output_file.parent.mkdir(parents=True, exist_ok=True)

# 9. Save the cleaned dataset
orders.to_csv(output_file, index=False)

# 10. Print a quality summary
print("\nETL completed successfully!")
print("Total rows:", len(orders))
print("Unique orders:", orders["order_id"].nunique())
print("Missing delivery durations:", orders["delivery_days"].isna().sum())
print("Negative delivery durations:", (orders["delivery_days"] < 0).sum())
print("Output saved to:", output_file)
