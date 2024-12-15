from extract import extract_csv
from pyspark.sql import SparkSession


 
def load(df):
    spark = SparkSession.builder.getOrCreate()
    spark_df = spark.createDataFrame(df)
    
    spark_df.write.format("delta").mode("append").saveAsTable("rm564_clubs")
    
    print('Data loaded into Databricks succesfully!')


if __name__ == '__main__':
    df = extract_csv(
        'https://raw.githubusercontent.com/nogibjj/Ramil-Data-Pipeline-Databricks/refs/heads/main/data/Clubs.csv'
    )

    load(df)

