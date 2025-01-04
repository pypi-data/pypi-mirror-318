# Databricks notebook source
# MAGIC %pip install markets_analytics_databricks==0.0.9
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

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
    DROP TABLE IF EXISTS sales_and_supply.test_table;

    CREATE TABLE IF NOT EXISTS sales_and_supply.test_table (
        name VARCHAR(255),
        age INT
    );
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

redshift.insert(df, "sales_and_supply", "test_table", "offprice-markets-databricks-test", spark)
redshift.insert(df2, "sales_and_supply", "test_table", "offprice-markets-databricks-test", spark, "append")

query = "SELECT * FROM sales_and_supply.test_table"
df = redshift.execute(query)
df

# COMMAND ----------

files = dbutils.fs.ls('s3://offprice-markets-databricks-test/temp/test_table')
for file in files:
    print(file.path)
    dbutils.fs.rm(file.path, True)

dbutils.fs.ls('s3://offprice-markets-databricks-test/temp/test_table')

# COMMAND ----------

df = pd.DataFrame({
    'name': ['Kash', 'Vik', 'Pat'],
    'age': [30, 12, 19]
})

redshift.insert(df2, "sales_and_supply", "test_table", "offprice-markets-databricks-test", spark, "overwrite")

query = "SELECT * FROM sales_and_supply.test_table"
df = redshift.execute(query)
df

# COMMAND ----------

redshift.update("sales_and_supply", "test_table", "age = 29", "name = 'Pat'")

query = "SELECT * FROM sales_and_supply.test_table"
df = redshift.execute(query)
df

# COMMAND ----------

redshift.delete("sales_and_supply", "test_table", "age = 29 OR name LIKE 'V%'")

query = "SELECT * FROM sales_and_supply.test_table"
df = redshift.execute(query)
df
