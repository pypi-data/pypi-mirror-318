import psycopg2

import pandas as pd
import datetime as dt

class RedshiftConnector:
    # Constructor
    def __init__(self, cred):
        """
            Initializing connection details and testing out the connection to Redshift
        """
        self.host = cred["host"]
        self.port = cred["port"]
        self.database = cred["database"]
        self.__user__ = cred["user"]
        self.__password__ = cred["password"]

        self.__connect__()
        self.__disconnect__()

    # Connect
    def __connect__(self):
        """
            Connecting to the Redshift Server instance
        """
        try:
            self.__conn__ = psycopg2.connect(host=self.host, port=self.port, database=self.database, user=self.__user__, password=self.__password__)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Redshift: {e}")

    # Disconnect
    def __disconnect__(self):
        """
            Disconnecting from the Redshift Server instance
        """

        if self.__conn__ is not None:
            self.__conn__.close()

    # Commit
    def __commit__(self, query):
        """
            Committing the query to the Redshift Server
        """
        self.__connect__()
        cursor = self.__conn__.cursor()
        cursor.execute(query)
        self.__conn__.commit()
        cursor.close()
        self.__disconnect__()

    # Print
    def __str__(self):
        """
            Printing which user is connected to what instance of Redshift Server
        """

        if self.__user__ is None:
            return "No Connection Established to any Redshift Server"
        return f"User: {self.__user__} is Connected to Redshift Server: {self.host}:{self.port}/{self.database}"
    
    # Execute Query
    def execute(self, query, log=True):
        """
            Executing the SQL query and returning it as a Pandas DataFrame
        """
        if log: print(f"[{dt.datetime.now()}] Executing Query\n{query}")

        self.__connect__()
        df = pd.read_sql_query(query, self.__conn__)
        self.__disconnect__()

        if log: print(f"[{dt.datetime.now()}] Query Executed Successfully")

        return df
    
    # Truncate
    def truncate(self, schema, table, log=True):
        """
            Deleting all the data stored in the table
        """
        if log: print(f"[{dt.datetime.now()}] Truncating Table: {schema}.{table}")

        query = f"TRUNCATE TABLE {schema}.{table}"
        self.__commit__(query)

        if log: print(f"[{dt.datetime.now()}] Table Truncated Successfully")
    
    # Delete
    def delete(self, schema, table, condition, log=True):
        """
            Deleting rows from the table that match the specified condition
        """
        if log: print(f"Deleting from {schema}.{table} where {condition}")

        if condition is None:
            self.truncate(schema, table)
        else:
            query = f"DELETE FROM {schema}.{table} WHERE {condition}"
            self.__commit__(query)

        if log: print(f"[{dt.datetime.now()}] Delete Executed Successfully")

    # Update
    def update(self, schema, table, value, condition, log=True):
        """
            Updating certain rows with values in the table that match the specified condition
        """
        if log: print(f"Updating {schema}.{table} with {value} where {condition}")

        query = f"UPDATE {schema}.{table} SET {value} WHERE {condition}"
        self.__commit__(query)

        if log: print(f"[{dt.datetime.now()}] Update Executed Successfully")

    # Insert
    def insert(self, df, schema, table, s3_bucket, spark, dbutils, mode="append"):
        """
            Inserting data into the table using the s3 bucket
        """
        print(f"[{dt.datetime.now()}] Inserting Data into {schema}.{table}")

        s3_temp_path = f"s3://{s3_bucket}/temp/{table}"

        # Removing temporary files to avoid distorting our final dataset
        files = dbutils.fs.ls(s3_temp_path)
        for file in files:
            dbutils.fs.rm(file.path, True)

        # Converting pandas DataFrame into a Spark DataFrame and saving it as parquet file
        spark_df = spark.createDataFrame(df)
        spark_df.write.parquet(s3_temp_path, mode=mode)
        spark_df = spark.read.parquet(s3_temp_path)

        # Writing data to Redshift via S3 Bucket
        (spark_df.write
          .format("com.databricks.spark.redshift")
          .option("url", f"jdbc:redshift://{self.host}:{self.port}/{self.database}?user={self.__user__}&password={self.__password__}&ssl=false")
          .option("dbtable", f"{schema}.{table}")
          .option("tempdir", s3_temp_path)
          .option("forward_spark_s3_credentials", "true")
          .mode(mode)
          .save())
    
        print(f"[{dt.datetime.now()}] Data Inserted Successfully")