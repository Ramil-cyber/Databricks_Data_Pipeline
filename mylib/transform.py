from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, concat_ws


def transform_data(source, target):
    """Apply transformations to add a medal scoring column
      and a combined discipline-event column."""
 
    spark = SparkSession.builder.appName('temp').getOrCreate()

    df = spark.read.table(source)

    transformed_df = df.withColumn(
        "total_market_value_numeric",
        when(col("total_market_value").startswith("€"), 
            col("total_market_value").substr(2, 100).cast("float"))
        .otherwise(None)
    )

    transformed_df = transformed_df.withColumn(
        "market_value_per_player",
        when(
            (col("squad_size").isNotNull()) \
                & (col("total_market_value_numeric").isNotNull()),
            col("total_market_value_numeric") / col("squad_size")
        ).otherwise(None)
    )

    # Transformation: Merge columns into club_summary
    transformed_df = transformed_df.withColumn(
        "club_summary",
        concat_ws(" - ", col("club_code"), col("name"), col("domestic_competition_id"))
    )

    transformed_df.write.format("delta").mode("append").saveAsTable(target)


    return transformed_df.show()
  

if  __name__ == "__main__":
    transform_data("rm564_clubs", "rm564_clubs_transform")




