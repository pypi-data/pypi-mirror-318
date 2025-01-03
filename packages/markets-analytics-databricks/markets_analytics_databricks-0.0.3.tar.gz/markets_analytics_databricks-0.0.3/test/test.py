# Databricks notebook source
from markets_analytics_databricks import GSheetHelper

credentials = dbutils.secrets.get(scope="team-offprice-market-analytics-scope", key="bq_credential")
gsheet = GSheetHelper('1XtGO4Wk0FLHxPLk6lYpF8IstO1ZpIHazi4mm39CK0jo', credentials)
gsheet.read('# Logins', 'D1')
