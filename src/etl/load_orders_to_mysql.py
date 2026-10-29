
from pathlib import Path
import os
import getpass

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# 1. Find the project folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# 2. Locate the cleaned CSV
csv_file = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "orders_clean.csv"
)

# 3. Read the CSV
df = pd.read_csv(csv_file)

print("CSV loaded:", len(df), "rows")

# 4. Read MySQL credentials securely
db_user = os.getenv("MYSQL_USER", "root")
db_password = getpass.getpass("Enter MySQL root password: ")

# 5. Configure the database connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username=db_user,
    password=db_password,
    host="localhost",
    port=3306,
    database="retail_analytics",
)

engine = create_engine(connection_url)

# 6. Load data into the existing orders table
try:
    with engine.begin() as connection:
        df.to_sql(
            name="orders",
            con=connection,
            if_exists="append",
            index=False,
            chunksize=1000,
        )

        total_rows = connection.execute(
            text("SELECT COUNT(*) FROM orders")
        ).scalar_one()

    print("Data loaded successfully!")
    print("Rows currently in MySQL:", total_rows)

except Exception as error:
    print("Loading failed:", error)
    raise

finally:
    engine.dispose()
