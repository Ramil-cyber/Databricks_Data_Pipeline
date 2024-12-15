"""
Main cli or app entry point
"""
from mylib.lib import (
    extract_csv,
    run_spark_sql_query,
    transform_data,
    display_summary_statistics,
    load_dataframe,
    terminate_spark_session,
    initialize_spark_session,
)


def pyspark_process():

    extract_csv(
        "https://raw.githubusercontent.com/nogibjj/Ramil-Complex-SQL-Query-MySQL-Database/refs/heads/main/data/clubs.csv",
        file_name="Clubs.csv",
        target_directory="data",
    )

    spark = initialize_spark_session("Initial")

    df = load_dataframe(spark)

    display_summary_statistics(df)

    run_spark_sql_query(
        spark,
        df,
        sql_query="""
            SELECT 
                domestic_competition_id,
                SUM(squad_size) AS total_squad_size
            FROM 
                Clubs
            GROUP BY 
                domestic_competition_id
            ORDER BY 
                total_squad_size DESC
        """,
        temp_view_name="Clubs",
    )

    transform_data(df)

    terminate_spark_session(spark)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    pyspark_process()
