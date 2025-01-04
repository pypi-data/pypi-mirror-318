# Databricks notebook source
# %pip install --upgrade markets_analytics_databricks
dbutils.library.restartPython()

# COMMAND ----------

# %pip install markets_analytics_databricks --quiet
from markets_analytics_databricks import RedshiftConnector

cred = {
    "host": "vpce-0ce2ac9b6b7bf8385-aomwnrqk.vpce-svc-05892d2f78eca1c10.eu-central-1.vpce.amazonaws.com",
    # "host": "lounge-dwh-production.cotnm1vpt3gw.eu-central-1.redshift.amazonaws.com",
    "port": 5439,
    "database": "production",
    'user': dbutils.secrets.get(scope="team-offprice-market-analytics-scope", key="redshift_user"),
    'password': dbutils.secrets.get(scope="team-offprice-market-analytics-scope", key="redshift_password")
}

redshift = RedshiftConnector(cred)
print(redshift)

# COMMAND ----------

query = """
    CREATE TABLE IF NOT EXISTS sales_and_supply.test_table (
        name VARCHAR(255),
        age INT
    )
"""
redshift.__commit__(query)

query = """
    INSERT INTO sales_and_supply.test_table (name, age) VALUES ('Alice', 30), ('Bob', 12), ('Danz', 19)
"""
redshift.__commit__(query)

query = "SELECT * FROM sales_and_supply.test_table"
df = redshift.execute(query)
df

# COMMAND ----------

redshift.truncate("sales_and_supply", "test_table")

query = "SELECT * FROM sales_and_supply.test_table"
df = redshift.execute(query)
df

# COMMAND ----------

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Danz"],
    "age": [30, 12, 19]
})

df2 = pd.DataFrame({
    'name': ['Kash', 'Vik', 'Pat'],
    'age': [30, 12, 19]
})

redshift.insert(df, "sales_and_supply", "test_table", "offprice-markets-databricks-test")
redshift.insert(df2, "sales_and_supply", "test_table", "offprice-markets-databricks-test", "append")

query = "SELECT * FROM sales_and_supply.test_table"
df = redshift.execute(query)
df

# COMMAND ----------

df = pd.DataFrame({
    'name': ['Kash', 'Vik', 'Pat'],
    'age': [30, 12, 19]
})

redshift.insert(df2, "sales_and_supply", "test_table", "offprice-markets-databricks-test", "overwrite")

query = "SELECT * FROM sales_and_supply.test_table"
df = redshift.execute(query)
df

# COMMAND ----------


