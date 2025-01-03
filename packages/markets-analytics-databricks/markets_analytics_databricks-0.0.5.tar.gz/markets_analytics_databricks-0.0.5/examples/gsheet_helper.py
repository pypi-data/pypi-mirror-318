# Databricks notebook source
# MAGIC %pip install markets_analytics_databricks --quiet
# MAGIC from markets_analytics_databricks import GSheetHelper
# MAGIC
# MAGIC credentials = dbutils.secrets.get(scope="team-offprice-market-analytics-scope", key="bq_credential")
# MAGIC gsheet = GSheetHelper('1XtGO4Wk0FLHxPLk6lYpF8IstO1ZpIHazi4mm39CK0jo', credentials)
# MAGIC gsheet.read('# Logins', 'D1')

# COMMAND ----------

# from markets_analytics_databricks import RedshiftConnector

cred = {
    "host": "vpce-0ce2ac9b6b7bf8385-aomwnrqk.vpce-svc-05892d2f78eca1c10.eu-central-1.vpce.amazonaws.com",
    # "host": "lounge-dwh-production.cotnm1vpt3gw.eu-central-1.redshift.amazonaws.com",
    "port": 5439,
    "database": "production",
    'username': dbutils.secrets.get(scope="team-offprice-market-analytics-scope", key="redshift_user"),
    'password': dbutils.secrets.get(scope="team-offprice-market-analytics-scope", key="redshift_password")
}

print(cred)


# COMMAND ----------

dbutils.secrets.list("team-offprice-market-analytics-scope")

# COMMAND ----------

dbutils.fs.ls('s3://offprice-markets-databricks-test/temp/test_table')
